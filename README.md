# MedyBot: Medical Assistant Chatbot

MedyBot is a simple command-line medical assistant chatbot powered by OpenAI. It can answer health questions, suggest over-the-counter medicines, and provide general advice, but always reminds users to consult a real doctor for serious issues.

## Features
- Friendly, empathetic responses
- General medicine suggestions (with disclaimers)
- Reminds users to consult a real doctor
- Maintains conversation context

## Requirements
- Python 3.7+
- [OpenAI Python package](https://pypi.org/project/openai/)

## Installation
1. Clone this repository or download the script.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup
1. Get your OpenAI API key from [OpenAI](https://platform.openai.com/account/api-keys).
2. Set your API key as an environment variable:
   - **Linux/Mac:**
     ```bash
     export OPENAI_API_KEY=your-key-here
     ```
   - **Windows CMD:**
     ```cmd
     set OPENAI_API_KEY=your-key-here
     ```
   - **Windows PowerShell:**
     ```powershell
     $env:OPENAI_API_KEY="your-key-here"
     ```

## Usage
Run the chatbot with:
```bash
python medybot.py
```

Type your questions and MedyBot will respond. Type `exit`, `quit`, or `bye` to end the conversation.

## Disclaimer
This chatbot is for educational/demo purposes only and should not be used as a substitute for professional medical advice. 