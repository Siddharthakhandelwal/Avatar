import json
import os
from datetime import datetime

class PatientVitals:
    """Module for tracking and analyzing patient vital signs"""
    
    def __init__(self):
        self.vitals_file = "patient_vitals.json"
        self.vitals_data = self._load_vitals()
        
        # Normal ranges for common vital signs
        self.normal_ranges = {
            "blood_pressure_systolic": (90, 120),
            "blood_pressure_diastolic": (60, 80),
            "heart_rate": (60, 100),
            "respiratory_rate": (12, 20),
            "temperature": (97.0, 99.0),  # Fahrenheit
            "oxygen_saturation": (95, 100),
            "blood_glucose": (70, 140)
        }
    
    def _load_vitals(self):
        """Load vitals data from file"""
        try:
            if os.path.exists(self.vitals_file):
                with open(self.vitals_file, "r") as file:
                    return json.load(file)
            return {}
        except Exception as e:
            print(f"Error loading vitals data: {e}")
            return {}
    
    def _save_vitals(self):
        """Save vitals data to file"""
        try:
            with open(self.vitals_file, "w") as file:
                json.dump(self.vitals_data, file, indent=2)
        except Exception as e:
            print(f"Error saving vitals data: {e}")
    
    def record_vitals(self, patient_id, vitals):
        """
        Record a set of vital signs for a patient
        
        Args:
            patient_id (str): The patient's ID
            vitals (dict): A dictionary containing vital sign measurements
                           (e.g., blood_pressure, heart_rate, etc.)
        
        Returns:
            str: The ID of the recorded vitals entry
        """
        if patient_id not in self.vitals_data:
            self.vitals_data[patient_id] = []
        
        # Add timestamp to vitals
        vitals["timestamp"] = datetime.now().isoformat()
        vitals["vitals_id"] = f"vitals_{len(self.vitals_data[patient_id]) + 1}"
        
        # Add vitals to patient's record
        self.vitals_data[patient_id].append(vitals)
        self._save_vitals()
        
        return vitals["vitals_id"]
    
    def get_patient_vitals(self, patient_id, limit=10):
        """
        Get vitals history for a patient
        
        Args:
            patient_id (str): The patient's ID
            limit (int): Maximum number of records to return (most recent first)
        
        Returns:
            list: A list of vital sign records for the patient
        """
        if patient_id not in self.vitals_data:
            return []
        
        vitals = sorted(
            self.vitals_data[patient_id],
            key=lambda x: x["timestamp"],
            reverse=True
        )
        
        return vitals[:limit]
    
    def analyze_vitals(self, patient_id, vital_type=None):
        """
        Analyze a patient's vitals for concerning values
        
        Args:
            patient_id (str): The patient's ID
            vital_type (str, optional): Specific vital to analyze. Defaults to None (all vitals).
        
        Returns:
            dict: Analysis results with potential concerns
        """
        if patient_id not in self.vitals_data or not self.vitals_data[patient_id]:
            return {"status": "No data available"}
        
        vitals = self.vitals_data[patient_id]
        concerns = []
        
        for vital_record in vitals:
            for key, value in vital_record.items():
                # Skip non-vital keys
                if key in ["timestamp", "vitals_id", "notes"]:
                    continue
                
                # If a specific vital type was requested, skip others
                if vital_type and key != vital_type:
                    continue
                
                # Check if this vital has a defined normal range
                if key in self.normal_ranges:
                    min_val, max_val = self.normal_ranges[key]
                    
                    try:
                        # Handle blood pressure which may be stored as string "120/80"
                        if key == "blood_pressure":
                            sys, dia = map(int, value.split("/"))
                            
                            if sys < self.normal_ranges["blood_pressure_systolic"][0]:
                                concerns.append(f"Low systolic blood pressure ({sys}) on {vital_record['timestamp']}")
                            elif sys > self.normal_ranges["blood_pressure_systolic"][1]:
                                concerns.append(f"High systolic blood pressure ({sys}) on {vital_record['timestamp']}")
                                
                            if dia < self.normal_ranges["blood_pressure_diastolic"][0]:
                                concerns.append(f"Low diastolic blood pressure ({dia}) on {vital_record['timestamp']}")
                            elif dia > self.normal_ranges["blood_pressure_diastolic"][1]:
                                concerns.append(f"High diastolic blood pressure ({dia}) on {vital_record['timestamp']}")
                        else:
                            # Handle numeric values
                            val = float(value)
                            if val < min_val:
                                concerns.append(f"Low {key.replace('_', ' ')} ({val}) on {vital_record['timestamp']}")
                            elif val > max_val:
                                concerns.append(f"High {key.replace('_', ' ')} ({val}) on {vital_record['timestamp']}")
                    except (ValueError, TypeError):
                        # Skip values that can't be parsed
                        continue
        
        if concerns:
            return {
                "status": "Concerns identified",
                "concerns": concerns
            }
        else:
            return {"status": "All vitals within normal range"}
    
    def get_vitals_trends(self, patient_id, vital_type, days=30):
        """
        Get trend data for a specific vital sign
        
        Args:
            patient_id (str): The patient's ID
            vital_type (str): The type of vital sign to analyze
            days (int): Number of days to include in trend
        
        Returns:
            list: Trend data for the specified vital sign
        """
        if patient_id not in self.vitals_data:
            return []
        
        vitals = self.vitals_data[patient_id]
        
        # Filter vitals by date and type
        cutoff_date = (datetime.now() - datetime.timedelta(days=days)).isoformat()
        trend_data = []
        
        for vital in vitals:
            if vital["timestamp"] >= cutoff_date and vital_type in vital:
                trend_data.append({
                    "timestamp": vital["timestamp"],
                    "value": vital[vital_type]
                })
        
        # Sort by timestamp
        trend_data.sort(key=lambda x: x["timestamp"])
        
        return trend_data
    
    def is_vital_in_range(self, vital_type, value):
        """
        Check if a vital sign value is within normal range
        
        Args:
            vital_type (str): The type of vital sign
            value (float/str): The vital sign value
        
        Returns:
            tuple: (bool, str) indicating if in range and a description
        """
        if vital_type not in self.normal_ranges:
            return None, "Unknown vital type"
        
        try:
            # Handle blood pressure which may be stored as string "120/80"
            if vital_type == "blood_pressure":
                sys, dia = map(int, value.split("/"))
                sys_min, sys_max = self.normal_ranges["blood_pressure_systolic"]
                dia_min, dia_max = self.normal_ranges["blood_pressure_diastolic"]
                
                sys_in_range = sys_min <= sys <= sys_max
                dia_in_range = dia_min <= dia <= dia_max
                
                if sys_in_range and dia_in_range:
                    return True, "Blood pressure within normal range"
                else:
                    issues = []
                    if not sys_in_range:
                        if sys < sys_min:
                            issues.append("low systolic")
                        else:
                            issues.append("high systolic")
                    if not dia_in_range:
                        if dia < dia_min:
                            issues.append("low diastolic")
                        else:
                            issues.append("high diastolic")
                    
                    return False, f"Blood pressure shows {', '.join(issues)}"
            else:
                # Handle numeric values
                val = float(value)
                min_val, max_val = self.normal_ranges[vital_type]
                
                if min_val <= val <= max_val:
                    return True, f"{vital_type.replace('_', ' ')} within normal range"
                elif val < min_val:
                    return False, f"{vital_type.replace('_', ' ')} is low"
                else:
                    return False, f"{vital_type.replace('_', ' ')} is high"
                    
        except (ValueError, TypeError):
            return None, "Invalid value format"

def get_patient_vitals_tracker():
    """Factory function to create and return a PatientVitals instance"""
    return PatientVitals() 