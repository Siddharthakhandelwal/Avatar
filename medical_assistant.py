import datetime
import time
import random
import os
import json
import re
from dotenv import load_dotenv
import requests
import azure.cognitiveservices.speech as speechsdk
import pyttsx3
from conversation_flow import ConversationState, ConversationStage, generate_structured_prompt, generate_appointment_pdf
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get environment variables with defaults
SPEECH_TIMEOUT = int(os.getenv('SPEECH_TIMEOUT', '5'))
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')

# Initialize text-to-speech engine as fallback
engine = pyttsx3.init()

# Azure Speech Service setup
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY", "F9Gcgcr3uBODrscmhrMUEaorbV6WF9H6bqc4kghYsNqvcux9ZavxJQQJ99BCACYeBjFXJ3w3AAAYACOGYQHZ")
SERVICE_REGION = os.getenv("AZURE_SPEECH_REGION", "eastus")
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# Add voice settings for more natural sound
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"  # Warm, professional female voice

# Assistant personality settings
assistant_name = "Dr. Maya"
hospital_name = "Wellness Care Center"
current_date = datetime.datetime.now().strftime("%A, %B %d")

# Medical knowledge base (enhanced with more detailed information)
medical_conditions = {
    "headache": {
        "symptoms": ["pain in head", "throbbing", "pressure", "pounding", "temple pain", "migraine", "tension", "cluster"],
        "possible_causes": ["stress", "dehydration", "lack of sleep", "eyestrain", "tension", "migraine", "sinus congestion"],
        "suggested_remedies": ["adequate rest in a quiet, dark room", "staying hydrated", "over-the-counter pain relievers like acetaminophen", "applying a cool compress to your forehead", "gentle massage of the temples"],
        "severity": "low to medium",
        "follow_up": "If your headache persists for more than 3 days or is accompanied by fever, please consult with a physician."
    },
    "common cold": {
        "symptoms": ["runny nose", "cough", "sore throat", "sneezing", "congestion", "post-nasal drip", "mild fever", "fatigue"],
        "possible_causes": ["viral infection", "rhinovirus", "seasonal changes", "weakened immune system"],
        "suggested_remedies": ["plenty of rest", "increased fluid intake", "over-the-counter cold medicine", "saline nasal spray", "throat lozenges", "warm tea with honey"],
        "severity": "low",
        "follow_up": "Most colds resolve within 7-10 days. If symptoms worsen after 5 days or you develop a high fever, please contact your doctor."
    },
    "fever": {
        "symptoms": ["elevated temperature", "chills", "sweating", "body aches", "headache", "weakness", "fatigue", "loss of appetite"],
        "possible_causes": ["infection", "inflammation", "heat exhaustion", "reaction to medication", "immune response"],
        "suggested_remedies": ["rest", "staying hydrated with water and electrolyte solutions", "fever reducers like acetaminophen", "light clothing", "cool compresses"],
        "severity": "medium",
        "follow_up": "For fevers above 102°F (39°C) or any fever lasting more than 3 days, please seek medical attention."
    },
    "stomachache": {
        "symptoms": ["abdominal pain", "nausea", "bloating", "cramping", "indigestion", "gas", "heartburn", "discomfort"],
        "possible_causes": ["indigestion", "food poisoning", "gas", "stomach virus", "acid reflux", "stress", "overeating"],
        "suggested_remedies": ["light, bland diet like the BRAT diet (bananas, rice, applesauce, toast)", "ginger tea", "probiotics", "small, frequent meals", "avoiding spicy and fatty foods"],
        "severity": "low to medium",
        "follow_up": "If you experience severe pain, blood in stool, persistent vomiting, or symptoms lasting more than 2 days, please see a healthcare provider."
    },
    "sore throat": {
        "symptoms": ["throat pain", "difficulty swallowing", "scratchiness", "irritation", "hoarseness", "dry throat"],
        "possible_causes": ["viral infection", "bacterial infection", "allergies", "dry air", "strain from overuse", "acid reflux"],
        "suggested_remedies": ["warm saltwater gargles", "throat lozenges", "warm tea with honey", "staying hydrated", "using a humidifier", "resting your voice"],
        "severity": "low to medium",
        "follow_up": "If your sore throat is severe, lasts more than a week, or is accompanied by difficulty breathing, please seek medical care right away."
    },
    "allergies": {
        "symptoms": ["sneezing", "itchy eyes", "runny nose", "congestion", "skin rash", "hives", "coughing"],
        "possible_causes": ["pollen", "dust mites", "pet dander", "mold", "certain foods", "seasonal changes"],
        "suggested_remedies": ["over-the-counter antihistamines", "nasal sprays", "avoiding known allergens", "air purifiers", "washing bedding frequently", "shower after outdoor activities"],
        "severity": "low",
        "follow_up": "For severe allergic reactions with breathing difficulties or swelling, seek emergency care immediately."
    }
}

# Drugs database (enhanced with more medical details)
medication_database = {
    "headache": [
        {"name": "Acetaminophen (Tylenol)", "dosage": "325-650mg every 4-6 hours as needed", "note": "Avoid alcohol while taking this medication."},
        {"name": "Ibuprofen (Advil)", "dosage": "200-400mg every 4-6 hours with food", "note": "Not recommended for those with stomach ulcers or kidney problems."},
        {"name": "Aspirin", "dosage": "325-650mg every 4-6 hours with food", "note": "Not recommended for children under 18 or those with bleeding disorders."}
    ],
    "common cold": [
        {"name": "Pseudoephedrine", "dosage": "60mg every 4-6 hours, not to exceed 240mg daily", "note": "May cause insomnia if taken near bedtime."},
        {"name": "Dextromethorphan", "dosage": "10-20mg every 4 hours for cough, not to exceed 120mg daily", "note": "Helps suppress cough."},
        {"name": "Chlorpheniramine", "dosage": "4mg every 4-6 hours, not to exceed 24mg daily", "note": "May cause drowsiness."}
    ],
    "fever": [
        {"name": "Acetaminophen (Tylenol)", "dosage": "325-650mg every 4-6 hours as needed", "note": "Effective for reducing fever."},
        {"name": "Ibuprofen (Advil)", "dosage": "200-400mg every 4-6 hours with food", "note": "Helpful for fever and associated aches."}
    ],
    "stomachache": [
        {"name": "Bismuth subsalicylate (Pepto-Bismol)", "dosage": "30mL or 2 tablets every 30-60 minutes as needed", "note": "May cause temporary darkening of tongue and stool."},
        {"name": "Loperamide (Imodium)", "dosage": "4mg initially, then 2mg after each loose stool, not to exceed 8mg daily", "note": "For diarrhea symptoms only."}
    ],
    "sore throat": [
        {"name": "Throat lozenges/sprays", "dosage": "As directed on package", "note": "Provides temporary relief for mild sore throat."},
        {"name": "Acetaminophen (Tylenol)", "dosage": "325-650mg every 4-6 hours as needed", "note": "For pain relief."}
    ],
    "allergies": [
        {"name": "Cetirizine (Zyrtec)", "dosage": "10mg once daily", "note": "Non-drowsy for most people."},
        {"name": "Loratadine (Claritin)", "dosage": "10mg once daily", "note": "Non-drowsy antihistamine."},
        {"name": "Diphenhydramine (Benadryl)", "dosage": "25-50mg every 4-6 hours", "note": "May cause significant drowsiness."}
    ]
}

# Doctor specialties for appropriate referrals
medical_specialties = {
    "headache": ["Neurologist", "Primary Care Physician"],
    "common cold": ["Primary Care Physician", "Family Medicine"],
    "fever": ["Primary Care Physician", "Infectious Disease Specialist"],
    "stomachache": ["Gastroenterologist", "Primary Care Physician"],
    "sore throat": ["Otolaryngologist (ENT)", "Primary Care Physician"],
    "allergies": ["Allergist", "Immunologist", "Primary Care Physician"]
}

# Initialize conversation state for structured flow
conversation_state = ConversationState()

# Greeting templates for more natural conversation
greetings = [
    f"Hello, I'm {assistant_name} from {hospital_name}. How are you feeling today?",
    f"Good day, this is {assistant_name}, your virtual healthcare assistant. What brings you in today?",
    f"Welcome to {hospital_name}'s virtual care. I'm {assistant_name}, how can I assist with your health concerns today?",
    f"Hi there, I'm {assistant_name}, your medical assistant. How may I help you with your health today?"
]

class MedicalAssistant:
    """Core Medical Assistant class that handles medical queries and conversation"""
    
    def __init__(self):
        self.conversation_history = []
        self.patient_info = {
            "name": None,
            "age": None,
            "gender": None,
            "symptoms": [],
            "medical_history": None
        }
        
        # Initialize system prompt for medical capabilities
        self.system_prompt = """
        You are Dr. Maya, an AI medical assistant trained to help patients with preliminary medical queries 
        and advice. Your primary goals are to:
        
        1. Understand patient symptoms and medical concerns
        2. Provide general health information and preliminary guidance
        3. Determine when a patient should see a healthcare professional
        4. Never provide definitive diagnoses - always clarify that proper diagnosis requires a healthcare professional
        5. Identify medical emergencies and direct patients to seek immediate care when necessary
        
        Important rules:
        - Maintain patient privacy and confidentiality
        - Express empathy and compassion in all responses
        - Be clear about your limitations as an AI assistant
        - Provide evidence-based information when possible
        - Use clear, jargon-free language that patients can understand
        - For serious conditions, emphasize the importance of seeking professional medical care
        - Never recommend specific medications, treatments, or dosages
        """
        
        self.conversation_history.append({"role": "system", "content": self.system_prompt})
    
    def process_input(self, user_input):
        """Process user input and generate appropriate response"""
        # Add user input to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Check for emergency keywords
        emergency_keywords = ["heart attack", "stroke", "unconscious", "seizure", "severe bleeding", 
                             "can't breathe", "suicide", "poisoning", "severe pain"]
        
        for keyword in emergency_keywords:
            if keyword in user_input.lower():
                emergency_response = ("This sounds like an emergency. Please call emergency services (911) immediately "
                                     "or go to your nearest emergency room. Do not wait for my response.")
                self.conversation_history.append({"role": "assistant", "content": emergency_response})
                return emergency_response
        
        try:
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                max_tokens=400
            )
            
            assistant_response = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            # Update patient info based on response if needed
            self._update_patient_info(user_input)
            
            return assistant_response
            
        except Exception as e:
            error_msg = f"I apologize, but I'm experiencing technical difficulties. Error: {str(e)}"
            self.conversation_history.append({"role": "assistant", "content": error_msg})
            return error_msg
    
    def _update_patient_info(self, user_input):
        """Extract and update patient information from user input"""
        # Basic information extraction (simple version)
        input_lower = user_input.lower()
        
        # Extract name
        if "my name is" in input_lower and not self.patient_info["name"]:
            name_parts = input_lower.split("my name is")
            if len(name_parts) > 1:
                self.patient_info["name"] = name_parts[1].strip().title()
        
        # Extract age
        if "years old" in input_lower and not self.patient_info["age"]:
            for word in input_lower.split():
                if word.isdigit() and 1 <= int(word) <= 120:
                    self.patient_info["age"] = int(word)
                    break
        
        # Extract gender
        if not self.patient_info["gender"]:
            if "male" in input_lower and "female" not in input_lower:
                self.patient_info["gender"] = "Male"
            elif "female" in input_lower:
                self.patient_info["gender"] = "Female"
        
        # Extract symptoms
        symptom_keywords = ["pain", "ache", "fever", "cough", "headache", "nausea", 
                          "tired", "fatigue", "dizzy", "sore", "rash", "swelling"]
        
        for keyword in symptom_keywords:
            if keyword in input_lower and keyword not in self.patient_info["symptoms"]:
                self.patient_info["symptoms"].append(keyword)
    
    def get_patient_info(self):
        """Return current patient information"""
        return self.patient_info
    
    def reset_conversation(self):
        """Reset the conversation history while keeping system prompt"""
        self.conversation_history = [self.conversation_history[0]]
        self.patient_info = {
            "name": None,
            "age": None,
            "gender": None,
            "symptoms": [],
            "medical_history": None
        }

def get_medical_assistant():
    """Factory function to create and return a MedicalAssistant instance"""
    return MedicalAssistant()

def run_test_sequence():
    """Run a test sequence to verify the medical assistant is working properly"""
    assistant = get_medical_assistant()
    
    test_inputs = [
        "Hello, I'm not feeling well today",
        "My name is John and I'm 45 years old",
        "I've been having headaches and fever for the past 3 days",
        "The pain is mostly in the front of my head",
        "I have a history of high blood pressure"
    ]
    
    print("Running test sequence...")
    for test_input in test_inputs:
        print(f"\nUser: {test_input}")
        response = assistant.process_input(test_input)
        print(f"Assistant: {response}")
    
    print("\nPatient information gathered:")
    print(assistant.get_patient_info())
    
    return "Test sequence completed successfully"

def speak(text):
    """Convert text to speech using Azure Speech Service"""
    print(f"{assistant_name}: {text}")
    try:
        result = speech_synthesizer.speak_text_async(text).get()
        if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Azure speech synthesis failed, falling back to pyttsx3")
            engine.say(text)
            engine.runAndWait()
    except Exception as e:
        print(f"Azure speech synthesis error: {e}, falling back to pyttsx3")
        engine.say(text)
        engine.runAndWait()

def listen():
    """Listen to user's voice input using Azure Speech Service"""
    print("Listening... Speak now!")
    try:
        result = speech_recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            text = result.text
            print(f"You: {text}")
            return text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized.")
            speak("I'm sorry, I didn't quite catch that. Could you please speak a little more clearly?")
            return None
        elif result.reason == speechsdk.ResultReason.Canceled:
            print("Speech recognition canceled:", result.cancellation_details.reason)
            speak("I apologize, but there seems to be an issue with our voice recognition system. Let's try again, shall we?")
            return None
    except Exception as e:
        print(f"Error in speech recognition: {e}")
        speak("I'm experiencing some technical difficulties with my hearing. Please try speaking again.")
        return None

def get_time_of_day_greeting():
    """Return a time-appropriate greeting"""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def get_groq_response(user_input):
    """Get response from Groq model with structured conversation flow"""
    if not GROQ_API_KEY:
        print("No Groq API key provided, falling back to rule-based responses")
        return generate_medical_response(user_input)
    
    try:
        # Generate structured prompt based on conversation stage
        prompt, context = generate_structured_prompt(
            conversation_state, 
            user_input, 
            assistant_name, 
            hospital_name
        )
        
        # Prepare conversation context for Groq
        messages = []
        
        # Add system prompt
        messages.append({"role": "system", "content": prompt})
        
        # Add patient context if available
        if context:
            messages.append({"role": "system", "content": context})
        
        # Add relevant conversation history (last 5 exchanges)
        for msg in conversation_state.conversation_history[-10:]:
            role = msg.get("role", "user")  # Default to user if role not specified
            messages.append({"role": role, "content": msg.get("content", "")})
        
        # Call Groq API
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messages": messages,
            "model": "llama3-8b-8192",  # Using Llama 3 model (can be changed to other Groq models)
            "temperature": 0.7,
            "max_tokens": 800,
            "top_p": 0.9
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            response_json = response.json()
            message_content = response_json["choices"][0]["message"]["content"]
            
            # Add assistant response to conversation history
            conversation_state.add_to_history("assistant", message_content)
            
            # Check if we need to generate a PDF
            if conversation_state.current_stage == ConversationStage.CONFIRMING_APPOINTMENT and conversation_state.needs_pdf:
                if conversation_state.patient_info["appointment"]:
                    filename = generate_appointment_pdf(
                        conversation_state.patient_info["appointment"],
                        conversation_state.patient_info,
                        hospital_name
                    )
                    conversation_state.patient_info["appointment_file"] = filename
                    conversation_state.needs_pdf = False
                    message_content += f"\n\nI've generated a PDF with your appointment details. You can find it at {filename}."
            
            return message_content
        else:
            print(f"Error from Groq API: {response.status_code}, {response.text}")
            return generate_medical_response(user_input)
            
    except Exception as e:
        print(f"Error with Groq API: {e}")
        return generate_medical_response(user_input)

def generate_medical_response(prompt):
    """Generate a rule-based medical-style response when APIs are unavailable"""
    prompt_lower = prompt.lower()
    
    # Extract patient name if provided
    name_match = re.search(r"my name is (\w+)", prompt_lower)
    if name_match and not conversation_state.patient_info["name"]:
        conversation_state.patient_info["name"] = name_match.group(1).capitalize()
        time_greeting = get_time_of_day_greeting()
        return f"{time_greeting}, {conversation_state.patient_info['name']}. It's nice to meet you. How can I assist with your health concerns today?"
    
    # Check for greeting patterns and personalize if name is known
    if any(word in prompt_lower for word in ["hello", "hi", "hey", "greetings"]):
        time_greeting = get_time_of_day_greeting()
        if conversation_state.patient_info["name"]:
            return f"{time_greeting}, {conversation_state.patient_info['name']}. How are you feeling today? Is there anything specific I can help you with?"
        else:
            return f"{time_greeting}! I'm {assistant_name}, your medical assistant at {hospital_name}. Could you please tell me your name?"
    
    # Check for age information
    age_match = re.search(r"i(?:'|a)m (\d+)(?:\s+years? old)?|(\d+)(?:\s+years? old)", prompt_lower)
    if age_match and not conversation_state.patient_info["age"]:
        age = age_match.group(1) if age_match.group(1) else age_match.group(2)
        conversation_state.patient_info["age"] = age
        return f"Thank you for sharing that you're {age} years old. Could you please provide a phone number or email where we can reach you?"
    
    # Check for contact information
    phone_match = re.search(r"(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})", prompt)
    if phone_match and not conversation_state.patient_info["contact"]:
        conversation_state.patient_info["contact"] = phone_match.group(1)
        return f"Thank you for providing your contact number. Now, could you please tell me what symptoms you're experiencing?"
    
    email_match = re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", prompt)
    if email_match and not conversation_state.patient_info["email"]:
        conversation_state.patient_info["email"] = email_match.group(1)
        return f"Thank you for providing your email address. Now, could you please tell me what symptoms you're experiencing?"
    
    # Check for medical condition keywords
    for condition, info in medical_conditions.items():
        if condition in prompt_lower or any(symptom in prompt_lower for symptom in info["symptoms"]):
            doctor_type = medical_specialties[condition][0]
            follow_up = info["follow_up"]
            response = f"Based on what you're describing, it sounds like you might be experiencing {condition}. This could be due to {', '.join(info['possible_causes'][0:2])}."
            response += f" I would recommend {', '.join(info['suggested_remedies'][0:3])}. {follow_up} If needed, I can help schedule an appointment with a {doctor_type} for you."
            return response
    
    # Check for appointment-related keywords
    if any(word in prompt_lower for word in ["appointment", "book", "schedule", "doctor"]):
        if conversation_state.patient_info["name"] and conversation_state.patient_info["age"] and (conversation_state.patient_info["contact"] or conversation_state.patient_info["email"]):
            conversation_state.update_stage(ConversationStage.BOOKING_APPOINTMENT)
            return f"I'd be happy to help you schedule an appointment, {conversation_state.patient_info['name']}. Could you please tell me what day and time would work best for you?"
        elif not conversation_state.patient_info["name"]:
            return "I'd be glad to help you book an appointment. First, could you please tell me your name?"
        elif not conversation_state.patient_info["age"]:
            return f"Before we book your appointment, {conversation_state.patient_info['name']}, could you please tell me your age?"
        else:
            return f"To book your appointment, {conversation_state.patient_info['name']}, I'll need a contact number or email. Could you please provide that information?"
    
    # Check for medicine-related keywords
    if any(word in prompt_lower for word in ["medicine", "medication", "drug", "pill"]):
        return "Before I can recommend any medications, I need to understand your symptoms better. Could you describe what you're experiencing? Also, do you have any known allergies or are you currently taking any other medications?"
    
    # Default response
    if conversation_state.current_stage == ConversationStage.GREETING:
        return "I'm Dr. Maya from Wellness Care Center. Could you please tell me your name so we can get started?"
    elif conversation_state.current_stage == ConversationStage.COLLECTING_NAME:
        return "Could you please tell me your name?"
    elif conversation_state.current_stage == ConversationStage.COLLECTING_AGE:
        return f"Thank you. Could you please tell me your age, {conversation_state.patient_info['name']}?"
    elif conversation_state.current_stage == ConversationStage.COLLECTING_CONTACT:
        return f"Could you please provide a phone number or email where we can reach you, {conversation_state.patient_info['name']}?"
    elif conversation_state.current_stage == ConversationStage.COLLECTING_SYMPTOMS:
        return f"What symptoms are you experiencing today, {conversation_state.patient_info['name']}?"
    else:
        return f"I'm here to help with your health concerns. Could you tell me more about your symptoms? The more details you provide, the better I can assist you."

def book_appointment(user_input):
    """Simulate booking a medical appointment with hospital feel"""
    # Extract potential date and time from user input
    date_match = re.search(r'(today|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday)', user_input, re.IGNORECASE)
    time_match = re.search(r'(\d{1,2})(?::(\d{2}))?\s*(am|pm)?', user_input, re.IGNORECASE)
    
    date = date_match.group(1) if date_match else "tomorrow"
    
    if time_match:
        hour = time_match.group(1)
        minute = time_match.group(2) if time_match.group(2) else "00"
        period = time_match.group(3) if time_match.group(3) else "am"
        appointment_time = f"{hour}:{minute} {period}"
    else:
        # Generate random time between 9 AM and 5 PM
        hour = random.randint(9, 16)
        minute = random.choice(["00", "15", "30", "45"])
        appointment_time = f"{hour}:{minute} {'am' if hour < 12 else 'pm'}"
    
    # Determine appropriate doctor based on symptoms or previous conversation
    condition = None
    for symptom in conversation_state.patient_info["symptoms"]:
        for cond, info in medical_conditions.items():
            if any(s in symptom.lower() for s in info["symptoms"]):
                condition = cond
                break
        if condition:
            break
    
    # Select appropriate doctor specialty based on condition
    if condition and condition in medical_specialties:
        specialty = medical_specialties[condition][0]
        doctor_title = "Dr."
        doctor_last_names = ["Smith", "Johnson", "Patel", "Williams", "Garcia", "Chen", "Thompson", "Rodriguez", "Khan"]
        doctor_name = f"{doctor_title} {random.choice(doctor_last_names)}"
    else:
        specialty = "Primary Care"
        doctor_name = f"Dr. {random.choice(['Smith', 'Johnson', 'Patel', 'Williams'])}"
    
    # Generate confirmation details
    confirmation_number = f"MED-{random.randint(10000, 99999)}"
    
    # Format date better for readability
    formatted_date = date
    if date.lower() == "today":
        formatted_date = datetime.datetime.now().strftime("%A, %B %d")
    elif date.lower() == "tomorrow":
        formatted_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A, %B %d")
    
    appointment_details = {
        "date": formatted_date,
        "time": appointment_time,
        "doctor": doctor_name,
        "specialty": specialty,
        "confirmation": confirmation_number,
        "location": f"{hospital_name}, Medical Building B, Suite 204",
        "instructions": "Please arrive 15 minutes before your appointment time to complete any necessary paperwork. Bring your insurance card and photo ID."
    }
    
    # Store appointment in patient info
    conversation_state.patient_info["appointment"] = appointment_details
    
    # Flag that we need to generate a PDF
    conversation_state.needs_pdf = True
    
    # Update conversation stage
    conversation_state.update_stage(ConversationStage.CONFIRMING_APPOINTMENT)
    
    # Format response with more hospital-like language
    greeting = "Mr./Ms." if not conversation_state.patient_info["name"] else conversation_state.patient_info["name"]
    
    response = f"Perfect! I've scheduled an appointment for you with {doctor_name}, our {specialty} specialist, on {formatted_date} at {appointment_time}. "
    response += f"Your confirmation number is {confirmation_number}. The appointment will be at {hospital_name}, Medical Building B, Suite 204.\n\n"
    response += f"Please arrive 15 minutes early to complete your registration. Remember to bring your insurance card and a valid photo ID. "
    
    if specialty != "Primary Care":
        response += f"Since you'll be seeing our {specialty} specialist, it may be helpful to write down your symptoms beforehand. "
    
    response += f"I'll generate a PDF confirmation of your appointment details that you can download. Do you have any questions about your upcoming visit, {greeting}?"
    
    return response, appointment_details

def process_user_input(user_input):
    """Process user input and generate appropriate response"""
    if not user_input:
        return "I didn't quite catch that. Could you please speak again?"
    
    # First check for exit command
    if any(word in user_input.lower() for word in ["exit", "quit", "bye", "goodbye"]):
        if conversation_state.patient_info["name"]:
            return f"Thank you for reaching out to {hospital_name} today, {conversation_state.patient_info['name']}. Your health is our priority, and we're here for you 24/7. Take care and stay healthy! Goodbye!"
        else:
            return f"Thank you for reaching out to {hospital_name} today. Your health is our priority, and we're here for you 24/7. Take care and stay healthy! Goodbye!"
    
    # Check for appointment booking intent
    if any(word in user_input.lower() for word in ["appointment", "book", "schedule", "doctor", "visit"]):
        # If we have enough information, book the appointment
        if (conversation_state.patient_info["name"] and 
            conversation_state.patient_info["age"] and 
            (conversation_state.patient_info["contact"] or conversation_state.patient_info["email"])):
            
            appointment_response, appointment_details = book_appointment(user_input)
            conversation_state.add_to_history("assistant", appointment_response)
            return appointment_response
    
    # For general conversation, use Groq if available
    groq_response = get_groq_response(user_input)
    return groq_response

def main():
    """Main function to run the medical assistant"""
    greeting = random.choice(greetings)
    speak(greeting)
    
    while True:
        user_input = listen()
        if not user_input:
            continue
            
        response = process_user_input(user_input)
        speak(response)
        
        # Exit condition
        if any(word in user_input.lower() for word in ["exit", "quit", "bye", "goodbye"]):
            break
        
        # Small pause between interactions
        time.sleep(1)

if __name__ == "__main__":
    main() 