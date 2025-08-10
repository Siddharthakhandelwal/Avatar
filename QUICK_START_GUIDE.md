# Quick Start Guide 🚀

**Get MedyBot running in just 5 minutes!** This guide is designed for absolute beginners who want to start chatting with Nirog, your medical assistant, as quickly as possible.

---

## ⏱️ Before You Begin (2 minutes)

### ✅ Pre-Installation Checklist

Make sure you have these ready:

- [ ] **A computer** (Windows, Mac, or Linux)
- [ ] **Internet connection** (stable and working)
- [ ] **15 minutes of free time** (for first-time setup)
- [ ] **A Google account** (for the free API key)

### 🖥️ Check if Python is Installed

**Windows:**
1. Press `Windows + R`, type `cmd`, press Enter
2. Type: `python --version`
3. If you see "Python 3.7" or higher → ✅ You're good!
4. If you see "command not found" → Download Python from [python.org](https://python.org)

**Mac:**
1. Press `Cmd + Space`, type `terminal`, press Enter
2. Type: `python3 --version`
3. If you see "Python 3.7" or higher → ✅ You're good!
4. If not installed → Download from [python.org](https://python.org)

**Linux:**
1. Open Terminal (Ctrl + Alt + T)
2. Type: `python3 --version`
3. If you see "Python 3.7" or higher → ✅ You're good!
4. If not: `sudo apt install python3 python3-pip`

---

## 🚀 5-Minute Setup Guide

### Step 1: Download MedyBot (1 minute)

**Option A: Download ZIP (Easiest)**
1. Download the MedyBot ZIP file
2. Extract it to your Desktop or Documents folder
3. Remember where you saved it!

**Option B: Use Git (If you have it)**
```bash
git clone <repository-url>
cd Avatar
```

### Step 2: Open Terminal/Command Prompt (30 seconds)

**Windows:**
- Press `Windows + R`
- Type `cmd` and press Enter
- Navigate to your MedyBot folder: `cd Desktop\Avatar` (adjust path as needed)

**Mac:**
- Press `Cmd + Space`
- Type `terminal` and press Enter
- Navigate to your folder: `cd Desktop/Avatar` (adjust path as needed)

**Linux:**
- Press `Ctrl + Alt + T`
- Navigate to your folder: `cd Desktop/Avatar` (adjust path as needed)

### Step 3: Install Required Packages (1 minute)

Copy and paste this command:

**Windows:**
```cmd
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
pip3 install -r requirements.txt
```

You should see something like:
```
Collecting google-generativeai
Collecting python-dotenv
Installing collected packages...
Successfully installed google-generativeai-0.x.x python-dotenv-1.x.x
```

✅ **Success!** If you see "Successfully installed" → Continue to Step 4
❌ **Error?** → Check the [Troubleshooting](#-troubleshooting) section below

### Step 4: Get Your Free API Key (2 minutes)

1. **Visit Google AI Studio**
   - Go to: [https://aistudio.google.com/](https://aistudio.google.com/)
   - Sign in with your Google account

![Screenshot placeholder: Google AI Studio homepage with sign-in button highlighted]

2. **Create Your API Key**
   - Click "Get API Key" in the left sidebar
   - Click "Create API Key" button
   - Choose "Create API key in new project"

![Screenshot placeholder: API key creation dialog with "Create API key in new project" option highlighted]

3. **Copy Your Key**
   - Copy the generated key (starts with "AIza...")
   - **Important:** Keep this key private and secure!

![Screenshot placeholder: Generated API key with copy button highlighted]

### Step 5: Set Up Your API Key (30 seconds)

**Method 1: Create .env File (Recommended)**

1. In your MedyBot folder, create a new file called `.env`
2. Open it with any text editor (Notepad, TextEdit, etc.)
3. Add this line (replace with your actual key):
```
GEMINI_API_KEY=AIza...your-actual-key-here
```
4. Save the file

**Method 2: Environment Variable (Alternative)**

**Windows:**
```cmd
set GEMINI_API_KEY=AIza...your-actual-key-here
```

**Mac/Linux:**
```bash
export GEMINI_API_KEY=AIza...your-actual-key-here
```

### Step 6: Start MedyBot! (10 seconds)

In your terminal/command prompt, type:

```bash
python chat_bot.py
```

You should see:
```
👩‍⚕️ MedyBot: Hello! I am your medical assistant. How can I help you today?
You: 
```

🎉 **Congratulations!** MedyBot is now running!

---

## 💬 Your First Conversation

Try these example questions to get started:

### Example 1: Basic Health Question
```
You: I have a mild headache. What should I do?

👩‍⚕️ MedyBot: I understand you have a mild headache. Here's what I recommend:

💊 **Immediate Relief:**
- Take Paracetamol 500mg (1-2 tablets)
- Rest in a quiet, dark room
- Stay hydrated with water

⚠️ **When to see a doctor:**
- If headache becomes severe
- If it lasts more than 24 hours
- If you have fever or neck stiffness

Would you like me to help you book an appointment with a doctor?
```

### Example 2: Appointment Booking
```
You: I need to book an appointment with a heart doctor

👩‍⚕️ MedyBot: I can help you with that! For heart-related concerns, I recommend Dr. Sarah Johnson, our experienced Cardiologist in Vrindavan.

What date and time would work best for you?

You: Tomorrow at 3 PM for chest pain

👩‍⚕️ MedyBot: I've prepared your appointment details:

**Date:** Tomorrow (August 2, 2025)
**Time:** 3:00 PM
**Cause:** Chest pain
**Doctor:** Dr. Sarah Johnson (Cardiologist) — Vrindavan

⚠️ **Important:** For chest pain, if symptoms worsen or you have difficulty breathing, seek immediate emergency care.
```

### Example 3: Page Navigation
```
You: Take me to the appointment page

👩‍⚕️ MedyBot: page: appointment-booking

I'm directing you to the appointment booking page. Would you like me to help you choose the right specialist for your needs?
```

---

## 🛑 What to Do If Something Goes Wrong

### Problem: "pip is not recognized"
**Quick Fix:**
```bash
# Try this instead:
python -m pip install -r requirements.txt
```

### Problem: "API key not found"
**Quick Fix:**
1. Check that your `.env` file is in the same folder as `chat_bot.py`
2. Make sure there are no extra spaces in your API key
3. Restart your terminal and try again

### Problem: "Invalid API key"
**Quick Fix:**
1. Go back to [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Replace the old key in your `.env` file

### Problem: MedyBot doesn't respond
**Quick Fix:**
1. Check your internet connection
2. Wait 10 seconds and try a shorter message
3. Restart MedyBot by pressing `Ctrl+C` and running `python chat_bot.py` again

### Problem: "Permission denied" (Mac/Linux)
**Quick Fix:**
```bash
# Try with pip3:
pip3 install -r requirements.txt

# Or with user installation:
pip3 install --user -r requirements.txt
```

---

## ✅ Success! What's Next?

### 🎯 Now You Can:
- Ask Nirog any health-related questions
- Get medication suggestions with dosages
- Book appointments with 5 specialist doctors
- Navigate to different pages
- Have context-aware conversations

### 🔄 How to Use MedyBot Again:
1. Open terminal/command prompt
2. Navigate to your MedyBot folder: `cd path/to/Avatar`
3. Run: `python chat_bot.py`
4. Start chatting!

### 📚 Learn More:
- **Detailed Features**: Read [`USER_MANUAL.md`](USER_MANUAL.md)
- **Common Questions**: Check [`FAQ.md`](FAQ.md)
- **Full Documentation**: See [`README.md`](README.md)
- **Technical Details**: Review [`ARCHITECTURE.md`](ARCHITECTURE.md)

### 🛡️ Important Safety Reminders:
- **Medical Emergencies**: Call emergency services (102/108 in India)
- **Serious Conditions**: Always consult real doctors
- **Privacy**: Your conversations aren't stored permanently
- **API Key**: Keep your key secure and private

---

## 🎉 Congratulations!

You've successfully set up MedyBot and had your first conversation with Nirog! 

### Quick Commands to Remember:
- **Start MedyBot**: `python chat_bot.py`
- **Exit conversation**: Type `exit`, `quit`, or `bye`
- **Get help**: Ask Nirog directly or check [`FAQ.md`](FAQ.md)

### Pro Tips:
- Be specific about your symptoms
- Mention your location for doctor recommendations
- Ask follow-up questions - Nirog remembers your conversation
- Don't hesitate to ask for clarifications

---

## 📞 Need Help?

If you're still having trouble:

1. **Check [`FAQ.md`](FAQ.md)** - Most common issues are covered there
2. **Review error messages** - They often contain helpful clues
3. **Try the troubleshooting steps** in [`README.md`](README.md#-troubleshooting)
4. **Start fresh** - Sometimes restarting your terminal helps

---

**🏥 Ready to chat with Nirog? Run `python chat_bot.py` and start your conversation!**

---

*Remember: MedyBot is for educational purposes only. Always consult qualified healthcare professionals for medical advice.*

**Last Updated**: August 2025 | **Version**: 2.0 | **Setup Time**: ~5 minutes