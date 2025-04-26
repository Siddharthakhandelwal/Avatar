#!/usr/bin/env python3
"""
Minimal Medical AI Assistant Test
This script provides a bare-bones version of the medical assistant for testing.
It doesn't require any external dependencies beyond the Python standard library.
"""

import random
import re

# Medical knowledge base (simplified)
medical_conditions = {
    "headache": {
        "symptoms": ["pain in head", "throbbing", "pressure"],
        "possible_causes": ["stress", "dehydration", "lack of sleep", "eyestrain"],
        "suggested_remedies": ["rest", "hydration", "over-the-counter pain relievers"],
        "severity": "low to medium"
    },
    "common cold": {
        "symptoms": ["runny nose", "cough", "sore throat", "sneezing", "congestion"],
        "possible_causes": ["viral infection", "weather changes"],
        "suggested_remedies": ["rest", "fluids", "over-the-counter cold medicine"],
        "severity": "low"
    },
    "fever": {
        "symptoms": ["elevated temperature", "chills", "sweating", "body aches"],
        "possible_causes": ["infection", "inflammation", "heat exhaustion"],
        "suggested_remedies": ["rest", "fluids", "fever reducers like acetaminophen"],
        "severity": "medium"
    },
    "stomachache": {
        "symptoms": ["abdominal pain", "nausea", "bloating"],
        "possible_causes": ["indigestion", "food poisoning", "gas", "stomach virus"],
        "suggested_remedies": ["light diet", "ginger tea", "probiotics"],
        "severity": "low to medium"
    }
}

# Drugs database (simplified, for demonstration only)
medication_database = {
    "headache": ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)", "Aspirin"],
    "common cold": ["Pseudoephedrine", "Dextromethorphan", "Chlorpheniramine"],
    "fever": ["Acetaminophen (Tylenol)", "Ibuprofen (Advil)"],
    "stomachache": ["Bismuth subsalicylate (Pepto-Bismol)", "Loperamide (Imodium)"]
}

# Dictionary to store conversation context
conversation_history = []

def generate_response(prompt):
    """Generate a response based on user input"""
    prompt_lower = prompt.lower()
    
    # Check for greeting patterns
    if any(word in prompt_lower for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! I'm your medical assistant. How are you feeling today?"
    
    # Check for medical condition keywords
    for condition, info in medical_conditions.items():
        if condition in prompt_lower or any(symptom in prompt_lower for symptom in info["symptoms"]):
            return f"It sounds like you might have {condition}. Common causes include {', '.join(info['possible_causes'])}. I recommend {', '.join(info['suggested_remedies'])}."
    
    # Check for appointment-related keywords
    if any(word in prompt_lower for word in ["appointment", "book", "schedule", "doctor"]):
        return "I can help you book an appointment. Could you please tell me what day and time would work for you?"
    
    # Check for medicine-related keywords
    if any(word in prompt_lower for word in ["medicine", "medication", "drug", "pill"]):
        return "Before suggesting any medication, I need to understand your symptoms better. Could you describe how you're feeling?"
    
    # Default response
    return "I'm here to help with your medical concerns. Could you tell me more about your symptoms?"

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
        return f"Based on your symptoms of {condition}, common over-the-counter medications include {', '.join(medications)}. However, please consult with a healthcare professional before taking any medication."
    else:
        return "I'd need more information about your symptoms to suggest appropriate medication. Please consult with a healthcare professional for personalized advice."

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
    doctor = random.choice(["Dr. Smith", "Dr. Johnson", "Dr. Patel", "Dr. Williams"])
    confirmation_number = f"MED-{random.randint(10000, 99999)}"
    
    # Format response
    response = f"Great! I've booked an appointment for you on {date} at {appointment_time} with {doctor}. Your confirmation number is {confirmation_number}. The appointment is at Medical Center, 123 Health Street. Would you like a reminder for this appointment?"
    
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
        return "Thank you for using the medical assistant. Take care and stay healthy! Goodbye!"
    
    # Check for appointment booking intent
    if any(word in user_input for word in ["appointment", "book", "schedule", "doctor", "visit"]):
        appointment_response = book_appointment(user_input)
        conversation_history.append({"role": "assistant", "content": appointment_response})
        return appointment_response
    
    # Check for symptom description and medical advice
    condition = diagnose_condition(user_input)
    if condition:
        if any(word in user_input for word in ["medicine", "medication", "drug", "remedy"]):
            medication_advice = suggest_medication(condition)
            conversation_history.append({"role": "assistant", "content": medication_advice})
            return medication_advice
        else:
            condition_info = medical_conditions[condition]
            response = f"Based on what you've told me, you might be experiencing {condition}. Common causes include {', '.join(condition_info['possible_causes'])}. I suggest {', '.join(condition_info['suggested_remedies'])}. Would you like me to suggest some medications or book a doctor's appointment?"
            conversation_history.append({"role": "assistant", "content": response})
            return response
    
    # Get response from fallback
    response = generate_response(user_input)
    conversation_history.append({"role": "assistant", "content": response})
    return response

def main():
    """Main function to run the minimal test assistant"""
    print("=" * 80)
    print("Medical AI Assistant (Minimal Test Version)")
    print("=" * 80)
    print("Hello! I'm your medical AI assistant. I can help diagnose your symptoms,")
    print("suggest remedies, and book doctor appointments. How are you feeling today?")
    print("(Type 'exit' to quit)")
    print("-" * 80)
    
    while True:
        user_input = input("You: ")
        if not user_input:
            continue
            
        response = process_user_input(user_input)
        print(f"Assistant: {response}")
        
        # Exit condition
        if any(word in user_input.lower() for word in ["exit", "quit", "bye", "goodbye"]):
            break

if __name__ == "__main__":
    main() 