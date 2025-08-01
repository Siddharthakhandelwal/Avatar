# Frequently Asked Questions (FAQ) 🤔

Welcome to the MedyBot FAQ! Here you'll find answers to the most common questions about Nirog, your friendly medical assistant from Delhi.

---

## 🚀 Getting Started

### Q: What is MedyBot?
**A:** MedyBot is an intelligent medical assistant chatbot powered by Google's Gemini AI. It features Nirog, a friendly assistant from Delhi who can provide general health advice, suggest over-the-counter medications, and help you book appointments with qualified doctors.

### Q: Is MedyBot free to use?
**A:** Yes! MedyBot is completely free to use. You only need a free Google Gemini API key, which you can obtain at no cost from Google AI Studio.

### Q: Do I need to be tech-savvy to use MedyBot?
**A:** Not at all! While you need basic command line knowledge for setup, we provide step-by-step guides. Once running, you simply type your questions in plain English.

---

## 🔧 Installation & Setup

### Q: What do I need to install before using MedyBot?
**A:** You need:
- Python 3.7 or higher
- A stable internet connection
- A free Google Gemini API key
- About 50MB of free storage space

### Q: I'm getting "pip is not recognized" error. What should I do?
**A:** This usually means Python isn't properly added to your system PATH. Try:
- **Windows**: Use `python -m pip install -r requirements.txt`
- **macOS/Linux**: Use `pip3 install -r requirements.txt`
- Or reinstall Python and check "Add to PATH" during installation

### Q: How do I get a Google Gemini API key?
**A:** Follow these steps:
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" → "Create API Key"
4. Choose "Create API key in new project"
5. Copy the key (starts with "AIza...")
6. Keep it secure and never share it publicly!

### Q: Where do I put my API key?
**A:** You have two options:
1. **Environment Variable** (recommended):
   - Windows: `set GEMINI_API_KEY=your-key-here`
   - macOS/Linux: `export GEMINI_API_KEY=your-key-here`
2. **Create a .env file** in your project folder with: `GEMINI_API_KEY=your-key-here`

### Q: I'm getting "API key not found" error. Help!
**A:** Check these common issues:
- Ensure your `.env` file is in the same folder as `chat_bot.py`
- Verify your API key starts with "AIza..."
- Restart your terminal after setting environment variables
- Make sure there are no extra spaces in your API key

---

## 💬 Using Nirog

### Q: What can Nirog help me with?
**A:** Nirog can assist with:
- General health questions and advice
- Over-the-counter medication suggestions with dosages
- Symptom guidance and when to seek professional help
- Booking appointments with specialist doctors
- Navigating to different pages or sections
- Basic medical education and information

### Q: What CAN'T Nirog do?
**A:** Nirog cannot and will not:
- Provide medical diagnoses
- Prescribe prescription medications
- Replace professional medical consultation
- Handle medical emergencies (call emergency services!)
- Store your personal medical information

### Q: How do I start a conversation with Nirog?
**A:** Simply run `python chat_bot.py` in your terminal, and Nirog will greet you. Then type your health questions naturally, like:
- "I have a headache, what should I do?"
- "Can you help me book an appointment?"
- "What medicine is good for a cold?"

### Q: Does Nirog remember our previous conversations?
**A:** Yes, during your current session, Nirog remembers everything you've discussed. However, when you close the program and restart it, Nirog starts fresh with no memory of previous sessions.

### Q: How do I end a conversation?
**A:** Type any of these commands: `exit`, `quit`, or `bye`

---

## 👨‍⚕️ Doctor Appointments

### Q: Which doctors are available for appointments?
**A:** MedyBot can help you book with these specialists:
- **Dr. Sarah Johnson** - Cardiologist (Heart) in Vrindavan
- **Dr. Michael Chen** - General Physician in Gaziabad  
- **Dr. Priya Patel** - Pediatrician (Children) in Delhi
- **Dr. Robert Wilson** - Dermatologist (Skin) in Gurgaon
- **Dr. Lisa Garcia** - Neurologist (Brain/Nerves) in Mumbai

### Q: How do I book an appointment?
**A:** Just tell Nirog you want to book an appointment. The process is:
1. Say "I need to book an appointment" or similar
2. Mention your city or preferred doctor
3. Provide your preferred date and time
4. Explain the reason for your visit
5. Nirog will format your appointment details

### Q: Are these real doctors?
**A:** The appointment booking feature is a demonstration of the system's capabilities. In a real implementation, these would connect to actual medical practices. Always verify doctor credentials and contact information independently.

### Q: Can I cancel or reschedule appointments through Nirog?
**A:** Currently, Nirog helps format appointment requests. For changes, you would need to contact the medical practice directly.

---

## 🔧 Technical Questions

### Q: Why is Nirog responding slowly?
**A:** Slow responses can be caused by:
- Slow internet connection
- Google API rate limits (wait a few seconds between messages)
- Long conversation history (restart for a fresh session)
- High API usage (check your Google Cloud quotas)

### Q: I'm getting "Invalid API key" errors. What's wrong?
**A:** Try these solutions:
1. Generate a new API key from Google AI Studio
2. Check if you've exceeded your free tier limits
3. Verify the API key is from the correct Google Cloud project
4. Ensure there are no typos in your API key

### Q: Can I use MedyBot offline?
**A:** No, MedyBot requires an internet connection to communicate with Google's Gemini API. All the AI processing happens in the cloud.

### Q: What programming language is MedyBot built with?
**A:** MedyBot is built with Python and uses Google's Generative AI library to communicate with the Gemini API.

### Q: Can I modify MedyBot for my own use?
**A:** Yes! The code is available for educational purposes. You can modify the instructions, add new features, or integrate it into other applications. Just remember to follow medical ethics and safety guidelines.

---

## 🛡️ Safety & Medical Questions

### Q: Can I trust Nirog's medical advice?
**A:** Nirog provides general health information and education, but it's NOT a substitute for professional medical advice. Always consult qualified healthcare professionals for:
- Serious medical conditions
- Prescription medications
- Medical diagnoses
- Emergency situations

### Q: What should I do in a medical emergency?
**A:** **Never use MedyBot for emergencies!** Instead:
- **India**: Call 102 (Ambulance) or 108 (Emergency Response)
- **International**: Contact your local emergency services
- Go to the nearest emergency room immediately

### Q: Is my conversation data stored anywhere?
**A:** No! Your conversations with Nirog are:
- Kept only in memory during your session
- Completely deleted when you close the program
- Never stored permanently on any server
- Not shared with third parties

### Q: Can Nirog diagnose my condition?
**A:** Absolutely not. Nirog can:
- Provide general health information
- Suggest when to see a doctor
- Recommend over-the-counter remedies
- Help you understand symptoms

But only licensed medical professionals can provide diagnoses.

---

## 🌍 Customization & Configuration

### Q: Can I change Nirog's personality or responses?
**A:** Yes! Advanced users can modify the `instructions` variable in [`chat_bot.py`](chat_bot.py:12-38) to customize:
- Nirog's personality and tone
- Available doctors and locations
- Response formats
- Medical guidelines

### Q: Can I add more doctors to the system?
**A:** Yes! Edit the doctor list in the instructions section of [`chat_bot.py`](chat_bot.py:28-33). Follow the same format: `Dr. Name (Specialty) — Location`

### Q: Can I make MedyBot work in other languages?
**A:** The Google Gemini API supports multiple languages. You could modify the instructions to respond in your preferred language, though the current setup is optimized for English.

### Q: Can I integrate MedyBot into a website or mobile app?
**A:** Yes! The core functionality can be adapted for web or mobile interfaces. You'd need to replace the command-line interface with web forms or mobile UI components.

---

## 🔍 Troubleshooting

### Q: MedyBot starts but doesn't respond to my messages. What's wrong?
**A:** Check these common issues:
1. Verify your internet connection
2. Confirm your API key is valid and properly set
3. Check if you've exceeded API rate limits
4. Look for error messages in the terminal
5. Try restarting the program

### Q: I'm getting "Module not found" errors. How do I fix this?
**A:** This usually means dependencies aren't installed properly:
```bash
# Uninstall and reinstall dependencies
pip uninstall google-generativeai python-dotenv
pip install -r requirements.txt
```

### Q: The program crashes when I type certain messages. Why?
**A:** This could be due to:
- Special characters in your input
- Very long messages
- Network connectivity issues
- API rate limiting

Try shorter, simpler messages and ensure stable internet connection.

### Q: How do I update MedyBot to the latest version?
**A:** Currently, you would need to download the latest version of the files. For dependencies:
```bash
pip install --upgrade google-generativeai python-dotenv
```

---

## 📞 Getting More Help

### Q: Where can I find more detailed documentation?
**A:** Check these files in your MedyBot folder:
- [`README.md`](README.md) - Comprehensive setup and usage guide
- [`USER_MANUAL.md`](USER_MANUAL.md) - Detailed feature walkthrough
- [`QUICK_START_GUIDE.md`](QUICK_START_GUIDE.md) - 5-minute setup guide
- [`ARCHITECTURE.md`](ARCHITECTURE.md) - Technical architecture details

### Q: What if my question isn't answered here?
**A:** Try these steps:
1. Check the troubleshooting section in [`README.md`](README.md#-troubleshooting)
2. Review error messages carefully for clues
3. Test individual components (Python, internet, API key)
4. Search online for specific error messages

### Q: Can I contribute to improving MedyBot?
**A:** Absolutely! Contributions are welcome, especially:
- Bug fixes and improvements
- Better error handling
- Additional safety features
- Documentation improvements
- New medical guidelines

Just remember to maintain medical ethics and safety standards.

---

## ⚠️ Important Reminders

- **Medical Emergencies**: Always call emergency services, never rely on MedyBot
- **Professional Consultation**: Consult real doctors for serious medical conditions
- **API Key Security**: Never share your API key publicly
- **Regular Updates**: Keep your dependencies updated for security
- **Backup Important Data**: Though MedyBot doesn't store data, backup your customizations

---

*Need immediate medical help? Don't use MedyBot - contact emergency services or visit your nearest hospital immediately.*

**Last Updated**: January 2025 | **Version**: 2.0