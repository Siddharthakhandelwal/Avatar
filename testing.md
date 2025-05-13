# Medical Assistant Chatbot - Test Script

## Overview

This document provides a structured test script to verify all functionalities of the Medical Assistant Chatbot. Follow the conversation flow outlined below to test each feature systematically.

## Setup Instructions

1. Ensure all required environment variables are set in the `.env` file:

   - `GROQ_API_KEY`
   - `AZURE_SPEECH_KEY`
   - `AZURE_SPEECH_REGION`

2. Install required packages:

   ```
   pip install azure-cognitiveservices-speech groq python-dotenv
   ```

3. Run the script:
   ```
   python medical_assistant.py
   ```

## Test Script

### Test 1: Wake Word Detection

**Action:** Wait for the initial prompt and speak one of the wake words

- Say: "Hey Maya"
- Expected: The assistant should respond with "Hello! I'm listening."

### Test 2: Basic Medical Query

**Action:** Ask a simple medical question

- Say: "What are the symptoms of the common cold?"
- Expected: Maya should list common cold symptoms professionally

### Test 3: Personality Verification

**Action:** Ask a personal question to verify persona

- Say: "What's your name?"
- Expected: The assistant should identify itself as Dr. Maya (not as an AI)
- Say: "How old are you?"
- Expected: The assistant should give a practical age as per instructions

### Test 4: Non-Medical Query Handling

**Action:** Ask an off-topic question

- Say: "What's the capital of France?"
- Expected: Maya should politely redirect to medical topics or give a brief answer before redirecting

### Test 5: Appointment Booking - Basic

**Action:** Request an appointment

- Say: "I need to make an appointment"
- Expected: Maya should start collecting information for an appointment
- Follow the prompts to provide:
  - Your name
  - Contact information (phone or email)
  - Reason for visit
  - Preferred date and time

### Test 6: Appointment Booking - Doctor Selection

**Action:** Ask about available doctors

- Say: "Which doctors are available?"
- Expected: Maya should list the available doctors and their specialties
- Say: "I'd like to see Dr. Michael Chen"
- Expected: Maya should acknowledge and continue booking process with this doctor

### Test 7: Emergency Detection

**Action:** Mention emergency symptoms

- Say: "I'm having severe chest pain right now"
- Expected: Maya should immediately advise calling 911 or going to the emergency room
- The assistant should ask if you want to continue with other information

### Test 8: Error Handling - Speech Recognition

**Action:** Remain silent after a prompt

- Say: Nothing (remain silent for 5-10 seconds)
- Expected: Maya should prompt you to repeat or indicate it didn't hear anything

### Test 9: Multi-turn Conversation

**Action:** Have a back-and-forth medical conversation

- Say: "I've been having headaches recently"
- Expected: Maya should ask follow-up questions about your symptoms
- Answer Maya's questions to test the conversation flow
- Verify that Maya remembers context from earlier in the conversation

### Test 10: Conversation Saving

**Action:** End the conversation naturally

- Say: "Thank you, goodbye"
- Expected:
  - If an appointment was made: Maya should confirm appointment details before ending
  - Maya should thank you and end the conversation
  - Check that a conversation JSON file was created in the "conversations" directory

### Test 11: Appointment Saving

**Action:** Verify appointment was saved (if one was made)

- After the conversation ends, check the "appointments" directory
- Verify that a JSON file was created with the correct appointment details

## Advanced Testing (Optional)

### Test 12: Handling Complex Medical Questions

**Action:** Ask a more complex medical query

- Say: "What's the difference between a viral and bacterial infection?"
- Expected: Maya should provide an informative but concise explanation

### Test 13: Interruption Recovery

**Action:** Interrupt the flow and restart

- During a conversation, close the program (Ctrl+C)
- Restart the program and verify it initializes correctly

### Test 14: Multiple Wake Word Variations

**Action:** Test different wake word combinations

- Try various wake phrases like "Medical Assistant", "Medycall", "Hey", etc.
- Verify the assistant activates properly with each valid wake word

## Bug Reporting

If you encounter any issues during testing, please document:

1. The test number and action you were performing
2. What you expected to happen
3. What actually happened
4. Any error messages displayed in the console

## Expected Output Files

After completing the tests, you should have:

1. At least one JSON file in the "conversations" directory
2. If appointments were made, at least one JSON file in the "appointments" directory

These files should be properly formatted and contain the relevant conversation and appointment details.
