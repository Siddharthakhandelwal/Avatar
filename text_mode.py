import random
import re
import os
import json
import datetime
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv
import openai

# Load environment variables if available
try:
    load_dotenv()
except:
    pass

# Assistant personality settings
assistant_name = "Dr. Maya"
hospital_name = "Wellness Care Center"
current_date = datetime.now().strftime("%A, %B %d")

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

# Free model API configuration
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY', 'hf_dummy_key')}"}

# Dictionary to store conversation context
conversation_history = []
patient_info = {
    "name": "",
    "age": "",
    "symptoms_started": "",
    "last_visit": "",
    "has_appointment": False
}

# Greeting templates for more natural conversation
greetings = [
    f"Hello, I'm {assistant_name} from {hospital_name}. How are you feeling today?",
    f"Good day, this is {assistant_name}, your virtual healthcare assistant. What brings you in today?",
    f"Welcome to {hospital_name}'s virtual care. I'm {assistant_name}, how can I assist with your health concerns today?",
    f"Hi there, I'm {assistant_name}, your medical assistant. How may I help you with your health today?"
]

def get_time_of_day_greeting():
    """Return a time-appropriate greeting"""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def get_model_response(prompt):
    """Get response from free Hugging Face model"""
    try:
        # Attempt to use the model API
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers=headers, json=payload)
        
        # If successful, return the generated text
        if response.status_code == 200:
            return response.json()[0]["generated_text"]
        
        # Fallback for demonstration purposes
        print("[Using medical response generation since API might not be available]")
        return generate_medical_response(prompt)
    
    except Exception as e:
        print(f"[Error accessing model API: {e}]")
        return generate_medical_response(prompt)

def generate_medical_response(prompt):
    """Generate a medical-style response when the API is unavailable"""
    prompt_lower = prompt.lower()
    
    # Extract patient name if provided
    name_match = re.search(r"my name is (\w+)", prompt_lower)
    if name_match and not patient_info["name"]:
        patient_info["name"] = name_match.group(1).capitalize()
        time_greeting = get_time_of_day_greeting()
        return f"{time_greeting}, {patient_info['name']}. It's nice to meet you. How can I assist with your health concerns today?"
    
    # Check for greeting patterns and personalize if name is known
    if any(word in prompt_lower for word in ["hello", "hi", "hey", "greetings"]):
        time_greeting = get_time_of_day_greeting()
        if patient_info["name"]:
            return f"{time_greeting}, {patient_info['name']}. How are you feeling today? Is there anything specific I can help you with?"
        else:
            return f"{time_greeting}! I'm {assistant_name}, your medical assistant at {hospital_name}. How may I help you today?"
    
    # Check for well-being inquiries
    if "how are you" in prompt_lower:
        return f"I'm doing well, thank you for asking. More importantly, I'm here to focus on your health. How are you feeling today?"
    
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
        if patient_info["name"]:
            return f"I'd be happy to help you schedule an appointment, {patient_info['name']}. Could you please let me know what day and time would work best for you?"
        else:
            return f"I'd be happy to help you schedule an appointment. Could you please tell me your name and what day and time would work best for you?"
    
    # Check for medicine-related keywords
    if any(word in prompt_lower for word in ["medicine", "medication", "drug", "pill"]):
        return "Before I can recommend any medications, I need to understand your symptoms better. Could you describe what you're experiencing? Also, do you have any known allergies or are you currently taking any other medications?"
    
    # Check for gratitude
    if any(word in prompt_lower for word in ["thanks", "thank you", "appreciate"]):
        if patient_info["name"]:
            return f"You're very welcome, {patient_info['name']}. Your health is our priority at {hospital_name}. Is there anything else I can assist you with today?"
        else:
            return f"You're very welcome. Your health is our priority at {hospital_name}. Is there anything else I can assist you with today?"
    
    # Default response
    return f"I'm here to help with your health concerns. Could you tell me more about your symptoms? The more details you provide, the better I can assist you."

def diagnose_condition(user_input):
    """Analyze user input to determine potential medical conditions"""
    potential_conditions = []
    symptoms_mentioned = []
    
    for condition, info in medical_conditions.items():
        # Check if condition name or symptoms are mentioned
        condition_match = condition in user_input
        symptom_matches = [symptom for symptom in info["symptoms"] if symptom in user_input]
        
        if condition_match or symptom_matches:
            potential_conditions.append(condition)
            symptoms_mentioned.extend(symptom_matches)
    
    if potential_conditions:
        # If multiple conditions match, prioritize the one with more symptom matches
        if len(potential_conditions) > 1:
            condition_symptom_counts = {}
            for cond in potential_conditions:
                condition_symptom_counts[cond] = sum(1 for symptom in medical_conditions[cond]["symptoms"] if symptom in user_input)
            return max(condition_symptom_counts, key=condition_symptom_counts.get)
        return potential_conditions[0]
    else:
        return None

def suggest_medication(condition):
    """Suggest medication based on diagnosed condition with medical details"""
    if condition in medication_database:
        medications = medication_database[condition]
        response = f"Based on your symptoms of {condition}, here are some common over-the-counter medications that might help:"
        
        for med in medications[:2]:  # Limit to 2 medications for brevity
            response += f"\n\n• {med['name']}: {med['dosage']}. {med['note']}"
        
        response += "\n\nHowever, I strongly recommend consulting with a healthcare professional before starting any medication, especially if you have existing medical conditions or are taking other medications."
        
        if patient_info["name"]:
            response += f" {patient_info['name']}, would you like me to schedule a consultation for you with one of our physicians?"
        else:
            response += " Would you like me to schedule a consultation for you with one of our physicians?"
        
        return response
    else:
        return "I'd need more specific information about your symptoms to suggest appropriate medication. It's best to consult with a healthcare professional for a proper diagnosis and treatment plan. Can I help schedule an appointment for you?"

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
    for msg in conversation_history[-5:]:
        if msg.get("role") == "assistant":
            for cond in medical_conditions:
                if cond in msg.get("content", "").lower():
                    condition = cond
                    break
    
    if not condition:
        for cond, info in medical_conditions.items():
            if any(symptom in user_input.lower() for symptom in info["symptoms"]):
                condition = cond
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
    
    # Set the patient as having an appointment
    patient_info["has_appointment"] = True
    
    # Format response with more hospital-like language
    greeting = "Mr./Ms." if not patient_info["name"] else patient_info["name"]
    
    response = f"Perfect! I've scheduled an appointment for you with {doctor_name}, our {specialty} specialist, on {formatted_date} at {appointment_time}. "
    response += f"Your confirmation number is {confirmation_number}. The appointment will be at {hospital_name}, Medical Building B, Suite 204.\n\n"
    response += f"Please arrive 15 minutes early to complete your registration. Remember to bring your insurance card and a valid photo ID. "
    
    if specialty != "Primary Care":
        response += f"Since you'll be seeing our {specialty} specialist, it may be helpful to write down your symptoms beforehand. "
    
    response += f"Would you like me to send a reminder to your phone on the day of your appointment? Also, do you have any questions about your upcoming visit, {greeting}?"
    
    return response, appointment_details

def process_user_input(user_input):
    """Process user input and generate appropriate response"""
    if not user_input:
        return "I didn't understand that. Could you please try again?"
    
    user_input = user_input.lower()
    
    # Add to conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # Check for exit command
    if any(word in user_input for word in ["exit", "quit", "bye", "goodbye"]):
        if patient_info["name"]:
            return f"Thank you for reaching out to {hospital_name} today, {patient_info['name']}. Your health is our priority, and we're here for you 24/7. Take care and stay healthy! Goodbye!"
        else:
            return f"Thank you for reaching out to {hospital_name} today. Your health is our priority, and we're here for you 24/7. Take care and stay healthy! Goodbye!"
    
    # Check for appointment booking intent
    if any(word in user_input for word in ["appointment", "book", "schedule", "doctor", "visit"]):
        appointment_response, _ = book_appointment(user_input)
        conversation_history.append({"role": "assistant", "content": appointment_response})
        return appointment_response
    
    # Check for symptom description and medical advice
    condition = diagnose_condition(user_input)
    if condition:
        if any(word in user_input for word in ["medicine", "medication", "drug", "remedy", "treatment"]):
            medication_advice = suggest_medication(condition)
            conversation_history.append({"role": "assistant", "content": medication_advice})
            return medication_advice
        else:
            condition_info = medical_conditions[condition]
            doctor_type = medical_specialties[condition][0]
            response = f"I understand you're experiencing symptoms of {condition}. "
            
            if patient_info["name"]:
                response += f"{patient_info['name']}, "
            
            response += f"Based on what you've described, this could be due to {', '.join(condition_info['possible_causes'][0:2])}. "
            response += f"I recommend {', '.join(condition_info['suggested_remedies'][0:3])}. "
            response += f"{condition_info['follow_up']} "
            response += f"Would you like me to suggest some medications for your {condition}, or would you prefer to schedule an appointment with our {doctor_type}?"
            
            conversation_history.append({"role": "assistant", "content": response})
            return response
    
    # Check for personal information
    name_match = re.search(r"my name is (\w+)", user_input)
    if name_match and not patient_info["name"]:
        patient_info["name"] = name_match.group(1).capitalize()
        response = f"Thank you, {patient_info['name']}. It's nice to meet you. How can I assist with your health concerns today?"
        conversation_history.append({"role": "assistant", "content": response})
        return response
    
    # Get response from model/fallback
    full_context = " ".join([item["content"] for item in conversation_history[-3:] if "content" in item])
    model_response = get_model_response(full_context)
    conversation_history.append({"role": "assistant", "content": model_response})
    return model_response

def text_mode():
    """Text-only interface for the medical assistant"""
    patient_info = {
        "name": None,
        "age": None,
        "gender": None,
        "symptoms": [],
        "medical_history": None
    }
    
    conversation_state = {
        "greeting_done": False,
        "collecting_info": False,
        "info_collected": False,
        "providing_medical_advice": False,
        "booking_appointment": False,
        "conversation_ended": False
    }
    
    # Assistant personality and medical knowledge
    assistant_persona = """
    You are Dr. Maya, an AI medical assistant designed to help patients with preliminary medical questions
    and schedule appointments with real doctors when necessary. You are professional, compassionate, and 
    informative. You always maintain a calm and reassuring demeanor.
    
    Your capabilities include:
    1. Collecting basic patient information
    2. Providing general medical information
    3. Offering preliminary assessments of common symptoms
    4. Scheduling appointments with specialists
    5. Providing lifestyle and wellness advice
    
    You must always clarify that you are an AI assistant and not a replacement for professional medical care.
    For serious or emergency conditions, you will immediately advise patients to seek emergency medical attention.
    """
    
    print("Dr. Maya: Hello, I'm Dr. Maya, your AI medical assistant. How can I help you today?")
    conversation_state["greeting_done"] = True
    
    while not conversation_state["conversation_ended"]:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            print("Dr. Maya: Thank you for consulting with me. Take care and stay healthy!")
            conversation_state["conversation_ended"] = True
            continue
        
        # Prepare conversation history
        messages = [{"role": "system", "content": assistant_persona}]
        
        # Add patient information context if we have it
        if patient_info["name"]:
            patient_context = f"Current patient information: Name: {patient_info['name']}"
            if patient_info["age"]:
                patient_context += f", Age: {patient_info['age']}"
            if patient_info["gender"]:
                patient_context += f", Gender: {patient_info['gender']}"
            if patient_info["symptoms"]:
                patient_context += f", Reported symptoms: {', '.join(patient_info['symptoms'])}"
            if patient_info["medical_history"]:
                patient_context += f", Medical history: {patient_info['medical_history']}"
            
            messages.append({"role": "system", "content": patient_context})
        
        # Add conversation state
        state_context = "Conversation state: "
        for state, value in conversation_state.items():
            if value:
                state_context += state.replace("_", " ").title() + ", "
        
        messages.append({"role": "system", "content": state_context})
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=300
            )
            
            assistant_response = response.choices[0].message.content
            print(f"Dr. Maya: {assistant_response}")
            
            # Check for conversation state transitions based on the content
            if not conversation_state["collecting_info"] and "May I ask your name" in assistant_response:
                conversation_state["collecting_info"] = True
            
            if conversation_state["collecting_info"] and not conversation_state["info_collected"]:
                # Try to extract patient information
                if patient_info["name"] is None and "my name is" in user_input.lower():
                    name_parts = user_input.lower().split("my name is")
                    if len(name_parts) > 1:
                        patient_info["name"] = name_parts[1].strip().title()
                
                if patient_info["age"] is None and "years old" in user_input.lower():
                    for word in user_input.split():
                        if word.isdigit() and 1 <= int(word) <= 120:
                            patient_info["age"] = int(word)
                            break
                
                if patient_info["gender"] is None:
                    if "male" in user_input.lower():
                        patient_info["gender"] = "Male"
                    elif "female" in user_input.lower():
                        patient_info["gender"] = "Female"
                
                # Check if we have collected basic info
                if patient_info["name"] and patient_info["age"]:
                    conversation_state["info_collected"] = True
            
            if "appointment" in user_input.lower() or "schedule" in user_input.lower():
                conversation_state["booking_appointment"] = True
            
            if conversation_state["booking_appointment"] and "scheduled" in assistant_response.lower():
                print("\nAppointment details:")
                print("-------------------")
                tomorrow = datetime.now() + timedelta(days=1)
                print(f"Date: {tomorrow.strftime('%A, %B %d, %Y')}")
                print("Time: 2:00 PM")
                print("Doctor: Dr. Sarah Johnson")
                print("Location: Medical Center, 123 Health Ave")
                print("Please arrive 15 minutes early to complete paperwork.")
                print("-------------------")
        
        except Exception as e:
            print(f"Dr. Maya: I apologize, but I'm having trouble processing that request. {str(e)}")

if __name__ == "__main__":
    text_mode() 