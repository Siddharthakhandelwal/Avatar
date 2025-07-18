# MedyBot: Medical Assistant Chatbot

MedyBot is a simple command-line medical assistant chatbot powered by Google Gemini. It can answer health questions, suggest over-the-counter medicines, and provide general advice, but always reminds users to consult a real doctor for serious issues.

## Features
- Friendly, empathetic responses
- General medicine suggestions (with disclaimers)
- Reminds users to consult a real doctor
- Maintains conversation context
- Uses Google Gemini API for responses

## Requirements
- Python 3.7+
- [google-generativeai Python package](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation
1. Clone this repository or download the script.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup
1. Get your Gemini API key from Google AI Studio or your Google Cloud Console.
2. Set your API key as an environment variable:
   - **Linux/Mac:**
     ```bash
     export GEMINI_API_KEY=your-key-here
     ```
   - **Windows CMD:**
     ```cmd
     set GEMINI_API_KEY=your-key-here
     ```
   - **Windows PowerShell:**
     ```powershell
     $env:GEMINI_API_KEY="your-key-here"
     ```
   Or, create a `.env` file in the project directory with:
   ```
   GEMINI_API_KEY=your-key-here
   ```

## Usage
Run the chatbot with:
```bash
python chat_bot.py
```

Type your questions and MedyBot will respond. Type `exit`, `quit`, or `bye` to end the conversation.

## How it works
- The chatbot maintains a conversation history in memory, sending the full history to the Gemini model for context-aware responses.
- The assistant is instructed to act as Dr. Maya, the medical assistant at Wellness Medical Center, and never refer to itself as an AI.
- The bot can help book appointments with a list of available doctors, and always reminds users to consult a real doctor for serious issues.

## Disclaimer
This chatbot is for educational/demo purposes only and should not be used as a substitute for professional medical advice. 