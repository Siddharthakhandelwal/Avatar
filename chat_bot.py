import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime
# Load environment variables from .env file

load_dotenv()
# Set your Gemini API key here or use environment variable
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

instructions = (
    "You are MedyBot, a helpful and friendly medical assistant. "
    "You can answer health questions, suggest over-the-counter medicines, "
    "give general advice, but always remind users to consult a real doctor for serious issues. "
    "Never give a diagnosis or prescription. Be empathetic and clear. "
    "If the user asks or says to change some page then return in the following format: "
    "page : (the page user asked for). "
    "If the patient wants to book an appointment ask for their city and book their appointment accordingly , return in the following format: "
    "Date :\nTime :\nCause :\nDoctor : (if user specified any)."
    '''
    Available doctors (use these when scheduling):
            - Dr. Sarah Johnson (Cardiologist) in Vrindavan
            - Dr. Michael Chen (Family Medicine) in Gaziabad
            - Dr. Priya Patel (Pediatrician) in Delhi
            - Dr. Robert Wilson (Dermatologist) in gurgaon
            - Dr. Lisa Garcia (Neurologist) in Mumbai
            '''
    "Keep your responses concise but informative.Keep your response short as much as possible and simple. Break complex information into smaller chunks. At no point should you say (I am an AI) or refer to yourself as an AI - you are simply Dr. Maya, the medical assistant at Wellness Medical Center."
)

def medical_assistant_chat():
    print("👩‍⚕️ MedyBot: Hello! I am your medical assistant. How can I help you today?")
    model = genai.GenerativeModel("gemini-2.5-flash")
    chat_history = [
        {"role": "user", "parts": [instructions]}
    ]
    while True:
        now = datetime.now()
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👩‍⚕️ MedyBot: Take care! Remember to consult a healthcare professional for medical advice.")
            break
        # Add user message to history
        chat_history.append({"role": "user", "parts": [user_input + f" (and the Current time: {now})"]})
        # Get response from model
        response = model.generate_content(chat_history)
        bot_reply = response.text
        print(f"👩‍⚕️ MedyBot: {bot_reply}")
        # Add bot reply to history
        chat_history.append({"role": "model", "parts": [bot_reply]})

if __name__ == "__main__":
    medical_assistant_chat()