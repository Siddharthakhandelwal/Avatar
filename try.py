import os
import time
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
import groq


# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SERVICE_REGION = os.getenv("AZURE_SPEECH_REGION")
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"




def speak(text):
        """Convert text to speech using Azure"""
        print(f"Dr. Maya: {text}")
        try:
            result = speech_synthesizer.speak_text_async(text).get()
            if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
                print("Speech synthesis failed")
        except Exception as e:
            print(f"Speech synthesis error: {e}")

def listen():
        """Listen to user's voice input using Azure"""
        print("Listening... Speak now!")
        try:
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
def chat(History):
    client = groq.Client(
                api_key=GROQ_API_KEY
            )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=History,
        max_tokens=200,
        temperature=0.7
    )
    
    assistant_response = response.choices[0].message.content
    print(f"\nGroq Response: {assistant_response}") 
    return assistant_response
    
def appointment(History):
    History.append({"role":"user","content":"I am giving you the whole chat summarize the conversation and give me the summary of the conversation. If user booked a appontment then give details of it."})
    summary=chat(History)
    return summary


def main():
    History = [{"role":"system","content":"You are a medical assistant. You are helpful and friendly. You are also a bit sassy.if user asks about your name, you should say 'Maya'.if user asks about your age, you should say some age randomly but practical.Act more like a human assistant.You can also make jokes and be more engaging.If user asks some random question or not related to medical, you should say 'I'm sorry, I can't answer that. I'm here to help with medical questions.'.You can book appointments with doctors take name in random for now and thier designation as well.You can also ask for their name and other details and then book the appointment.You can also ask for their address and then book the appointment.You can also ask for their phone number and then book the appointment.You can also ask for their email and then book the appointment.You can also ask for their insurance and then book the appointment.You can also ask for their medical history and then book the appointment.Ask questions to user to get more information about their problem.Ask question one by one and wait for user to answer before asking next question."}]
    speak("Hello, how can I help you today?")
    History.append({"role":"assistant","content":"Hello, how can I help you today? \n"})
    user_input = listen()
    while "thanks" or "thank you" not in user_input.lower():
        History.append({"role":"user","content":user_input})
        response = chat(History)
        speak(response)
        History.append({"role":"assistant","content":response})
        user_input = listen()
    print(speak("Thank you for using Medycall. Have a great day!"))
    summary=appointment(History)
    print(summary+"\n")
    print(History)


while True:
    user_input = listen()
    if "hey" or "medycall" or "assistant" or "medical" in user_input.lower():
        main()
        break
        
        
