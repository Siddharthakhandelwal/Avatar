# Dr. Maya - Medical AI Assistant

A healthcare-focused virtual assistant with a human touch that can:

- Interact with users using natural, empathetic voice or text conversations
- Provide information about common medical conditions with professional medical knowledge
- Suggest appropriate remedies and medications with proper dosage information
- Book appointments with specialists based on symptoms
- Track patient vitals and medications

## Quick Start

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (optional but recommended for full functionality)
4. Run the assistant:
   - Text-only mode: `python main.py --text`
   - Voice mode: `python main.py`
   - Test mode: `python main.py --test`

## Project Structure

- **main.py** - Entry point for the application
- **text_mode.py** - Text-based interface
- **medical_assistant.py** - Core assistant functionality
- **appointment_scheduler.py** - Appointment booking and management
- **medication_manager.py** - Medication tracking and recommendations
- **patient_vitals.py** - Patient health metrics tracking and analysis
- **conversation_flow.py** - Structured conversation management

## Setup Instructions

### Prerequisites

- Python 3.8+ installed
- pip package manager

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd medical-assistant
   ```

2. **Create a virtual environment (recommended)**:

   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy `env.sample` to a new file named `.env`
   - Fill in your API keys (optional, see "API Integration" below)

### Running the Application

There are three ways to run the application:

1. **Text Mode** (no speech capabilities required):

   ```bash
   python main.py --text
   ```

2. **Voice Mode** (requires speech services):

   ```bash
   python main.py
   ```

3. **Test Mode** (runs a predefined test sequence):
   ```bash
   python main.py --test
   ```

## API Integration

For full functionality, you can set up these APIs (optional):

### OpenAI API

For natural language processing:

1. Create an account at https://platform.openai.com
2. Generate an API key
3. Add to your `.env` file: `OPENAI_API_KEY=your_key_here`

### Azure Speech Service

For voice capabilities:

1. Create a free Azure account at https://azure.microsoft.com
2. Create a Speech Service resource
3. Add to your `.env` file:
   ```
   AZURE_SPEECH_KEY=your_key_here
   AZURE_SPEECH_REGION=your_region_here
   ```

## Features

### Medical Assistant

- Natural conversation with medical context
- Symptom assessment and preliminary guidance
- Emergency detection and appropriate response

### Appointment Management

- Schedule appointments with specialists
- Cancel or reschedule appointments
- View available time slots

### Medication Management

- Track patient medications
- Check for potential drug interactions
- Provide medication information and suggestions

### Vitals Tracking

- Record and monitor vital signs
- Analyze trends and detect concerns
- Compare with normal ranges

## Usage Examples

### Text Mode Interaction

```
Dr. Maya: Hello, I'm Dr. Maya, your AI medical assistant. How can I help you today?
You: I've been having headaches for the past three days
Dr. Maya: I'm sorry to hear about your headaches. Could you tell me more about them? Are they constant or intermittent? On a scale of 1-10, how would you rate the pain? Do you have any other symptoms accompanying the headaches?
```

### Scheduling an Appointment

```
You: I'd like to schedule an appointment
Dr. Maya: I'd be happy to help you schedule an appointment. Could you please tell me your name and what day and time would work best for you?
You: My name is John and I'm available tomorrow morning
```

## Troubleshooting

- **No voice output**: Make sure Azure Speech API keys are set or the system will fall back to text mode
- **API errors**: Check internet connection and API key validity
- **Missing files**: Ensure all project files are in the correct structure

## Development

To extend this project:

1. Fork the repository
2. Make your changes
3. Run the tests: `python -m unittest discover`
4. Submit a pull request

## Disclaimer

This application is for educational purposes only and not for actual medical use. All medical information and advice provided are simulated and should not replace consultation with real healthcare professionals.
