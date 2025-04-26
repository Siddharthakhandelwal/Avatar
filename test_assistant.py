#!/usr/bin/env python3
"""
Minimal Medical AI Assistant Test
This script provides a bare-bones version of the medical assistant for testing.
It doesn't require any external dependencies beyond the Python standard library.
"""

import random
import re
import datetime

# Assistant personality settings
assistant_name = "Dr. Maya"
hospital_name = "Wellness Care Center"

# Medical knowledge base (simplified but with more human detail)
medical_conditions = {
    "headache": {
        "symptoms": ["pain in head", "throbbing", "pressure", "temple pain", "migraine"],
        "possible_causes": ["stress", "dehydration", "lack of sleep", "eyestrain", "tension"],
        "suggested_remedies": ["rest in a quiet room", "staying hydrated", "over-the-counter pain relievers"],
        "follow_up": "If your headache persists for more than 3 days, please consult with a doctor."
    },
    "common cold": {
        "symptoms": ["runny nose", "cough", "sore throat", "sneezing", "congestion"],
        "possible_causes": ["viral infection", "seasonal changes", "weakened immune system"],
        "suggested_remedies": ["plenty of rest", "fluids", "over-the-counter cold medicine"],
        "follow_up": "Most colds resolve within 7-10 days. If symptoms worsen, please contact your doctor."
    },
    "fever": {
        "symptoms": ["elevated temperature", "chills", "sweating", "body aches", "headache"],
        "possible_causes": ["infection", "inflammation", "immune response"],
        "suggested_remedies": ["rest", "hydration", "fever reducers like acetaminophen"],
        "follow_up": "For high fevers above 102°F or any fever lasting more than 3 days, please seek medical attention."
    },
    "stomachache": {
        "symptoms": ["abdominal pain", "nausea", "bloating", "cramping", "indigestion"],
        "possible_causes": ["indigestion", "food poisoning", "gas", "stomach virus"],
        "suggested_remedies": ["light, bland diet", "ginger tea", "small meals", "avoiding spicy foods"],
        "follow_up": "If you experience severe pain or symptoms lasting more than 2 days, please see a doctor."
    }
}

# Drugs database (simplified version with some medical details)
medication_database = {
    "headache": ["Acetaminophen (Tylenol): 325-650mg every 4-6 hours", "Ibuprofen (Advil): 200-400mg every 4-6 hours with food"],
    "common cold": ["Decongestants for nasal congestion", "Cough suppressants as needed", "Antihistamines for runny nose"],
    "fever": ["Acetaminophen (Tylenol): 325-650mg every 4-6 hours", "Ibuprofen (Advil): 200-400mg every 4-6 hours with food"],
    "stomachache": ["Bismuth subsalicylate (Pepto-Bismol)", "Antacids for heartburn", "Anti-gas medication if bloated"]
}

# Dictionary to store conversation context
conversation_history = []
patient_info = {"name": ""}

def get_time_of_day_greeting():
    """Return a time-appropriate greeting"""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def generate_response(prompt):
    """Generate a response based on user input with medical assistant personality"""
    prompt_lower = prompt.lower()
    
    # Extract name if provided
    name_match = re.search(r"my name is (\w+)", prompt_lower)
    if name_match and not patient_info["name"]:
        patient_info["name"] = name_match.group(1).capitalize()
        return f"Thank you, {patient_info['name']}. It's nice to meet you. I'm {assistant_name} from {hospital_name}. How can I assist with your health concerns today?"
    
    # Check for greeting patterns
    if any(word in prompt_lower for word in ["hello", "hi", "hey", "greetings"]):
        time_greeting = get_time_of_day_greeting()
        if patient_info["name"]:
            return f"{time_greeting}, {patient_info['name']}. How are you feeling today? Is there anything specific I can help you with?"
        else:
            return f"{time_greeting}! I'm {assistant_name}, your medical assistant at {hospital_name}. How may I help you today?"
    
    # Check for medical condition keywords
    for condition, info in medical_conditions.items():
        if condition in prompt_lower or any(symptom in prompt_lower for symptom in info["symptoms"]):
            response = f"Based on what you're describing, it sounds like you might be experiencing {condition}. This could be due to {', '.join(info['possible_causes'][0:2])}."
            response += f" I recommend {', '.join(info['suggested_remedies'][0:3])}. {info['follow_up']}"
            if patient_info["name"]:
                response = f"{patient_info['name']}, {response}"
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
    
    # Default response
    if patient_info["name"]:
        return f"{patient_info['name']}, I'm here to help with your health concerns. Could you tell me more about your symptoms?"
    else:
        return f"I'm here to help with your health concerns. Could you tell me more about your symptoms? The more details you provide, the better I can assist you."

def diagnose_condition(user_input):
    """Analyze user input to determine potential medical conditions"""
    potential_conditions = []
    
    for condition, info in medical_conditions.items():
        # Check if condition name or symptoms are mentioned
        if condition in user_input or any(symptom in user_input for symptom in info["symptoms"]):
            potential_conditions.append(condition)
    
    if potential_conditions:
        # Return the first matched condition for simplicity
        return potential_conditions[0]
    else:
        return None

def suggest_medication(condition):
    """Suggest medication based on diagnosed condition"""
    if condition in medication_database:
        medications = medication_database[condition]
        response = f"Based on your symptoms of {condition}, here are some medications that might help: {', '.join(medications)}."
        response += "\n\nHowever, I strongly recommend consulting with a healthcare professional before starting any medication, especially if you have existing medical conditions or are taking other medications."
        
        if patient_info["name"]:
            response = f"{patient_info['name']}, {response}"
            
        return response
    else:
        return "I'd need more specific information about your symptoms to suggest appropriate medication. It's best to consult with a healthcare professional for a proper diagnosis and treatment plan."

def book_appointment(user_input):
    """Simulate booking a medical appointment"""
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
    
    # Generate confirmation details
    doctor_name = f"Dr. {random.choice(['Smith', 'Johnson', 'Patel', 'Williams'])}"
    confirmation_number = f"MED-{random.randint(10000, 99999)}"
    
    # Format date better
    formatted_date = date
    if date.lower() == "today":
        formatted_date = datetime.datetime.now().strftime("%A, %B %d")
    elif date.lower() == "tomorrow":
        formatted_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A, %B %d")
    
    # Format response
    greeting = "Mr./Ms." if not patient_info["name"] else patient_info["name"]
    
    response = f"Perfect! I've scheduled an appointment for you with {doctor_name} on {formatted_date} at {appointment_time}. "
    response += f"Your confirmation number is {confirmation_number}. The appointment will be at {hospital_name}, Medical Building B, Suite 204.\n\n"
    response += f"Please arrive 15 minutes early to complete your registration. Remember to bring your insurance card and a valid photo ID."
    response += f" Do you have any questions about your upcoming visit, {greeting}?"
    
    return response

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
        appointment_response = book_appointment(user_input)
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
            response = f"I understand you're experiencing symptoms of {condition}. "
            
            if patient_info["name"]:
                response += f"{patient_info['name']}, "
            
            response += f"Based on what you've described, this could be due to {', '.join(condition_info['possible_causes'][0:2])}. "
            response += f"I recommend {', '.join(condition_info['suggested_remedies'])}. {condition_info['follow_up']} "
            response += f"Would you like me to suggest some medications for your {condition}, or would you prefer to schedule an appointment?"
            
            conversation_history.append({"role": "assistant", "content": response})
            return response
    
    # Check for personal information
    name_match = re.search(r"my name is (\w+)", user_input)
    if name_match and not patient_info["name"]:
        patient_info["name"] = name_match.group(1).capitalize()
        response = f"Thank you, {patient_info['name']}. It's nice to meet you. How can I assist with your health concerns today?"
        conversation_history.append({"role": "assistant", "content": response})
        return response
    
    # Get response from generate_response function
    response = generate_response(user_input)
    conversation_history.append({"role": "assistant", "content": response})
    return response

def main():
    """Main function to run the minimal test assistant"""
    print("=" * 80)
    print(f"{hospital_name} - Medical Assistant (Minimal Version)")
    print("=" * 80)
    greeting = f"Hello! I'm {assistant_name} from {hospital_name}. I can help diagnose your symptoms, suggest remedies, and book doctor appointments. How are you feeling today?"
    print(f"{assistant_name}: {greeting}")
    print("-" * 80)
    
    while True:
        user_input = input("You: ")
        if not user_input:
            continue
            
        response = process_user_input(user_input)
        print(f"{assistant_name}: {response}")
        
        # Exit condition
        if any(word in user_input.lower() for word in ["exit", "quit", "bye", "goodbye"]):
            break

if __name__ == "__main__":
    main() 