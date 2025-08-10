# MedyBot: Your Personal Medical Assistant 🏥

**Meet Nirog** - Your friendly medical assistant from Delhi, India, powered by Google's advanced Gemini AI. MedyBot is an intelligent chatbot designed to provide general health advice, suggest over-the-counter medications, help book appointments with qualified doctors, and guide you through basic medical queries - all while maintaining a warm, empathetic conversation.

> **⚠️ Important Medical Disclaimer**: MedyBot is designed for educational and informational purposes only. It does not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for serious medical conditions.

---

## STATUS OF THE PROJECT
This project is currently in the **alpha** stage of development. This means that while the core features are implemented and functional, there may be bugs or incomplete features. The project is not yet ready for production use.

---

## 🌟 Features

### 🤖 **Intelligent Medical Assistant**
- **Personalized Health Advice**: Get tailored responses to your health-related questions
- **Medication Suggestions**: Receive recommendations for over-the-counter medicines with proper dosage information
- **Symptom Guidance**: Understand your symptoms and when to seek professional help

### 📅 **Appointment Booking System**
- **Doctor Matching**: Find the right specialist based on your location and medical needs
- **Easy Scheduling**: Book appointments with a simple conversation flow
- **Multi-City Coverage**: Access to doctors across Delhi, Mumbai, Gurgaon, Gaziabad, and Vrindavan

### 🧠 **Smart Conversation Features**
- **Context Awareness**: Remembers your conversation history for more relevant responses
- **Page Navigation**: Can guide you to different sections or pages as needed
- **Real-time Timestamps**: All interactions are timestamped for better tracking

### 🛡️ **Safety & Reliability**
- **Medical Disclaimers**: Always reminds users to consult real doctors for serious conditions
- **Ethical Guidelines**: Follows strict medical ethics and doesn't provide diagnoses
- **Privacy Focused**: No permanent data storage - conversations exist only during your session

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.7 or higher** installed on your system
- **Internet connection** for API communication
- **Google Gemini API key** (free to obtain)
- **Basic command line knowledge** (we'll guide you through it!)

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: Minimum 2GB available
- **Storage**: 50MB free space
- **Network**: Stable internet connection

---

## 🚀 Installation Guide

### Step 1: Download the Project
```bash
# Option 1: Clone with Git (if you have Git installed)
git clone <repository-url>
cd Avatar

# Option 2: Download ZIP file and extract it
# Then navigate to the extracted folder in your terminal/command prompt
```

### Step 2: Install Python Dependencies

#### For Windows:
```cmd
# Open Command Prompt as Administrator
pip install -r requirements.txt
```

#### For macOS:
```bash
# Open Terminal
pip3 install -r requirements.txt
```

#### For Linux (Ubuntu/Debian):
```bash
# Open Terminal
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python --version  # Should show Python 3.7+
pip list | grep google-generativeai  # Should show the installed package
```

---

## 🔑 API Key Setup

To use MedyBot, you need a free Google Gemini API key. Follow these detailed steps:

### Getting Your API Key

1. **Visit Google AI Studio**
   - Go to [https://aistudio.google.com/](https://aistudio.google.com/)
   - Sign in with your Google account

![Google AI Studio Homepage](images/google-ai-studio-homepage.png)

2. **Create API Key**
   - Click on "Get API Key" in the left sidebar
   - Click "Create API Key"
   - Choose "Create API key in new project" (recommended)

![API Key Creation](images/api-key-creation.png)

3. **Copy Your API Key**
   - Copy the generated API key (it starts with "AIza...")
   - **Keep this key secure and never share it publicly!**

![API Key Generated](images/api-key-generated.png)

### Setting Up Your API Key

Choose one of the following methods:

#### Method 1: Environment Variable (Recommended)

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**macOS/Linux:**
```bash
export GEMINI_API_KEY=your-api-key-here
```

#### Method 2: .env File (Persistent)
1. Create a file named `.env` in your project folder
2. Add this line to the file:
```
GEMINI_API_KEY=your-api-key-here
```
3. Save the file

![Environment File Setup](images/env-file-setup.png)

---

## ⚡ Quick Start

Once you have everything installed and your API key configured:

```bash
# Navigate to your project folder
cd path/to/your/Avatar/folder

# Run MedyBot
python chat_bot.py
```

You should see:
```
👩‍⚕️ MedyBot: Hello! I am your medical assistant. How can I help you today?
You: 
```

**That's it!** You're now ready to chat with Nirog, your medical assistant.

---

## 💬 Usage Guide

### Starting a Conversation
Simply type your health-related questions or concerns. Nirog will respond with helpful advice, medication suggestions, or guide you to appropriate medical care.

### Basic Commands
- **Ask health questions**: "I have a headache, what should I do?"
- **Request appointments**: "I need to book an appointment with a cardiologist"
- **Navigate pages**: "Take me to the appointment page"
- **End conversation**: Type `exit`, `quit`, or `bye`

### Conversation Tips
- **Be specific**: Describe your symptoms clearly
- **Mention your location**: This helps with doctor recommendations
- **Ask follow-up questions**: Nirog remembers your conversation context
- **Request clarifications**: Don't hesitate to ask for more details

---

## 👨‍⚕️ Available Doctors

MedyBot can help you book appointments with these qualified medical professionals:

| Doctor | Specialty | Location | Availability |
|--------|-----------|----------|--------------|
| **Dr. Sarah Johnson** | Cardiologist (Heart Specialist) | Vrindavan | Mon-Fri, 9 AM - 5 PM |
| **Dr. Michael Chen** | General Physician | Gaziabad | Mon-Sat, 8 AM - 6 PM |
| **Dr. Priya Patel** | Pediatrician (Child Specialist) | Delhi | Tue-Sun, 10 AM - 4 PM |
| **Dr. Robert Wilson** | Dermatologist (Skin Specialist) | Gurgaon | Mon-Fri, 11 AM - 7 PM |
| **Dr. Lisa Garcia** | Neurologist (Brain & Nerve Specialist) | Mumbai | Wed-Sun, 9 AM - 3 PM |

### Appointment Booking Process
1. Tell Nirog you want to book an appointment
2. Mention your city or preferred doctor
3. Provide your preferred date and time
4. Explain the reason for your visit
5. Nirog will format your appointment details

---

## 📝 Example Conversations

### Example 1: General Health Query
```
You: I have a mild fever and headache. What should I do?

👩‍⚕️ MedyBot: I understand you're feeling unwell with fever and headache. Here's what I recommend:

💊 **Immediate Relief:**
- Take Paracetamol 500mg every 6-8 hours (max 4 doses/day)
- Rest and stay hydrated with plenty of fluids
- Use a cool compress on your forehead

⚠️ **When to see a doctor:**
- If fever exceeds 102°F (39°C)
- If symptoms persist for more than 3 days
- If you develop severe headache, neck stiffness, or difficulty breathing

Would you like me to help you book an appointment with a doctor in your area?
```

### Example 2: Appointment Booking
```
You: I need to see a heart doctor in Delhi area

👩‍⚕️ MedyBot: I can help you with that! For heart-related concerns, I recommend Dr. Sarah Johnson, our experienced Cardiologist. She's located in Vrindavan, which is close to Delhi.

What date and time would work best for you?

You: Tomorrow at 2 PM, I have chest pain occasionally

👩‍⚕️ MedyBot: I've scheduled your appointment. Here are the details:

**Date:** Tomorrow (January 2, 2025)
**Time:** 2:00 PM  
**Cause:** Occasional chest pain
**Doctor:** Dr. Sarah Johnson (Cardiologist) — Vrindavan

⚠️ **Important:** Given that you're experiencing chest pain, if it becomes severe or you have difficulty breathing, please seek immediate emergency care. Don't wait for the appointment.
```

### Example 3: Page Navigation
```
You: Can you take me to the appointment booking page?

👩‍⚕️ MedyBot: page: appointment-booking

I'm directing you to the appointment booking page where you can schedule a visit with one of our doctors. Would you like me to help you choose the right specialist for your needs?
```

![Example Conversations](images/example-conversations.png)

---

## ⚙️ Dynamic Variables & Features

### Timestamp Integration
MedyBot automatically includes timestamps in conversations to provide context-aware responses:
- **Current time tracking**: Every message includes the current date and time
- **Appointment scheduling**: Uses real-time information for booking
- **Session management**: Tracks conversation duration

### Environment Variables
The system uses several environment variables for configuration:

| Variable | Purpose | Required |
|----------|---------|----------|
| `GEMINI_API_KEY` | Google Gemini API authentication | Yes |
| `PYTHONPATH` | Python module path (auto-configured) | No |

### Conversation Context
- **Memory retention**: Remembers entire conversation during session
- **Context awareness**: Responses build on previous interactions
- **Session isolation**: Each new session starts fresh

---

## 🔧 Troubleshooting

### Common Installation Issues

#### Problem: "pip is not recognized"
**Solution:**
```bash
# Windows: Add Python to PATH or use
python -m pip install -r requirements.txt

# macOS/Linux: Use pip3
pip3 install -r requirements.txt
```

#### Problem: "Permission denied" on Linux/macOS
**Solution:**
```bash
# Use sudo for system-wide installation
sudo pip3 install -r requirements.txt

# Or install for current user only
pip3 install --user -r requirements.txt
```

### API Key Issues

#### Problem: "API key not found" error
**Solutions:**
1. **Check your .env file**: Ensure it's in the same folder as `chat_bot.py`
2. **Verify API key format**: Should start with "AIza..."
3. **Restart terminal**: After setting environment variables
4. **Check file permissions**: Ensure `.env` file is readable

#### Problem: "Invalid API key" error
**Solutions:**
1. **Generate new key**: Visit Google AI Studio and create a fresh API key
2. **Check quotas**: Ensure you haven't exceeded free tier limits
3. **Verify project**: Make sure API key is from the correct Google Cloud project

### Runtime Issues

#### Problem: Chatbot doesn't respond
**Solutions:**
1. **Check internet connection**: API requires stable internet
2. **Verify API key**: Test with a simple request
3. **Check Python version**: Must be 3.7 or higher
4. **Review error messages**: Look for specific error details

#### Problem: "Module not found" errors
**Solution:**
```bash
# Reinstall dependencies
pip uninstall google-generativeai python-dotenv
pip install -r requirements.txt
```

### Performance Issues

#### Problem: Slow responses
**Causes & Solutions:**
- **Slow internet**: Check your connection speed
- **API rate limits**: Wait a few seconds between requests
- **Large conversation history**: Restart for fresh session

#### Problem: Memory usage
**Solution:**
- Restart the chatbot periodically for long conversations
- The system automatically manages memory during sessions

### Getting Help

If you encounter issues not covered here:

1. **Check error messages**: Read the full error output
2. **Verify setup**: Ensure all installation steps were completed
3. **Test components**: Try running Python and importing modules separately
4. **Update dependencies**: Ensure you have the latest versions

```bash
# Update all packages
pip install --upgrade google-generativeai python-dotenv
```

---

## 🛡️ Safety & Medical Disclaimers

### Medical Disclaimer
**MedyBot is NOT a substitute for professional medical advice, diagnosis, or treatment.**

- **Educational Purpose**: This chatbot is designed for educational and informational purposes only
- **No Medical Diagnosis**: Nirog cannot and does not provide medical diagnoses
- **No Prescriptions**: Only suggests over-the-counter medications, never prescription drugs
- **Emergency Situations**: For medical emergencies, call your local emergency services immediately

### Usage Guidelines

#### ✅ **Appropriate Use:**
- General health information and education
- Over-the-counter medication guidance
- Basic symptom understanding
- Appointment booking assistance
- Health-related questions and concerns

#### ❌ **Inappropriate Use:**
- Replacing professional medical consultation
- Self-diagnosing serious medical conditions
- Managing chronic diseases without doctor supervision
- Emergency medical situations
- Prescription medication decisions

### Privacy & Data Protection

- **No Data Storage**: Conversations are not permanently stored
- **Session-Based**: All data is cleared when you close the application
- **API Security**: Communications with Google Gemini are encrypted
- **Local Processing**: Your conversations stay on your device

### Liability Limitations

- Users are responsible for their own medical decisions
- Always consult healthcare professionals for medical advice
- MedyBot developers are not liable for medical outcomes
- Use of this software indicates acceptance of these terms

---

## 🏗️ Technical Architecture

### System Overview
MedyBot is built using a simple yet effective architecture:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│   Chat Bot       │───▶│  Google Gemini  │
│  (Command Line) │    │  (chat_bot.py)   │    │      API        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │ Conversation     │    │   AI Response   │
                       │ History Manager  │    │   Generation    │
                       └──────────────────┘    └─────────────────┘
```

### Core Components

#### 1. **Main Application** ([`chat_bot.py`](chat_bot.py))
- **Purpose**: Entry point and conversation management
- **Functions**: User input handling, API communication, response formatting
- **Model**: Uses `gemini-1.5-pro` for advanced reasoning

#### 2. **Conversation Manager**
- **Context Retention**: Maintains full conversation history
- **Message Formatting**: Structures data for API consumption
- **Session Management**: Handles conversation lifecycle

#### 3. **API Integration**
- **Google Gemini**: Advanced language model for responses
- **Authentication**: Secure API key management
- **Error Handling**: Graceful failure management

#### 4. **Instructions System**
- **Persona Definition**: Establishes Nirog's character and capabilities
- **Medical Guidelines**: Ensures appropriate medical advice boundaries
- **Response Formatting**: Defines output structure for appointments and navigation

### Data Flow

1. **User Input** → Captured via command line interface
2. **Context Building** → Added to conversation history with timestamp
3. **API Request** → Sent to Google Gemini with full context
4. **AI Processing** → Gemini generates contextual response
5. **Response Display** → Formatted output shown to user
6. **History Update** → Response added to conversation context

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `google-generativeai` | Latest | Google Gemini API client |
| `python-dotenv` | Latest | Environment variable management |
| `datetime` | Built-in | Timestamp functionality |
| `os` | Built-in | Operating system interface |

### Security Features

- **API Key Protection**: Environment variable storage
- **No Data Persistence**: Memory-only conversation storage
- **Input Validation**: Safe handling of user input
- **Error Boundaries**: Graceful error handling and recovery

---

## 🤝 How to Contribute
We welcome contributions to MedyBot! Here are some ways you can help:

*   **Reporting Bugs:** If you find a bug, please open an issue on our GitHub repository. Include as much detail as possible, including steps to reproduce the bug.
*   **Suggesting Enhancements:** If you have an idea for a new feature or an improvement to an existing one, please open an issue on our GitHub repository.
*   **Pull Requests:** We welcome pull requests! Please make sure to follow the coding style and to run the tests before submitting a pull request.

## 📞 Support & Contact

### Getting Help

If you need assistance with MedyBot:

#### 🐛 **Bug Reports & Issues**
- Check the [Troubleshooting](#-troubleshooting) section first
- Verify your setup follows the installation guide
- Include error messages and system information when reporting issues

#### 💡 **Feature Requests**
- Suggest improvements or new features
- Describe your use case and expected behavior
- Consider contributing to the project

#### 📚 **Documentation**
- Review this README for comprehensive information
- Check [`ARCHITECTURE.md`](ARCHITECTURE.md) for technical details
- Refer to code comments for implementation specifics

### Medical Support

**For medical emergencies or serious health concerns:**
- **India**: Call 102 (National Ambulance Service) or 108 (Emergency Response)
- **International**: Contact your local emergency services
- **Non-emergency**: Consult with qualified healthcare professionals

### Technical Support

#### System Requirements Issues
- Ensure Python 3.7+ is installed
- Verify internet connectivity
- Check API key configuration

#### Installation Problems
- Follow platform-specific installation guides
- Use appropriate package managers (pip/pip3)
- Consider virtual environment setup

### Community & Contributions

#### Contributing to MedyBot
- Follow coding standards and documentation practices
- Test thoroughly before submitting changes
- Respect medical ethics and safety guidelines

#### Feedback & Suggestions
- Share your experience using MedyBot
- Suggest improvements for user experience
- Report any medical advice concerns

---

## 📄 License & Legal

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Software License
This project is provided for educational and demonstration purposes. Please review the license file for specific terms and conditions.

### Medical Liability
- **No Medical Liability**: Developers assume no responsibility for medical decisions
- **Educational Use Only**: Not intended for clinical or diagnostic use
- **Professional Consultation Required**: Always seek qualified medical advice

### API Usage
- **Google Gemini API**: Subject to Google's terms of service
- **Rate Limits**: Respect API usage guidelines and quotas
- **Data Privacy**: Review Google's privacy policy for API usage

---

## 🎯 Quick Reference

### Essential Commands
```bash
# Start MedyBot
python chat_bot.py

# Exit conversation
Type: exit, quit, or bye

# Check Python version
python --version

# Install dependencies
pip install -r requirements.txt
```

### Key Features Summary
- ✅ General health advice and medication suggestions
- ✅ Appointment booking with 5 specialist doctors
- ✅ Context-aware conversations with memory
- ✅ Page navigation and user guidance
- ✅ Real-time timestamp integration
- ✅ Multi-city doctor coverage (Delhi, Mumbai, Gurgaon, Gaziabad, Vrindavan)

### Important Reminders
- 🔑 **API Key Required**: Get free key from Google AI Studio
- 🏥 **Not Medical Diagnosis**: Always consult real doctors for serious conditions
- 💾 **No Data Storage**: Conversations are session-only
- 🌐 **Internet Required**: Needs stable connection for API communication

---

**Ready to get started?** Follow the [Quick Start](#-quick-start) guide and begin your conversation with Nirog, your friendly medical assistant! 🚀

---

*Last updated: January 2025 | Version: 2.0 | Powered by Google Gemini 2.5 Pro*
