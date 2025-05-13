# Maya - Medical Virtual Assistant

Maya is an intelligent medical virtual assistant that combines speech recognition, natural language processing, and appointment management to provide a seamless healthcare interaction experience.

## Features

- **Voice Interaction**: Real-time speech recognition and synthesis using Azure Cognitive Services.
- **Natural Language Processing**: Powered by Groq's LLM for intelligent, context-aware conversation.
- **Appointment Management**: Automated appointment scheduling and management, with Groq handling the entire appointment flow and summarizing details at the end.
- **Wake Word Detection**: Background listening for hands-free activation.
- **Conversation History**: Maintains context-aware conversations with history management and file-based saving.
- **Error Handling**: Robust error handling and graceful degradation.
- **Idle Timeout**: Automatic sleep mode after periods of inactivity.
- **Emergency Detection**: Recognizes medical emergencies and advises immediate action.
- **Date/Time Awareness**: The assistant always provides the current date and time to Groq, so relative dates like "tomorrow" are resolved accurately.

## Prerequisites

- Python 3.9+
- Azure Cognitive Services account
- Groq API key
- Required Python packages (see `requirements.txt`)

## Environment Variables

Create a `.env` file with the following variables (see `env.sample` for an example):

```
GROQ_API_KEY=your_groq_api_key
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_SPEECH_REGION=your_azure_region
SPEECH_TIMEOUT=5  # Optional, default is 5 seconds
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/maya-medical-assistant.git
   cd maya-medical-assistant
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables in `.env` file**

## Usage

### **Run the Assistant**

```bash
python siri.py
```

### **Voice Commands**

- **Wake Words:** "Hey Maya", "Hello", "Hi", "MedyCall", "Medical", "Assistant"
- **Exit Phrases:** "Goodbye", "Bye", "Exit", "Quit", "End", "Thank you", "Thanks"

## Features & Architecture

### 1. **Voice Interaction**

- Natural speech recognition (Azure)
- Text-to-speech with SSML support
- Background wake word detection

### 2. **Conversation Management**

- Context-aware responses
- Conversation history tracking
- Automatic history pruning

### 3. **Appointment Handling**

- Groq LLM handles the entire appointment conversation naturally.
- At the end of the conversation, Groq summarizes and provides appointment details if discussed.
- All relative dates (like "tomorrow") are resolved using the current date/time context.

### 4. **Emergency Detection**

- Recognizes keywords indicating a medical emergency and advises the user to call 911 or visit the ER

### 5. **Error Handling**

- Graceful degradation
- Fallback responses
- Error logging

## File Overview

- **siri.py**: Main assistant logic, robust, production-ready. Handles voice, LLM, and appointment features with background listening and conversation history. Includes emergency detection and file-based conversation/appointment saving. Always provides current date/time context to Groq.
- **try.py**: Minimal, experimental version for quick tests. Useful for debugging or prototyping.
- **requirements.txt**: Python dependencies.
- **env.sample**: Example environment variable file.
- **README.md**: This documentation.

### Data Storage

- **conversations/**: Directory where conversation histories are saved as JSON files.

## Troubleshooting

- **Missing Environment Variables:**

  - Ensure your `.env` file is present and contains all required keys. The assistant will not function without valid API keys.

- **Dependency Issues:**

  - Run `pip install -r requirements.txt` to ensure all dependencies are installed.

- **Audio Issues:**

  - Ensure your microphone is connected and accessible by the OS.
  - Azure Speech SDK must be able to access your audio hardware.

- **Appointment/Conversation Not Saved:**
  - Ensure the application has write permissions to create the `conversations/` directory.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Azure Cognitive Services for speech capabilities
- Groq for LLM integration
- Python community for various libraries and tools

**Note:**
Appointment management is now handled entirely by Groq's LLM, with details summarized at the end of the conversation. If you wish to modularize appointment management or add more structured data storage, you may create a separate module for it.
