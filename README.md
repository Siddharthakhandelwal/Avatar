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
3. Set up environment variables in a `.env` file (required for API functionality)
4. Run the assistant:
   - Text-only mode: `python main.py --text`
   - Voice mode: `python main.py`
   - Test mode: `python main.py --test`
   - Or use the convenience script: `python run.py`

## Project Structure

- **main.py** - Entry point for the application
- **run.py** - User-friendly launcher script with menu options
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
   git clone https://github.com/Siddharthakhandelwal/Avatar.git
   cd Avatar
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
   - Fill in your API keys (see "API Integration" below)
   - IMPORTANT: Never commit your `.env` file with real API keys to version control

### Running the Application

There are multiple ways to run the application:

1. **Using the launcher script** (recommended for first-time users):

   ```bash
   python run.py
   ```

   This will show a menu with different options and check for required dependencies.

2. **Text Mode** (no speech capabilities required):

   ```bash
   python main.py --text
   ```

3. **Voice Mode** (requires speech services):

   ```bash
   python main.py
   ```

4. **Test Mode** (runs a predefined test sequence):
   ```bash
   python main.py --test
   ```

## API Integration

The application can run with limited functionality without APIs, but for full features:

### OpenAI API (Required for best experience)

For natural language processing:

1. Create an account at https://platform.openai.com
2. Generate an API key
3. Add to your `.env` file: `OPENAI_API_KEY=your_key_here`

### Hugging Face API (Alternative option)

For a free alternative to OpenAI:

1. Create an account at https://huggingface.co
2. Generate a user access token
3. Add to your `.env` file: `HUGGINGFACE_API_KEY=your_key_here`

### Azure Speech Service (Required for voice mode)

For voice capabilities:

1. Create a free Azure account at https://azure.microsoft.com
2. Create a Speech Service resource
3. Add to your `.env` file:
   ```
   AZURE_SPEECH_KEY=your_key_here
   AZURE_SPEECH_REGION=your_region_here
   ```

## Security Notes

- Never commit API keys to version control
- The `.env` file is included in `.gitignore` to prevent accidental exposure
- If you need to share this project, use `env.sample` with placeholder values
- If you accidentally commit API keys, regenerate them immediately

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

- **API key errors**: Make sure your `.env` file is properly configured with valid API keys
- **No voice output**: Check Azure Speech API keys or use text mode with `--text` argument
- **Python package errors**: Try reinstalling with `pip install -r requirements.txt --force-reinstall`
- **Missing .env file**: Copy `env.sample` to `.env` and add your API keys
- **"Module not found" errors**: Ensure you're running the application from the project root directory

## Development

To extend this project:

1. Fork the repository
2. Make your changes
3. Run the tests: `python -m unittest discover`
4. Submit a pull request

## Disclaimer

This application is for educational purposes only and not for actual medical use. All medical information and advice provided are simulated and should not replace consultation with real healthcare professionals.
