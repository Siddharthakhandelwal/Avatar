# Voice-to-Voice Medical AI Assistant

A console-based medical AI assistant that can:

- Interact with you using voice
- Diagnose basic medical conditions
- Suggest remedies and medications
- Book simulated doctor appointments

## Setup

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. (Optional) For better responses, create a `.env` file in the project root with your API keys:

```
# Hugging Face API key (for better conversational responses)
HUGGINGFACE_API_KEY=your_key_here

# Azure Speech Service credentials (for voice capabilities)
AZURE_SPEECH_KEY=your_azure_speech_key_here
AZURE_SPEECH_REGION=eastus
```

If you don't have API keys, the system will use fallback mechanisms:

- Without a Hugging Face key, the system will use rule-based responses
- Without Azure Speech credentials, it will fall back to pyttsx3 for text-to-speech

## Usage

There are several ways to interact with the assistant:

### Option 1: Use the launcher script (recommended)

```bash
python run.py
```

This script lets you choose between voice mode and text mode, and will check if you have all required dependencies.

### Option 2: Run specific modes directly

For voice interaction:

```bash
python medical_assistant.py
```

For text interaction (if you have issues with voice recognition):

```bash
python text_mode.py
```

### Option 3: Run the minimalist version (no dependencies required)

If you're having trouble installing the dependencies, or just want to test the basic functionality:

```bash
python test_assistant.py
```

This version works with just the Python standard library - no additional packages needed.

### Voice Commands

- **Describe symptoms**: "I have a headache and feel tired"
- **Ask for medication**: "What medicine should I take for my cough?"
- **Book appointment**: "I need to book an appointment with a doctor"
- **Exit**: "Goodbye" or "Exit"

## Features

- **Voice Recognition**: Uses Azure Speech Service for high-quality speech recognition
- **Text-to-Speech**: Uses Azure Speech Service for natural-sounding responses
- **Medical Diagnosis**: Basic symptom matching and condition identification
- **Treatment Suggestions**: Recommends over-the-counter medications
- **Appointment Booking**: Simulates scheduling a doctor's appointment
- **Text Mode Fallback**: Can operate fully in text mode if voice services are unavailable

## Disclaimer

This application is for educational purposes only and not for actual medical use. Always consult a real healthcare professional for medical advice.

## Voice Recognition

This application uses Microsoft's Azure Speech Service for high-quality speech recognition and synthesis. The included key has limited usage, so for extended use:

1. Create a free Azure account at https://azure.microsoft.com/
2. Create a Speech Service resource
3. Copy your key and region to the `.env` file
