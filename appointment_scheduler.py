import datetime
import json
import os
from pathlib import Path
from datetime import timedelta

class AppointmentScheduler:
    """Module for scheduling and managing patient appointments"""
    
    def __init__(self):
        self.appointments_file = "appointments.json"
        self.appointments = self._load_appointments()
        
        # Default appointment durations in minutes
        self.default_durations = {
            "checkup": 30,
            "consultation": 45,
            "follow_up": 20,
            "procedure": 60,
            "emergency": 45,
            "specialist": 60
        }
        
        # Working hours
        self.working_hours = {
            "Monday": {"start": "09:00", "end": "17:00"},
            "Tuesday": {"start": "09:00", "end": "17:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Thursday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "09:00", "end": "17:00"},
            "Saturday": {"start": "10:00", "end": "14:00"},
            "Sunday": {"start": None, "end": None}  # Closed
        }
    
    def _load_appointments(self):
        """Load appointments from file"""
        try:
            if os.path.exists(self.appointments_file):
                with open(self.appointments_file, "r") as file:
                    return json.load(file)
            return {}
        except Exception as e:
            print(f"Error loading appointments: {e}")
            return {}
    
    def _save_appointments(self):
        """Save appointments to file"""
        try:
            with open(self.appointments_file, "w") as file:
                json.dump(self.appointments, file, indent=2)
        except Exception as e:
            print(f"Error saving appointments: {e}")
    
    def schedule_appointment(self, patient_id, doctor_id, date_time, appointment_type, notes=""):
        """
        Schedule a new appointment
        
        Args:
            patient_id (str): The patient's ID
            doctor_id (str): The doctor's ID
            date_time (str): ISO format datetime string
            appointment_type (str): Type of appointment
            notes (str, optional): Additional appointment notes
        
        Returns:
            str: The ID of the scheduled appointment or None if failed
        """
        try:
            # Validate date/time format
            appointment_datetime = datetime.datetime.fromisoformat(date_time)
            
            # Check if appointment time is during working hours
            weekday = appointment_datetime.strftime("%A")
            if self.working_hours[weekday]["start"] is None:
                return {"status": "error", "message": f"No appointments available on {weekday}"}
            
            # Convert working hours to datetime for comparison
            appt_date = appointment_datetime.date()
            start_time = datetime.datetime.strptime(self.working_hours[weekday]["start"], "%H:%M").time()
            end_time = datetime.datetime.strptime(self.working_hours[weekday]["end"], "%H:%M").time()
            
            working_start = datetime.datetime.combine(appt_date, start_time)
            working_end = datetime.datetime.combine(appt_date, end_time)
            
            if appointment_datetime < working_start or appointment_datetime >= working_end:
                return {"status": "error", "message": "Appointment time outside working hours"}
            
            # Check for appointment conflicts
            duration = self.default_durations.get(appointment_type.lower(), 30)
            appointment_end = appointment_datetime + timedelta(minutes=duration)
            
            if doctor_id in self.appointments:
                for appt_id, appt in self.appointments[doctor_id].items():
                    existing_start = datetime.datetime.fromisoformat(appt["date_time"])
                    existing_end = existing_start + timedelta(minutes=self.default_durations.get(appt["type"].lower(), 30))
                    
                    # Check if new appointment overlaps with existing one
                    if (appointment_datetime < existing_end and appointment_end > existing_start):
                        return {"status": "error", "message": "Appointment conflicts with existing schedule"}
            
            # Generate a unique appointment ID
            appointment_id = f"appt_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # Create appointment object
            appointment = {
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "date_time": date_time,
                "type": appointment_type,
                "status": "scheduled",
                "notes": notes,
                "created_at": datetime.datetime.now().isoformat()
            }
            
            # Add to appointments
            if doctor_id not in self.appointments:
                self.appointments[doctor_id] = {}
            
            self.appointments[doctor_id][appointment_id] = appointment
            self._save_appointments()
            
            return {"status": "success", "appointment_id": appointment_id}
            
        except ValueError:
            return {"status": "error", "message": "Invalid date format"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def reschedule_appointment(self, appointment_id, doctor_id, new_date_time):
        """
        Reschedule an existing appointment
        
        Args:
            appointment_id (str): The appointment ID
            doctor_id (str): The doctor's ID
            new_date_time (str): New ISO format datetime string
        
        Returns:
            dict: Status of the rescheduling operation
        """
        try:
            if doctor_id not in self.appointments or appointment_id not in self.appointments[doctor_id]:
                return {"status": "error", "message": "Appointment not found"}
            
            # Validate date/time format
            new_datetime = datetime.datetime.fromisoformat(new_date_time)
            
            # Get current appointment
            appointment = self.appointments[doctor_id][appointment_id]
            
            # Create a copy of the appointment with the new date/time
            original_date = appointment["date_time"]
            appointment["date_time"] = new_date_time
            appointment["updated_at"] = datetime.datetime.now().isoformat()
            appointment["rescheduled"] = True
            
            # Check if the new time works (reuse scheduling logic)
            appointment_type = appointment["type"]
            patient_id = appointment["patient_id"]
            
            # Temporarily remove this appointment to avoid self-conflict
            temp_appointment = self.appointments[doctor_id].pop(appointment_id)
            
            # Check if new time works
            result = self.schedule_appointment(
                patient_id, 
                doctor_id, 
                new_date_time, 
                appointment_type,
                appointment.get("notes", "")
            )
            
            # If scheduling would work, update the existing appointment instead
            if result["status"] == "success":
                # Remove the temporary appointment we just created
                self.appointments[doctor_id].pop(result["appointment_id"])
                # Put back our original appointment with updated time
                self.appointments[doctor_id][appointment_id] = temp_appointment
                self._save_appointments()
                return {"status": "success", "message": "Appointment rescheduled"}
            else:
                # Put back original appointment with original time
                temp_appointment["date_time"] = original_date
                self.appointments[doctor_id][appointment_id] = temp_appointment
                self._save_appointments()
                return {"status": "error", "message": result["message"]}
                
        except ValueError:
            return {"status": "error", "message": "Invalid date format"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def cancel_appointment(self, appointment_id, doctor_id, reason=""):
        """
        Cancel an existing appointment
        
        Args:
            appointment_id (str): The appointment ID
            doctor_id (str): The doctor's ID
            reason (str, optional): Reason for cancellation
        
        Returns:
            dict: Status of the cancellation operation
        """
        try:
            if doctor_id not in self.appointments or appointment_id not in self.appointments[doctor_id]:
                return {"status": "error", "message": "Appointment not found"}
            
            # Update appointment status
            self.appointments[doctor_id][appointment_id]["status"] = "cancelled"
            self.appointments[doctor_id][appointment_id]["cancelled_at"] = datetime.datetime.now().isoformat()
            self.appointments[doctor_id][appointment_id]["cancellation_reason"] = reason
            
            self._save_appointments()
            return {"status": "success", "message": "Appointment cancelled"}
            
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_doctor_appointments(self, doctor_id, start_date=None, end_date=None, status=None):
        """
        Get appointments for a specific doctor
        
        Args:
            doctor_id (str): The doctor's ID
            start_date (str, optional): ISO format start date
            end_date (str, optional): ISO format end date
            status (str, optional): Filter by appointment status
        
        Returns:
            list: Filtered list of appointments
        """
        if doctor_id not in self.appointments:
            return []
        
        appointments = []
        
        for appt_id, appt in self.appointments[doctor_id].items():
            appt_datetime = datetime.datetime.fromisoformat(appt["date_time"])
            
            # Apply date filter if provided
            if start_date and appt_datetime < datetime.datetime.fromisoformat(start_date):
                continue
            if end_date and appt_datetime > datetime.datetime.fromisoformat(end_date):
                continue
            
            # Apply status filter if provided
            if status and appt["status"] != status:
                continue
            
            # Add appointment ID to the appointment object for convenience
            appointment_with_id = appt.copy()
            appointment_with_id["appointment_id"] = appt_id
            appointments.append(appointment_with_id)
        
        # Sort appointments by date/time
        appointments.sort(key=lambda x: x["date_time"])
        
        return appointments
    
    def get_patient_appointments(self, patient_id, include_past=False):
        """
        Get all appointments for a specific patient
        
        Args:
            patient_id (str): The patient's ID
            include_past (bool): Whether to include past appointments
        
        Returns:
            list: List of patient appointments
        """
        patient_appointments = []
        current_datetime = datetime.datetime.now()
        
        for doctor_id, doctor_appointments in self.appointments.items():
            for appt_id, appt in doctor_appointments.items():
                if appt["patient_id"] == patient_id:
                    # Check if we should include this appointment
                    appt_datetime = datetime.datetime.fromisoformat(appt["date_time"])
                    
                    if not include_past and appt_datetime < current_datetime:
                        continue
                    
                    # Add appointment ID and doctor ID to the appointment object
                    appointment_with_id = appt.copy()
                    appointment_with_id["appointment_id"] = appt_id
                    appointment_with_id["doctor_id"] = doctor_id
                    patient_appointments.append(appointment_with_id)
        
        # Sort appointments by date/time
        patient_appointments.sort(key=lambda x: x["date_time"])
        
        return patient_appointments
    
    def get_available_slots(self, doctor_id, date, duration=30):
        """
        Get available appointment slots for a doctor on a specific day
        
        Args:
            doctor_id (str): The doctor's ID
            date (str): ISO format date string (YYYY-MM-DD)
            duration (int, optional): Appointment duration in minutes
        
        Returns:
            list: List of available time slots
        """
        try:
            # Parse the date
            target_date = datetime.datetime.fromisoformat(date).date()
            weekday = target_date.strftime("%A")
            
            # Check if practice is open that day
            if self.working_hours[weekday]["start"] is None:
                return []
            
            # Get working hours for that day
            start_time = datetime.datetime.strptime(self.working_hours[weekday]["start"], "%H:%M").time()
            end_time = datetime.datetime.strptime(self.working_hours[weekday]["end"], "%H:%M").time()
            
            working_start = datetime.datetime.combine(target_date, start_time)
            working_end = datetime.datetime.combine(target_date, end_time)
            
            # Generate all possible slots
            slots = []
            current_slot = working_start
            
            while current_slot + timedelta(minutes=duration) <= working_end:
                slots.append(current_slot.isoformat())
                current_slot += timedelta(minutes=duration)
            
            # Remove slots that conflict with existing appointments
            if doctor_id in self.appointments:
                for appt_id, appt in self.appointments[doctor_id].items():
                    if appt["status"] == "cancelled":
                        continue
                        
                    appt_datetime = datetime.datetime.fromisoformat(appt["date_time"])
                    appt_date = appt_datetime.date()
                    
                    # Only check appointments on the target date
                    if appt_date == target_date:
                        appt_duration = self.default_durations.get(appt["type"].lower(), 30)
                        appt_end = appt_datetime + timedelta(minutes=appt_duration)
                        
                        # Remove slots that overlap with this appointment
                        slots = [
                            slot for slot in slots
                            if not (
                                datetime.datetime.fromisoformat(slot) < appt_end and
                                datetime.datetime.fromisoformat(slot) + timedelta(minutes=duration) > appt_datetime
                            )
                        ]
            
            return slots
            
        except ValueError:
            return []
        except Exception as e:
            print(f"Error getting available slots: {e}")
            return []

def get_appointment_scheduler():
    """Factory function to create and return an AppointmentScheduler instance"""
    return AppointmentScheduler() 