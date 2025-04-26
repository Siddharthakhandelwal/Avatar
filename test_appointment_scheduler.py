import unittest
from datetime import datetime, timedelta
import os
import json
from appointment_scheduler import AppointmentScheduler

class TestAppointmentScheduler(unittest.TestCase):
    
    def setUp(self):
        # Create a test instance with a test file
        self.scheduler = AppointmentScheduler()
        self.scheduler.appointments_file = "test_appointments.json"
        self.scheduler.appointments = {}
        
        # Ensure test file doesn't exist from previous tests
        if os.path.exists(self.scheduler.appointments_file):
            os.remove(self.scheduler.appointments_file)
    
    def tearDown(self):
        # Clean up test file
        if os.path.exists(self.scheduler.appointments_file):
            os.remove(self.scheduler.appointments_file)
    
    def test_schedule_appointment(self):
        # Test scheduling a valid appointment
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        # Make appointment at 10 AM
        appointment_time = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time())
        result = self.scheduler.schedule_appointment(
            "patient123", 
            "doctor456", 
            appointment_time.isoformat(), 
            "checkup", 
            "Initial checkup"
        )
        
        self.assertEqual(result["status"], "success")
        self.assertTrue("appointment_id" in result)
        
        # Verify appointment was saved
        self.assertTrue("doctor456" in self.scheduler.appointments)
        self.assertEqual(len(self.scheduler.appointments["doctor456"]), 1)
        
        # Get the appointment
        appt_id = result["appointment_id"]
        appointment = self.scheduler.appointments["doctor456"][appt_id]
        
        self.assertEqual(appointment["patient_id"], "patient123")
        self.assertEqual(appointment["status"], "scheduled")
        self.assertEqual(appointment["type"], "checkup")
        self.assertEqual(appointment["notes"], "Initial checkup")
    
    def test_schedule_outside_hours(self):
        # Test scheduling outside working hours
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        # Make appointment at 3 AM (outside working hours)
        appointment_time = datetime.combine(tomorrow.date(), datetime.strptime("03:00", "%H:%M").time())
        result = self.scheduler.schedule_appointment(
            "patient123",
            "doctor456",
            appointment_time.isoformat(),
            "checkup"
        )
        
        self.assertEqual(result["status"], "error")
        self.assertTrue("outside working hours" in result["message"])
    
    def test_schedule_on_sunday(self):
        # Find the next Sunday
        today = datetime.now().date()
        days_until_sunday = (6 - today.weekday()) % 7
        next_sunday = today + timedelta(days=days_until_sunday)
        
        # Try to schedule on Sunday
        appointment_time = datetime.combine(next_sunday, datetime.strptime("10:00", "%H:%M").time())
        result = self.scheduler.schedule_appointment(
            "patient123",
            "doctor456",
            appointment_time.isoformat(),
            "checkup"
        )
        
        self.assertEqual(result["status"], "error")
        self.assertTrue("No appointments available" in result["message"])
    
    def test_appointment_conflict(self):
        # Schedule first appointment
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        appointment_time = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time())
        first_result = self.scheduler.schedule_appointment(
            "patient123", 
            "doctor456", 
            appointment_time.isoformat(), 
            "checkup"
        )
        
        # Try to schedule overlapping appointment
        second_result = self.scheduler.schedule_appointment(
            "patient789", 
            "doctor456", 
            appointment_time.isoformat(), 
            "consultation"
        )
        
        self.assertEqual(first_result["status"], "success")
        self.assertEqual(second_result["status"], "error")
        self.assertTrue("conflicts" in second_result["message"])
    
    def test_reschedule_appointment(self):
        # Schedule appointment
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        appointment_time = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time())
        schedule_result = self.scheduler.schedule_appointment(
            "patient123", 
            "doctor456", 
            appointment_time.isoformat(), 
            "checkup"
        )
        
        # Reschedule to 2 PM
        new_time = datetime.combine(tomorrow.date(), datetime.strptime("14:00", "%H:%M").time())
        reschedule_result = self.scheduler.reschedule_appointment(
            schedule_result["appointment_id"],
            "doctor456",
            new_time.isoformat()
        )
        
        self.assertEqual(reschedule_result["status"], "success")
        
        # Verify appointment was updated
        doctor_appts = self.scheduler.get_doctor_appointments("doctor456")
        self.assertEqual(len(doctor_appts), 1)
        self.assertEqual(doctor_appts[0]["date_time"], new_time.isoformat())
    
    def test_cancel_appointment(self):
        # Schedule appointment
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        appointment_time = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time())
        schedule_result = self.scheduler.schedule_appointment(
            "patient123", 
            "doctor456", 
            appointment_time.isoformat(), 
            "checkup"
        )
        
        # Cancel appointment
        cancel_result = self.scheduler.cancel_appointment(
            schedule_result["appointment_id"],
            "doctor456",
            "Patient request"
        )
        
        self.assertEqual(cancel_result["status"], "success")
        
        # Verify appointment was cancelled
        appt_id = schedule_result["appointment_id"]
        appointment = self.scheduler.appointments["doctor456"][appt_id]
        self.assertEqual(appointment["status"], "cancelled")
        self.assertEqual(appointment["cancellation_reason"], "Patient request")
    
    def test_get_doctor_appointments(self):
        # Schedule multiple appointments
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        # First appointment
        time1 = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time())
        self.scheduler.schedule_appointment(
            "patient123", 
            "doctor456", 
            time1.isoformat(), 
            "checkup"
        )
        
        # Second appointment
        time2 = datetime.combine(tomorrow.date(), datetime.strptime("11:00", "%H:%M").time())
        result2 = self.scheduler.schedule_appointment(
            "patient789", 
            "doctor456", 
            time2.isoformat(), 
            "follow_up"
        )
        
        # Third appointment that will be cancelled
        time3 = datetime.combine(tomorrow.date(), datetime.strptime("14:00", "%H:%M").time())
        result3 = self.scheduler.schedule_appointment(
            "patient456", 
            "doctor456", 
            time3.isoformat(), 
            "consultation"
        )
        
        # Cancel the third appointment
        self.scheduler.cancel_appointment(
            result3["appointment_id"],
            "doctor456"
        )
        
        # Get all appointments
        all_appts = self.scheduler.get_doctor_appointments("doctor456")
        self.assertEqual(len(all_appts), 3)
        
        # Get only scheduled appointments
        scheduled_appts = self.scheduler.get_doctor_appointments("doctor456", status="scheduled")
        self.assertEqual(len(scheduled_appts), 2)
        
        # Get only cancelled appointments
        cancelled_appts = self.scheduler.get_doctor_appointments("doctor456", status="cancelled")
        self.assertEqual(len(cancelled_appts), 1)
    
    def test_get_patient_appointments(self):
        # Schedule appointments for different patients
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        # Patient 1 appointments
        time1 = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time())
        self.scheduler.schedule_appointment(
            "patient123", 
            "doctor456", 
            time1.isoformat(), 
            "checkup"
        )
        
        time2 = datetime.combine(tomorrow.date() + timedelta(days=2), datetime.strptime("11:00", "%H:%M").time())
        self.scheduler.schedule_appointment(
            "patient123", 
            "doctor789", 
            time2.isoformat(), 
            "follow_up"
        )
        
        # Patient 2 appointment
        time3 = datetime.combine(tomorrow.date(), datetime.strptime("14:00", "%H:%M").time())
        self.scheduler.schedule_appointment(
            "patient456", 
            "doctor456", 
            time3.isoformat(), 
            "consultation"
        )
        
        # Get appointments for patient 1
        patient1_appts = self.scheduler.get_patient_appointments("patient123")
        self.assertEqual(len(patient1_appts), 2)
        
        # Get appointments for patient 2
        patient2_appts = self.scheduler.get_patient_appointments("patient456")
        self.assertEqual(len(patient2_appts), 1)
    
    def test_get_available_slots(self):
        tomorrow = datetime.now() + timedelta(days=1)
        # Ensure it's a weekday
        if tomorrow.weekday() == 6:  # Sunday
            tomorrow = tomorrow + timedelta(days=1)
        
        # Schedule an appointment
        time1 = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time())
        self.scheduler.schedule_appointment(
            "patient123", 
            "doctor456", 
            time1.isoformat(), 
            "checkup"  # 30 minutes
        )
        
        # Get available slots
        slots = self.scheduler.get_available_slots("doctor456", tomorrow.date().isoformat())
        
        # Verify that 10:00 is not available
        ten_am = datetime.combine(tomorrow.date(), datetime.strptime("10:00", "%H:%M").time()).isoformat()
        self.assertNotIn(ten_am, slots)
        
        # But 10:30 should be available
        ten_thirty_am = datetime.combine(tomorrow.date(), datetime.strptime("10:30", "%H:%M").time()).isoformat()
        self.assertIn(ten_thirty_am, slots)
        
        # Sunday should have no slots
        sunday_date = tomorrow.date()
        while sunday_date.weekday() != 6:  # Find next Sunday
            sunday_date = sunday_date + timedelta(days=1)
        
        sunday_slots = self.scheduler.get_available_slots("doctor456", sunday_date.isoformat())
        self.assertEqual(len(sunday_slots), 0)

if __name__ == "__main__":
    unittest.main() 