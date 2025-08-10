# MedyBot Setup Checklist ✅

**Print this page and check off each step as you complete it!**

*Your step-by-step guide to getting Nirog, your medical assistant, up and running.*

---

## 📋 Pre-Setup Requirements Checklist

**Before you begin, make sure you have:**

- [ ] **A computer** (Windows 10/11, macOS 10.14+, or Linux Ubuntu 18.04+)
- [ ] **Internet connection** (stable and working)
- [ ] **15-20 minutes** of free time for setup
- [ ] **A Google account** (for the free API key)
- [ ] **Basic willingness to follow instructions** (we'll guide you!)

---

## 🔍 System Check (2 minutes)

### Check if Python is Already Installed

**Windows Users:**
- [ ] Press `Windows + R`, type `cmd`, press Enter
- [ ] Type: `python --version` and press Enter
- [ ] **✅ SUCCESS:** You see "Python 3.7" or higher → Skip to Step 2
- [ ] **❌ NEED TO INSTALL:** You see "command not found" → Continue below

**Mac Users:**
- [ ] Press `Cmd + Space`, type `terminal`, press Enter  
- [ ] Type: `python3 --version` and press Enter
- [ ] **✅ SUCCESS:** You see "Python 3.7" or higher → Skip to Step 2
- [ ] **❌ NEED TO INSTALL:** No version shown → Continue below

**Linux Users:**
- [ ] Press `Ctrl + Alt + T` to open Terminal
- [ ] Type: `python3 --version` and press Enter
- [ ] **✅ SUCCESS:** You see "Python 3.7" or higher → Skip to Step 2
- [ ] **❌ NEED TO INSTALL:** No version shown → Continue below

### Install Python (if needed)
- [ ] Go to [python.org](https://python.org)
- [ ] Download Python 3.7 or higher for your system
- [ ] **IMPORTANT:** During installation, check "Add Python to PATH"
- [ ] Complete installation and restart your computer
- [ ] Repeat the version check above

---

## 📥 Step 1: Download MedyBot (2 minutes)

### Option A: Download ZIP File (Easiest)
- [ ] Download the MedyBot ZIP file from the provided source
- [ ] Extract/unzip it to your **Desktop** or **Documents** folder
- [ ] **Remember the folder location!** Write it here: ________________
- [ ] Rename the folder to "MedyBot" if it has a different name

### Option B: Use Git (If you have Git installed)
- [ ] Open terminal/command prompt
- [ ] Type: `git clone <repository-url>`
- [ ] Type: `cd Avatar`

---

## 💻 Step 2: Open Terminal/Command Prompt (1 minute)

**Windows:**
- [ ] Press `Windows + R`
- [ ] Type `cmd` and press Enter
- [ ] Navigate to your MedyBot folder: `cd Desktop\MedyBot` (adjust path if different)
- [ ] **SUCCESS CHECK:** Type `dir` - you should see `chat_bot.py` in the list

**Mac:**
- [ ] Press `Cmd + Space`
- [ ] Type `terminal` and press Enter
- [ ] Navigate to your folder: `cd Desktop/MedyBot` (adjust path if different)
- [ ] **SUCCESS CHECK:** Type `ls` - you should see `chat_bot.py` in the list

**Linux:**
- [ ] Press `Ctrl + Alt + T`
- [ ] Navigate to your folder: `cd Desktop/MedyBot` (adjust path if different)
- [ ] **SUCCESS CHECK:** Type `ls` - you should see `chat_bot.py` in the list

---

## 📦 Step 3: Install Required Packages (2 minutes)

### Install Dependencies

**Windows:**
- [ ] Type: `pip install -r requirements.txt`
- [ ] Press Enter and wait for installation

**Mac/Linux:**
- [ ] Type: `pip3 install -r requirements.txt`
- [ ] Press Enter and wait for installation

### Verify Installation Success
- [ ] **✅ SUCCESS:** You see "Successfully installed google-generativeai" and "python-dotenv"
- [ ] **❌ ERROR:** If you see errors, try these fixes:
  - [ ] Windows: Try `python -m pip install -r requirements.txt`
  - [ ] Mac/Linux: Try `sudo pip3 install -r requirements.txt`
  - [ ] Or try: `pip3 install --user -r requirements.txt`

---

## 🔑 Step 4: Get Your Free API Key (3 minutes)

### Visit Google AI Studio
- [ ] Open your web browser
- [ ] Go to: [https://aistudio.google.com/](https://aistudio.google.com/)
- [ ] Sign in with your Google account

### Create Your API Key
- [ ] Click "Get API Key" in the left sidebar
- [ ] Click the blue "Create API Key" button
- [ ] Choose "Create API key in new project" (recommended)
- [ ] **IMPORTANT:** Copy the generated key (starts with "AIza...")
- [ ] **Write your API key here (keep this paper safe!):**
  ```
  AIza_________________________________
  ```

---

## ⚙️ Step 5: Set Up Your API Key (2 minutes)

### Create .env File (Recommended Method)
- [ ] In your MedyBot folder, create a new file called `.env`
  - **Windows:** Right-click → New → Text Document → Rename to `.env`
  - **Mac:** Use TextEdit or any text editor
  - **Linux:** Use `nano .env` or any text editor
- [ ] Open the `.env` file with any text editor (Notepad, TextEdit, etc.)
- [ ] Add this line (replace with your actual key):
  ```
  GEMINI_API_KEY=AIza_your_actual_key_here
  ```
- [ ] **IMPORTANT:** No spaces around the = sign!
- [ ] Save the file
- [ ] **SUCCESS CHECK:** The file should be named `.env` (with the dot at the beginning)

---

## 🚀 Step 6: Start MedyBot! (1 minute)

### Launch the Application
- [ ] In your terminal/command prompt (still in the MedyBot folder)
- [ ] Type: `python chat_bot.py`
- [ ] Press Enter

### Verify Success
- [ ] **✅ SUCCESS:** You see this message:
  ```
  👩‍⚕️ MedyBot: Hello! I am your medical assistant. How can I help you today?
  You: 
  ```
- [ ] **❌ ERROR:** If you see error messages, check the troubleshooting section below

---

## 🎉 Step 7: Test Your First Conversation (2 minutes)

### Try These Test Messages
- [ ] Type: `I have a headache` and press Enter
- [ ] **SUCCESS:** Nirog responds with medical advice
- [ ] Type: `I need to book an appointment` and press Enter  
- [ ] **SUCCESS:** Nirog asks for details about the appointment
- [ ] Type: `exit` to end the conversation

### Congratulations! 
- [ ] **MedyBot is now working correctly!**
- [ ] **You can now chat with Nirog anytime by running `python chat_bot.py`**

---

## 🛑 Troubleshooting Quick Reference

### Problem: "pip is not recognized"
**Quick Fix:**
- [ ] Try: `python -m pip install -r requirements.txt`

### Problem: "API key not found"
**Quick Fix:**
- [ ] Check that your `.env` file is in the same folder as `chat_bot.py`
- [ ] Make sure there are no extra spaces in your API key
- [ ] Restart your terminal and try again

### Problem: "Invalid API key"
**Quick Fix:**
- [ ] Go back to [Google AI Studio](https://aistudio.google.com/)
- [ ] Create a new API key
- [ ] Replace the old key in your `.env` file

### Problem: MedyBot doesn't respond
**Quick Fix:**
- [ ] Check your internet connection
- [ ] Wait 10 seconds and try a shorter message
- [ ] Press `Ctrl+C` to stop, then run `python chat_bot.py` again

### Problem: "Permission denied" (Mac/Linux)
**Quick Fix:**
- [ ] Try: `pip3 install --user -r requirements.txt`

---

## ✅ Post-Setup Verification Checklist

**Confirm these success indicators:**

- [ ] **Python is installed** (version 3.7 or higher)
- [ ] **MedyBot folder is accessible** via terminal/command prompt
- [ ] **Dependencies are installed** (google-generativeai, python-dotenv)
- [ ] **API key is configured** in `.env` file
- [ ] **MedyBot starts successfully** with greeting message
- [ ] **Nirog responds to test messages** appropriately
- [ ] **You can exit cleanly** by typing `exit`

---

## 🎯 What to Do Next After Successful Setup

### Start Using MedyBot
- [ ] **Ask health questions:** "I have a sore throat, what should I do?"
- [ ] **Request medication advice:** "What can I take for a headache?"
- [ ] **Book appointments:** "I need to see a heart doctor"
- [ ] **Get health education:** "How can I boost my immune system?"

### Learn More Features
- [ ] Read [`USER_MANUAL.md`](USER_MANUAL.md) for detailed feature guide
- [ ] Check [`FAQ.md`](FAQ.md) for common questions and answers
- [ ] Review [`README.md`](README.md) for comprehensive documentation

### Remember These Important Points
- [ ] **For emergencies:** Call 102/108 (India) or your local emergency services
- [ ] **For serious conditions:** Always consult real doctors
- [ ] **Privacy:** Your conversations aren't stored permanently
- [ ] **API key security:** Keep your key private and secure

### Daily Usage
- [ ] **To start MedyBot:** Navigate to folder and run `python chat_bot.py`
- [ ] **To exit:** Type `exit`, `quit`, or `bye`
- [ ] **For help:** Ask Nirog directly or check the documentation

---

## 📞 Need Additional Help?

**If you're still having trouble:**

- [ ] **Check [`FAQ.md`](FAQ.md)** - Most issues are covered there
- [ ] **Review error messages carefully** - They often contain helpful clues
- [ ] **Try the detailed troubleshooting** in [`README.md`](README.md)
- [ ] **Start fresh** - Sometimes restarting your terminal helps

---

## 🏥 Medical Safety Reminders

**Always Remember:**
- [ ] **MedyBot is for education only** - Not a replacement for doctors
- [ ] **For emergencies:** Call emergency services immediately
- [ ] **For serious conditions:** Consult qualified healthcare professionals
- [ ] **Medication advice:** Only for over-the-counter medicines
- [ ] **No diagnoses:** Nirog provides information, not medical diagnoses

---

**🎉 Congratulations! You've successfully set up MedyBot and are ready to chat with Nirog, your friendly medical assistant from Delhi!**

---

*Keep this checklist handy for future reference or to help others set up MedyBot.*

**Last Updated**: August 2025 | **Version**: 2.0 | **Setup Time**: ~15 minutes