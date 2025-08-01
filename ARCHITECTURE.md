# MedyBot Architecture & Workflow

## Overview
MedyBot is a command-line medical assistant chatbot powered by Google's Gemini API. It interacts with users (patients), answers health-related questions, suggests over-the-counter medicines, and provides general advice, while always reminding users to consult a real doctor for serious issues. The assistant persona is Nirog, the friendly medical assistant from Delhi working at Medycall, and never refers to itself as an AI.

---

## Workflow

1. **User Input:**
   - The user starts the chatbot and enters their health-related question or concern via the command line.

2. **Conversation Context:**
   - The chatbot maintains a conversation history (context) as a list of message dictionaries, each with a `role` ("user" or "model") and a `parts` list (containing the message text).

3. **Instructions:**
   - The first message in the conversation history is a user message containing detailed instructions for the assistant's behavior, including available doctors and response style.

4. **Timestamp Integration:**
   - Each user message includes the current timestamp for context-aware responses and accurate appointment scheduling.

4. **Gemini API Call:**
   - The full conversation history is sent to the Gemini API (`gemini-2.5-pro` model) for processing.

5. **AI Response:**
   - The Gemini model generates a response, which is returned to the chatbot.

6. **Display to User:**
   - The chatbot prints the AI’s response to the user in the command line.

7. **Loop:**
   - Steps 1–6 repeat until the user types an exit command (e.g., `exit`, `quit`, `bye`).

---

## Available Medical Specialists

The system includes access to the following qualified doctors for appointment booking:

| Doctor | Specialty | Location | Availability |
|--------|-----------|----------|--------------|
| **Dr. Sarah Johnson** | Cardiologist (Heart Specialist) | Vrindavan | Mon-Fri, 9 AM - 5 PM |
| **Dr. Michael Chen** | General Physician | Gaziabad | Mon-Sat, 8 AM - 6 PM |
| **Dr. Priya Patel** | Pediatrician (Child Specialist) | Delhi | Tue-Sun, 10 AM - 4 PM |
| **Dr. Robert Wilson** | Dermatologist (Skin Specialist) | Gurgaon | Mon-Fri, 11 AM - 7 PM |
| **Dr. Lisa Garcia** | Neurologist (Brain & Nerve Specialist) | Mumbai | Wed-Sun, 9 AM - 3 PM |

---

## Architecture Diagram

```
User (Patient)
    │
    ▼
[Command Line Interface]
    │
    ▼
[Chatbot Script (chat_bot.py)]
    │
    │  (Maintains conversation history as list of {role, parts})
    ▼
[Google Gemini API]
    │
    ▼
[Gemini Model]
    │
    ▼
[Chatbot Script]
    │
    ▼
User (Patient)
```

---

## Data Flow

1. **Input:**
   - User types a message/question in the command line.
   - Example: "I have a headache and mild fever. What should I do?"

2. **Processing:**
   - The script appends the user message to the conversation history as `{"role": "user", "parts": [user_input]}`.
   - The full conversation (instructions + history) is sent to the Gemini API.

3. **AI Generation:**
   - The Gemini model processes the input and generates a response based on the context and instructions.

4. **Output:**
   - The response is displayed to the user.
   - Example: "For mild headache and fever, you may consider taking paracetamol. However, if symptoms persist or worsen, please consult a healthcare professional."

5. **Repeat:**
   - The conversation continues, with each new user input and AI response appended to the context.

---

## Key Components

- **Command Line Interface:** Handles user input and output.
- **Conversation Manager:** Maintains the conversation history for context-aware responses (list of message dicts).
- **Instructions Message:** Sets the assistant's behavior, available doctors, and boundaries.
- **Timestamp System:** Integrates real-time information for context-aware responses and appointment scheduling.
- **Gemini API Client:** Sends requests and receives responses from the Gemini model.
- **Doctor Database:** Maintains information about available specialists across multiple cities.

---

## Enhanced Features

### Real-Time Timestamp Integration
- **Current Time Tracking**: Every user message includes the current date and time
- **Appointment Scheduling**: Uses real-time information for accurate booking
- **Session Management**: Tracks conversation duration and context
- **Time-Sensitive Advice**: Provides context-aware medical guidance

### Multi-City Doctor Network
- **Geographic Coverage**: Doctors available across Delhi, Mumbai, Gurgaon, Gaziabad, and Vrindavan
- **Specialty Matching**: Automatically matches users with appropriate specialists
- **Availability Information**: Includes doctor schedules and working hours
- **Professional Formatting**: Structures appointment details professionally

### Advanced Conversation Management
- **Context Retention**: Maintains full conversation history during session
- **Memory Integration**: Builds responses based on previous interactions
- **Natural Flow**: Enables follow-up questions and clarifications
- **Session Isolation**: Each new session starts fresh for privacy

---

## Security & Privacy Notes
- No user data is stored permanently; all conversation context is kept in memory during the session only.
- The chatbot does not diagnose or prescribe; it only provides general advice and always recommends consulting a real doctor.

---

## Extending the System
- **GUI Integration:** The chatbot can be extended to a web or mobile interface.
- **Medical Database Integration:** For more accurate medicine suggestions, integrate with a verified medical database.
- **Multilingual Support:** Add language translation for broader accessibility.

---

## Disclaimer
This architecture is for a demo/educational chatbot and should not be used for real medical decision-making. 