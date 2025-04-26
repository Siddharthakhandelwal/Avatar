import json
import os
from datetime import datetime, timedelta

class MedicationManager:
    """Module for managing patient medications and prescriptions"""
    
    def __init__(self):
        self.medications_file = "medications.json"
        self.medications_data = self._load_medications()
        self.common_medications = {
            "antibiotics": ["Amoxicillin", "Azithromycin", "Ciprofloxacin", "Doxycycline"],
            "pain_relievers": ["Acetaminophen", "Ibuprofen", "Naproxen", "Aspirin"],
            "anti_inflammatories": ["Prednisone", "Hydrocortisone", "Dexamethasone"],
            "antihistamines": ["Loratadine", "Cetirizine", "Diphenhydramine"],
            "antihypertensives": ["Lisinopril", "Amlodipine", "Losartan", "Metoprolol"],
            "diabetes_medications": ["Metformin", "Insulin", "Glipizide", "Sitagliptin"]
        }
    
    def _load_medications(self):
        """Load medications data from file"""
        try:
            if os.path.exists(self.medications_file):
                with open(self.medications_file, "r") as file:
                    return json.load(file)
            return {}
        except Exception as e:
            print(f"Error loading medications: {e}")
            return {}
    
    def _save_medications(self):
        """Save medications data to file"""
        try:
            with open(self.medications_file, "w") as file:
                json.dump(self.medications_data, file, indent=2)
        except Exception as e:
            print(f"Error saving medications: {e}")
    
    def add_medication(self, patient_id, medication_name, dosage, frequency, start_date, end_date=None, notes=""):
        """Add a new medication for a patient"""
        if patient_id not in self.medications_data:
            self.medications_data[patient_id] = []
        
        # Create medication record
        medication = {
            "medication_id": f"med_{len(self.medications_data[patient_id]) + 1}",
            "name": medication_name,
            "dosage": dosage,
            "frequency": frequency,
            "start_date": start_date,
            "end_date": end_date,
            "notes": notes,
            "active": True,
            "created_at": datetime.now().isoformat()
        }
        
        self.medications_data[patient_id].append(medication)
        self._save_medications()
        
        return medication["medication_id"]
    
    def update_medication(self, patient_id, medication_id, **kwargs):
        """Update an existing medication"""
        if patient_id not in self.medications_data:
            return False, "Patient not found"
        
        for i, med in enumerate(self.medications_data[patient_id]):
            if med["medication_id"] == medication_id:
                # Update fields that were provided
                for key, value in kwargs.items():
                    if key in med:
                        med[key] = value
                
                med["updated_at"] = datetime.now().isoformat()
                self.medications_data[patient_id][i] = med
                self._save_medications()
                
                return True, "Medication updated successfully"
        
        return False, "Medication not found"
    
    def get_patient_medications(self, patient_id, active_only=True):
        """Get all medications for a patient"""
        if patient_id not in self.medications_data:
            return []
        
        if active_only:
            return [med for med in self.medications_data[patient_id] if med["active"]]
        
        return self.medications_data[patient_id]
    
    def discontinue_medication(self, patient_id, medication_id, reason=""):
        """Discontinue a medication"""
        if patient_id not in self.medications_data:
            return False, "Patient not found"
        
        for i, med in enumerate(self.medications_data[patient_id]):
            if med["medication_id"] == medication_id:
                med["active"] = False
                med["end_date"] = datetime.now().isoformat()
                med["discontinuation_reason"] = reason
                med["updated_at"] = datetime.now().isoformat()
                
                self.medications_data[patient_id][i] = med
                self._save_medications()
                
                return True, "Medication discontinued"
        
        return False, "Medication not found"
    
    def check_drug_interactions(self, medications_list):
        """
        Basic drug interaction checker
        Note: This is a simplified version and should not be used for actual medical decisions
        """
        # Example interactions (simplified)
        interaction_pairs = [
            ("Warfarin", "Aspirin"),
            ("Lisinopril", "Potassium supplements"),
            ("Ciprofloxacin", "Calcium supplements"),
            ("Simvastatin", "Grapefruit juice"),
            ("Methotrexate", "Ibuprofen")
        ]
        
        interactions = []
        for i, med1 in enumerate(medications_list):
            for j in range(i+1, len(medications_list)):
                med2 = medications_list[j]
                
                # Check if this pair is in our known interaction pairs
                if (med1, med2) in interaction_pairs or (med2, med1) in interaction_pairs:
                    interactions.append(f"Potential interaction between {med1} and {med2}")
        
        return interactions
    
    def get_medication_info(self, medication_name):
        """
        Retrieve basic information about a medication
        Note: This is simplified and should not be used for actual medical information
        """
        # Basic medication information database (simplified)
        medication_info = {
            "Amoxicillin": {
                "class": "Antibiotic",
                "common_uses": "Bacterial infections",
                "side_effects": "Diarrhea, nausea, rash"
            },
            "Lisinopril": {
                "class": "ACE inhibitor",
                "common_uses": "High blood pressure, heart failure",
                "side_effects": "Dry cough, dizziness, headache"
            },
            "Metformin": {
                "class": "Biguanide",
                "common_uses": "Type 2 diabetes",
                "side_effects": "Nausea, diarrhea, abdominal pain"
            },
            "Ibuprofen": {
                "class": "NSAID",
                "common_uses": "Pain, inflammation, fever",
                "side_effects": "Stomach upset, heartburn, dizziness"
            }
        }
        
        return medication_info.get(medication_name, {"info": "Information not available"})
    
    def suggest_medications(self, condition):
        """Suggest common medications for a given condition"""
        condition_medications = {
            "hypertension": ["Lisinopril", "Amlodipine", "Losartan"],
            "diabetes": ["Metformin", "Insulin", "Glipizide"],
            "pain": ["Acetaminophen", "Ibuprofen", "Naproxen"],
            "infection": ["Amoxicillin", "Azithromycin", "Ciprofloxacin"],
            "allergies": ["Loratadine", "Cetirizine", "Diphenhydramine"],
            "anxiety": ["Sertraline", "Alprazolam", "Buspirone"],
            "depression": ["Fluoxetine", "Sertraline", "Escitalopram"]
        }
        
        return condition_medications.get(condition.lower(), ["No specific recommendations available"])

def get_medication_manager():
    """Factory function to create and return a MedicationManager instance"""
    return MedicationManager() 