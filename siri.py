import os
import time
import json
import datetime
import re
import random
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
import groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SERVICE_REGION = os.getenv("AZURE_SPEECH_REGION")

# Initialize speech services
def initialize_speech_services():
    try:
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
        speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
        
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        
        return speech_config, speech_synthesizer, speech_recognizer
    except Exception as e:
        print(f"Error initializing speech services: {e}")
        return None, None, None

# Speech conversion functions
def speak(text, speech_synthesizer):
    """Convert text to speech using Azure"""
    print(f"Dr. Maya: {text}")
    try:
        result = speech_synthesizer.speak_text_async(text).get()
        if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesis failed")
            return False
        return True
    except Exception as e:
        print(f"Speech synthesis error: {e}")
        return False

def listen(speech_recognizer, timeout=10):
    """Listen to user's voice input using Azure, waits until user finishes speaking."""
    print("Listening... Speak now!")
    try:
        # Set timeout for silence (in milliseconds)
        speech_recognizer.properties.set_property(
            speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs,
            str(timeout * 1000)
        )
        result = speech_recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            text = result.text
            print(f"You: {text}")
            return text
        else:
            print("No speech recognized")
            return None
    except Exception as e:
        print(f"Speech recognition error: {e}")
        return None

# Chat function using Groq
def chat(history, client=None):
    """Get response from Groq API, always include current date and time as context."""
    if client is None:
        client = groq.Client(api_key=GROQ_API_KEY)
    
    # Insert current date and time as a system message at the start of the history
    now = datetime.datetime.now()
    date_context = {
        "role": "system",
        "content": f"Current date and time: {now.strftime('%A, %B %d, %Y, %I:%M %p')}"
    }
    # Avoid duplicating the date context if already present
    if not (history and history[0].get("role") == "system" and "Current date and time:" in history[0].get("content", "")):
        history = [date_context] + history
    else:
        history[0] = date_context

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=history,
            max_tokens=120,  # Lowered for concise responses
            temperature=0.7
        )
        assistant_response = response.choices[0].message.content
        print(f"\nGroq Response: {assistant_response}")
        return assistant_response
    except Exception as e:
        print(f"Groq API error: {e}")
        return "I'm having trouble connecting to my systems right now. Could you please try again in a moment?"

# Appointment extraction and management
def extract_appointment_details(history):
    """Extract appointment details from the conversation history"""
    # Create a summary request
    summary_history = history.copy()
    summary_history.append({
        "role": "user", 
        "content": "Please extract any appointment details from our conversation. If an appointment was discussed, provide the following in JSON format: {\"appointment\": true, \"patient_name\": \"[name]\", \"date\": \"[date]\", \"time\": \"[time]\", \"doctor\": \"[doctor]\", \"reason\": \"[reason]\", \"contact\": \"[contact]\"}. If no appointment was made, respond with {\"appointment\": false}."
    })
    
    client = groq.Client(api_key=GROQ_API_KEY)
    response = chat(summary_history, client)
    
    # Try to extract JSON from response
    try:
        # Look for JSON pattern in the response
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            appointment_data = json.loads(json_match.group(0))
            return appointment_data
        else:
            return {"appointment": False}
    except Exception as e:
        print(f"Error extracting appointment details: {e}")
        return {"appointment": False}

def save_appointment(appointment_data):
    """Save appointment details to a file"""
    try:
        # Create appointments directory if it doesn't exist
        if not os.path.exists("appointments"):
            os.makedirs("appointments")
        
        # Generate a unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"appointments/appointment_{timestamp}.json"
        
        # Save the appointment data
        with open(filename, "w") as f:
            json.dump(appointment_data, f, indent=4)
        
        print(f"Appointment saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving appointment: {e}")
        return False

# Function to save conversation history
def save_conversation(history):
    """Save the conversation history to a file"""
    try:
        # Create conversations directory if it doesn't exist
        if not os.path.exists("conversations"):
            os.makedirs("conversations")
        
        # Generate a unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversations/conversation_{timestamp}.json"
        
        # Save the conversation data
        with open(filename, "w") as f:
            json.dump(history, f, indent=4)
        
        print(f"Conversation saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving conversation: {e}")
        return False

# Check for health emergency keywords
def check_emergency(text):
    """Check if the user text indicates a medical emergency"""
    emergency_keywords = [
        "heart attack", "stroke", "not breathing", "bleeding", "unconscious",
        "choking", "seizure", "suicide", "dying", "emergency", "911", "help me now",
        "can't breathe", "chest pain", "severe pain"
    ]
    
    if text:
        text_lower = text.lower()
        for keyword in emergency_keywords:
            if keyword in text_lower:
                return True
    return False

# Main conversation flow
def main_conversation():
    """Main conversation loop with the medical assistant"""
    # Initialize services
    speech_config, speech_synthesizer, speech_recognizer = initialize_speech_services()
    if speech_synthesizer is None or speech_recognizer is None:
        print("Failed to initialize speech services. Exiting.")
        return
    
    # Initialize Groq client
    client = groq.Client(api_key=GROQ_API_KEY)
    
    # Initialize conversation history
    history = [
        {
            "role": "system",
            "content": """You are Dr. Maya, a medical assistant AI. You have a warm, friendly, and slightly sassy personality.
            
            Key behaviors:
            - For medical advice, always be professional and accurate.
            - If the user mentions symptoms that could be an emergency, immediately advise them to call 911 or go to an emergency room.
            - You can make appropriate jokes and be conversational, but prioritize accurate medical information.
            - When booking appointments, collect necessary information like name, contact details, preferred date/time, symptoms, and medical history.
            - If the user asks about non-medical topics, you can engage briefly but gently redirect to health topics.
            - You can represent a fictional medical clinic called "Wellness Medical Center" with fictional doctors.
            
            Available doctors (use these when scheduling):
            - Dr. Sarah Johnson (Cardiologist)
            - Dr. Michael Chen (Family Medicine)
            - Dr. Priya Patel (Pediatrician)
            - Dr. Robert Wilson (Dermatologist)
            - Dr. Lisa Garcia (Neurologist)
            
            Keep your responses concise but informative.Keep your response short as much as possible and simple. Break complex information into smaller chunks. At no point should you say "I'm an AI" or refer to yourself as an AI - you are simply Dr. Maya, the medical assistant at Wellness Medical Center.
            """
        }
    ]
    
    # Welcome message
    welcome_message = "Hello! This is Dr. Maya from Wellness Medical Center. How can I help you today?"
    speak_success = speak(welcome_message, speech_synthesizer)
    if not speak_success:
        print("Unable to speak welcome message. Exiting.")
        return
    
    history.append({"role": "assistant", "content": welcome_message})
    
    # Main conversation loop
    exit_phrases = ["goodbye", "bye", "exit", "end", "quit", "thank you", "thanks"]
    conversation_active = True
    
    while conversation_active:
        # Listen for user input
        user_input = listen(speech_recognizer)
        
        # Check if user said anything
        if user_input is None:
            speak("I didn't catch that. Could you please repeat?", speech_synthesizer)
            continue
        
        # Check for exit phrases
        if any(phrase in user_input.lower() for phrase in exit_phrases):
            # At the end, ask Groq to summarize the conversation and provide appointment details
            today = datetime.date

            summary_prompt = {
                "role": "user",
                "content": (
                    f"date is {today} "
                    "Please summarize our conversation. If the user requested an appointment, "
                    "provide the appointment details (name, contact, reason, date, time, doctor) in a clear format. "
                    "If no appointment was requested, just summarize the conversation."
                )
            }
            history.append(summary_prompt)
            summary_response = chat(history, client)
            speak("Here's a summary of our conversation:", speech_synthesizer)
            speak(summary_response, speech_synthesizer)
            print("Summary:", summary_response)
            # Save conversation history
            save_conversation(history)
            conversation_active = False
            continue
        
        # Check for emergency keywords
        if check_emergency(user_input):
            emergency_message = "This sounds like a medical emergency. Please call 911 or go to the nearest emergency room immediately. Would you like me to continue helping you with other information?"
            speak(emergency_message, speech_synthesizer)
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": emergency_message})
            continue
        
        # Add user input to history
        history.append({"role": "user", "content": user_input})
        
        # Get response from Groq
        assistant_response = chat(history, client)
        
        # Speak the response
        speak(assistant_response, speech_synthesizer)
        
        # Add assistant response to history
        history.append({"role": "assistant", "content": assistant_response})

# Wake word detection (simplified)
def detect_wake_word():
    """Simple wake word detection"""
    print("Listening for wake word ('Hey Maya' or 'Medical Assistant')...")
    
    # Initialize speech services for wake word detection
    speech_config, speech_synthesizer, speech_recognizer = initialize_speech_services()
    if speech_recognizer is None:
        print("Failed to initialize speech recognizer. Exiting.")
        return False
    
    # Listen for wake word
    while True:
        user_input = listen(speech_recognizer, timeout=3)
        if user_input:
            user_input_lower = user_input.lower()
            wake_words = ["hey maya", "medical assistant", "medycall", "assistant", "hey", "maya"]
            
            if any(word in user_input_lower for word in wake_words):
                print("Wake word detected!")
                return True
        
        # Add a small delay to prevent excessive CPU usage
        time.sleep(0.5)

# Main function
def main():
    """Main function to run the medical assistant"""
    try:
        # Check if environment variables are set
        if not all([GROQ_API_KEY, SPEECH_KEY, SERVICE_REGION]):
            print("Error: Missing required environment variables. Please check your .env file.")
            return
        
        print("Starting Medical Assistant...")
        
        # Detect wake word
        wake_word_detected = detect_wake_word()
        
        if wake_word_detected:
            # Start main conversation
            main_conversation()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()