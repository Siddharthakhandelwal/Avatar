"""
Conversation flow management and PDF generation for the medical assistant.
This module handles structured conversation and PDF appointment summary creation.
"""

import os
import re
import random
import datetime
from fpdf import FPDF
from enum import Enum

class ConversationStage(Enum):
    """Enum representing different stages in the conversation flow"""
    GREETING = 0
    COLLECTING_NAME = 1
    COLLECTING_AGE = 2
    COLLECTING_CONTACT = 3
    COLLECTING_SYMPTOMS = 4
    ASKING_SYMPTOM_DURATION = 5
    DIAGNOSING = 6
    SUGGESTING_REMEDIES = 7
    ASKING_APPOINTMENT = 8
    BOOKING_APPOINTMENT = 9
    CONFIRMING_APPOINTMENT = 10
    FAREWELL = 11
    GENERAL_CHAT = 12

class ConversationState:
    """Class to track the state of the conversation"""
    def __init__(self):
        self.current_stage = ConversationStage.GREETING
        self.patient_info = {
            "name": "",
            "age": "",
            "contact": "",
            "email": "",
            "address": "",
            "symptoms": [],
            "symptom_duration": "",
            "allergies": [],
            "current_medications": [],
            "medical_history": [],
            "appointment": None,
            "appointment_file": ""
        }
        self.identified_condition = None
        self.suggested_specialty = None
        self.conversation_history = []
        self.needs_pdf = False

    def update_stage(self, new_stage):
        """Update the current conversation stage"""
        self.current_stage = new_stage
        
    def add_to_history(self, role, content):
        """Add a message to the conversation history"""
        self.conversation_history.append({"role": role, "content": content})

def extract_patient_info(user_input, state):
    """Extract patient information from user input"""
    user_input_lower = user_input.lower()
    
    # Extract name
    if state.current_stage == ConversationStage.COLLECTING_NAME or not state.patient_info["name"]:
        name_match = re.search(r"my name is (\w+(?:\s\w+)?)|i(?:'|a)m (\w+(?:\s\w+)?)", user_input_lower)
        if name_match:
            name = name_match.group(1) if name_match.group(1) else name_match.group(2)
            state.patient_info["name"] = name.title()
            return True
    
    # Extract age
    if state.current_stage == ConversationStage.COLLECTING_AGE or not state.patient_info["age"]:
        age_match = re.search(r"i(?:'|a)m (\d+)(?:\s+years? old)?|(\d+)(?:\s+years? old)", user_input_lower)
        if age_match:
            age = age_match.group(1) if age_match.group(1) else age_match.group(2)
            state.patient_info["age"] = age
            return True
    
    # Extract contact information
    if state.current_stage == ConversationStage.COLLECTING_CONTACT or not state.patient_info["contact"]:
        # Phone number patterns
        phone_match = re.search(r"(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})", user_input)
        if phone_match:
            state.patient_info["contact"] = phone_match.group(1)
            return True
        
        # Email patterns
        email_match = re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", user_input)
        if email_match:
            state.patient_info["email"] = email_match.group(1)
            return True
    
    # Extract symptoms
    if state.current_stage == ConversationStage.COLLECTING_SYMPTOMS:
        symptoms = []
        symptom_keywords = ["pain", "ache", "sore", "hurt", "fever", "cough", "sneeze", 
                            "tired", "fatigue", "dizzy", "nausea", "vomit", "headache", 
                            "rash", "swelling", "breathing", "throat", "stomach", "back"]
        
        for keyword in symptom_keywords:
            if keyword in user_input_lower:
                # Try to get the full symptom phrase
                for i in range(3):  # Look for phrases up to 3 words before/after
                    pattern = r"\b(\w+\s+){{0,{0}}}{1}(\s+\w+){{0,{0}}}\b".format(i, keyword)
                    symptom_match = re.search(pattern, user_input_lower)
                    if symptom_match and symptom_match.group(0) not in symptoms:
                        symptoms.append(symptom_match.group(0))
                
        if symptoms:
            state.patient_info["symptoms"].extend(symptoms)
            return True
    
    # Extract symptom duration
    if state.current_stage == ConversationStage.ASKING_SYMPTOM_DURATION:
        duration_patterns = [
            (r"(\d+)\s+days?", "days"),
            (r"(\d+)\s+weeks?", "weeks"),
            (r"(\d+)\s+months?", "months"),
            (r"a\s+day", "1 day"),
            (r"a\s+week", "1 week"),
            (r"a\s+month", "1 month"),
            (r"since\s+yesterday", "1 day"),
            (r"since\s+last\s+week", "1 week")
        ]
        
        for pattern, unit in duration_patterns:
            duration_match = re.search(pattern, user_input_lower)
            if duration_match:
                if 'a' in pattern:
                    state.patient_info["symptom_duration"] = unit
                else:
                    state.patient_info["symptom_duration"] = f"{duration_match.group(1)} {unit}"
                return True
    
    return False

def generate_structured_prompt(state, user_input, assistant_name, hospital_name):
    """Generate structured prompt based on conversation stage"""
    current_date = datetime.datetime.now().strftime("%A, %B %d")
    
    # Base system prompt
    prompt = f"""You are {assistant_name}, an AI medical assistant designed to help patients with preliminary medical 
questions and schedule appointments with real doctors when necessary. You are professional, compassionate, and 
informative. You always maintain a calm and reassuring demeanor. Today is {current_date}.

Your capabilities include:
- Collecting basic patient information
- Providing general medical information
- Offering preliminary assessments of common symptoms
- Scheduling appointments with specialists
- Providing lifestyle and wellness advice

You must always clarify that you are an AI assistant and not a replacement for professional medical care.
For serious or emergency conditions, you will immediately advise patients to seek emergency medical attention.
"""

    # Replace Unicode bullet points with hyphen
    prompt = prompt.replace('\u2022', '-')
    
    # Add stage-specific instructions
    if state.current_stage == ConversationStage.GREETING:
        prompt += "\nYou are in the GREETING stage. Focus on welcoming the patient warmly and asking for their name."
    
    elif state.current_stage == ConversationStage.COLLECTING_NAME:
        prompt += "\nYou are in the COLLECTING_NAME stage. Ask for the patient's name if not provided yet."
    
    elif state.current_stage == ConversationStage.COLLECTING_AGE:
        prompt += "\nYou are in the COLLECTING_AGE stage. You already have the patient's name. Ask for their age."
    
    elif state.current_stage == ConversationStage.COLLECTING_CONTACT:
        prompt += "\nYou are in the COLLECTING_CONTACT stage. Ask for a phone number or email for contact purposes."
    
    elif state.current_stage == ConversationStage.COLLECTING_SYMPTOMS:
        prompt += "\nYou are in the COLLECTING_SYMPTOMS stage. Ask about the patient's symptoms and health concerns."
    
    elif state.current_stage == ConversationStage.PROVIDING_INFORMATION:
        prompt += "\nYou are in the PROVIDING_INFORMATION stage. Provide helpful medical information based on the symptoms described."
    
    elif state.current_stage == ConversationStage.BOOKING_APPOINTMENT:
        prompt += "\nYou are in the BOOKING_APPOINTMENT stage. Help the patient schedule an appointment with an appropriate specialist."
    
    elif state.current_stage == ConversationStage.CONFIRMING_APPOINTMENT:
        prompt += "\nYou are in the CONFIRMING_APPOINTMENT stage. Confirm appointment details and provide next steps."
    
    # Emergency keywords to watch for
    prompt += """
Watch for these emergency keywords: chest pain, difficulty breathing, severe bleeding, unconscious, stroke, heart attack, 
seizure, severe allergic reaction, anaphylaxis, poisoning, suicidal thoughts.
If any of these are mentioned, instruct the patient to call emergency services (911) immediately and do not continue 
with normal conversation flow.
"""
    
    # Generate patient context if we have information
    patient_context = None
    if state.patient_info["name"] or state.patient_info["age"] or state.patient_info["symptoms"]:
        patient_context = "Current patient information:"
        if state.patient_info["name"]:
            patient_context += f" Name: {state.patient_info['name']},"
        if state.patient_info["age"]:
            patient_context += f" Age: {state.patient_info['age']},"
        if state.patient_info["gender"]:
            patient_context += f" Gender: {state.patient_info['gender']},"
        if state.patient_info["contact"]:
            patient_context += f" Contact: {state.patient_info['contact']},"
        if state.patient_info["email"]:
            patient_context += f" Email: {state.patient_info['email']},"
        if state.patient_info["symptoms"]:
            patient_context += f" Reported symptoms: {', '.join(state.patient_info['symptoms'])},"
    
    return prompt, patient_context

def generate_appointment_pdf(appointment_details, patient_info, hospital_name):
    """Generate a PDF with appointment details"""
    pdf = FPDF()
    pdf.add_page()
    
    # Set up PDF
    pdf.set_font("Arial", "B", 16)
    pdf.cell(190, 10, f"{hospital_name}", 0, 1, "C")
    pdf.cell(190, 10, "Appointment Confirmation", 0, 1, "C")
    pdf.line(10, 30, 200, 30)
    
    # Add current date
    pdf.set_font("Arial", "", 10)
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    pdf.cell(190, 10, f"Generated on: {current_date}", 0, 1, "R")
    
    # Patient information
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 10, "Patient Information", 0, 1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(190, 10, f"Name: {patient_info['name']}", 0, 1)
    pdf.cell(190, 10, f"Age: {patient_info['age']}", 0, 1)
    
    if patient_info["contact"]:
        pdf.cell(190, 10, f"Contact: {patient_info['contact']}", 0, 1)
    if patient_info["email"]:
        pdf.cell(190, 10, f"Email: {patient_info['email']}", 0, 1)
    
    # Appointment details
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 10, "", 0, 1)  # Empty space
    pdf.cell(190, 10, "Appointment Details", 0, 1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(190, 10, f"Date: {appointment_details['date']}", 0, 1)
    pdf.cell(190, 10, f"Time: {appointment_details['time']}", 0, 1)
    pdf.cell(190, 10, f"Doctor: {appointment_details['doctor']}", 0, 1)
    pdf.cell(190, 10, f"Specialty: {appointment_details['specialty']}", 0, 1)
    pdf.cell(190, 10, f"Location: {appointment_details['location']}", 0, 1)
    pdf.cell(190, 10, f"Confirmation #: {appointment_details['confirmation']}", 0, 1)
    
    # Instructions
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 10, "", 0, 1)  # Empty space
    pdf.cell(190, 10, "Instructions", 0, 1)
    pdf.set_font("Arial", "", 12)
    for line in appointment_details['instructions'].split(". "):
        if line:
            pdf.cell(190, 10, f"• {line}.", 0, 1)
    
    # Reported symptoms if available
    if patient_info["symptoms"]:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(190, 10, "", 0, 1)  # Empty space
        pdf.cell(190, 10, "Reported Symptoms", 0, 1)
        pdf.set_font("Arial", "", 12)
        for symptom in patient_info["symptoms"]:
            pdf.cell(190, 10, f"• {symptom}", 0, 1)
        
        if patient_info["symptom_duration"]:
            pdf.cell(190, 10, f"Duration: {patient_info['symptom_duration']}", 0, 1)
    
    # Disclaimer
    pdf.set_font("Arial", "I", 10)
    pdf.cell(190, 10, "", 0, 1)  # Empty space
    pdf.multi_cell(190, 10, "Disclaimer: This is a simulated appointment confirmation. In a real medical setting, please verify all appointment details with your healthcare provider.")
    
    # Create directory if it doesn't exist
    os.makedirs("appointments", exist_ok=True)
    
    # Save the PDF
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"appointments/appointment_{patient_info['name'].replace(' ', '_')}_{timestamp}.pdf"
    pdf.output(filename)
    
    return filename 