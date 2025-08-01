# MedyBot User Manual 📖

**Complete Guide to Using Nirog, Your Medical Assistant**

Welcome to the comprehensive user manual for MedyBot! This guide will walk you through every feature, show you detailed examples, and help you get the most out of your conversations with Nirog.

---

## 📋 Table of Contents

1. [Introduction to Nirog](#-introduction-to-nirog)
2. [Getting Started](#-getting-started)
3. [Core Features Overview](#-core-features-overview)
4. [Health Consultation Features](#-health-consultation-features)
5. [Appointment Booking System](#-appointment-booking-system)
6. [Page Navigation Feature](#-page-navigation-feature)
7. [Understanding Nirog's Responses](#-understanding-nirogs-responses)
8. [Best Practices for Medical Queries](#-best-practices-for-medical-queries)
9. [Advanced Usage Tips](#-advanced-usage-tips)
10. [Safety Guidelines & Limitations](#-safety-guidelines--limitations)
11. [Troubleshooting Common Issues](#-troubleshooting-common-issues)

---

## 👋 Introduction to Nirog

### Who is Nirog?
Nirog is your friendly medical assistant from Delhi, India, powered by Google's advanced Gemini AI. Unlike a typical chatbot, Nirog has been designed with a warm, empathetic personality and extensive medical knowledge to help you with:

- **General health advice** and education
- **Over-the-counter medication** suggestions with proper dosages
- **Symptom guidance** and when to seek professional help
- **Appointment booking** with qualified specialist doctors
- **Medical information** simplified for easy understanding

### Nirog's Background
- **Location**: Delhi, India (grew up and studied there)
- **Organization**: Works at Medycall
- **Personality**: Friendly, empathetic, supportive, and knowledgeable
- **Language**: Communicates in clear, non-technical English
- **Approach**: Always reminds users to consult real doctors for serious conditions

---

## 🚀 Getting Started

### System Requirements
Before using MedyBot, ensure you have:
- Python 3.7 or higher
- Stable internet connection
- Google Gemini API key
- 50MB free storage space

### Starting MedyBot
1. Open your terminal/command prompt
2. Navigate to your MedyBot folder
3. Run: `python chat_bot.py`
4. Wait for Nirog's greeting message

### First Interaction
```
👩‍⚕️ MedyBot: Hello! I am your medical assistant. How can I help you today?
You: 
```

At this point, you can type any health-related question or concern.

---

## 🌟 Core Features Overview

### 1. **Intelligent Health Consultation**
- Provides personalized health advice based on your symptoms
- Suggests appropriate over-the-counter medications
- Explains medical conditions in simple terms
- Offers guidance on when to seek professional help

### 2. **Smart Appointment Booking**
- Matches you with the right specialist based on your needs
- Covers 5 cities: Delhi, Mumbai, Gurgaon, Gaziabad, and Vrindavan
- Formats appointment details professionally
- Provides doctor information and availability

### 3. **Context-Aware Conversations**
- Remembers your entire conversation during the session
- Builds responses based on previous interactions
- Maintains conversation flow naturally
- Provides relevant follow-up suggestions

### 4. **Page Navigation System**
- Can direct you to different sections or pages
- Uses specific formatting for navigation commands
- Helps organize information and user flow

### 5. **Real-Time Timestamp Integration**
- All interactions include current date and time
- Helps with appointment scheduling
- Provides context for time-sensitive advice

---

## 🏥 Health Consultation Features

### Types of Health Queries You Can Ask

#### 1. **Symptom-Based Questions**
Ask about specific symptoms you're experiencing:

**Example:**
```
You: I have a sore throat and slight fever

👩‍⚕️ MedyBot: I understand you're experiencing a sore throat and slight fever. Here's what I recommend:

💊 **Immediate Relief:**
- Paracetamol 500mg every 6-8 hours for fever (max 4 doses/day)
- Warm salt water gargle (1 tsp salt in warm water) 3-4 times daily
- Throat lozenges or honey for soothing relief
- Stay hydrated with warm fluids

🏠 **Home Care:**
- Rest and avoid strenuous activities
- Use a humidifier or breathe steam from hot water
- Avoid cold drinks and ice cream

⚠️ **See a doctor if:**
- Fever exceeds 101°F (38.3°C)
- Severe difficulty swallowing
- Symptoms persist beyond 3-4 days
- White patches or pus in throat

Would you like me to help you book an appointment with a doctor?
```

#### 2. **Medication Inquiries**
Ask about over-the-counter medications:

**Example:**
```
You: What can I take for a headache?

👩‍⚕️ MedyBot: For headache relief, here are safe over-the-counter options:

💊 **Primary Options:**
- **Paracetamol (Acetaminophen)**: 500-1000mg every 6-8 hours (max 4g/day)
- **Ibuprofen**: 200-400mg every 6-8 hours (max 1200mg/day)
- **Aspirin**: 500-1000mg every 4-6 hours (max 4g/day)

⚠️ **Important Notes:**
- Don't exceed recommended doses
- Take with food if you have a sensitive stomach
- Avoid aspirin if under 18 years old
- Don't combine multiple pain relievers

🏠 **Additional Relief:**
- Apply cold compress to forehead
- Rest in a quiet, dark room
- Stay hydrated
- Gentle neck and shoulder massage

**When to see a doctor:**
- Sudden, severe headache
- Headache with fever, stiff neck, or vision changes
- Frequent headaches (more than 2-3 per week)
```

#### 3. **Preventive Health Questions**
Ask about maintaining good health:

**Example:**
```
You: How can I boost my immune system naturally?

👩‍⚕️ MedyBot: Great question! Here are natural ways to strengthen your immune system:

🥗 **Nutrition:**
- Eat plenty of fruits and vegetables (especially citrus, berries, leafy greens)
- Include zinc-rich foods (nuts, seeds, legumes)
- Consume probiotics (yogurt, kefir, fermented foods)
- Stay hydrated with 8-10 glasses of water daily

💪 **Lifestyle:**
- Get 7-9 hours of quality sleep
- Exercise regularly (30 minutes, 5 days/week)
- Manage stress through meditation or relaxation
- Avoid smoking and limit alcohol

☀️ **Supplements (if needed):**
- Vitamin D3 (especially if limited sun exposure)
- Vitamin C (500-1000mg daily)
- Zinc (8-11mg daily)

⚠️ **Remember:** A balanced diet is usually sufficient. Consult a doctor before starting supplements, especially if you have health conditions.
```

### Understanding Medication Recommendations

When Nirog suggests medications, the response includes:
- **Generic and brand names**
- **Exact dosages** and frequency
- **Maximum daily limits**
- **Important warnings** and contraindications
- **When to stop** and see a doctor

---

## 📅 Appointment Booking System

### Available Doctors and Specialties

MedyBot can help you book appointments with these qualified professionals:

| Doctor | Specialty | Location | Best For |
|--------|-----------|----------|----------|
| **Dr. Sarah Johnson** | Cardiologist | Vrindavan | Heart problems, chest pain, blood pressure |
| **Dr. Michael Chen** | General Physician | Gaziabad | General health, fever, infections, checkups |
| **Dr. Priya Patel** | Pediatrician | Delhi | Children's health, vaccinations, growth issues |
| **Dr. Robert Wilson** | Dermatologist | Gurgaon | Skin problems, rashes, acne, hair loss |
| **Dr. Lisa Garcia** | Neurologist | Mumbai | Headaches, seizures, nerve problems, memory issues |

### How to Book an Appointment

#### Step 1: Express Your Need
Start by telling Nirog you need an appointment:

```
You: I need to see a doctor
You: Can you book an appointment for me?
You: I want to schedule a visit with a specialist
```

#### Step 2: Specify Your Requirements
Nirog will ask for details. You can provide:
- **Type of doctor** you need
- **Your location** or preferred city
- **Reason** for the visit
- **Preferred date and time**

#### Complete Booking Example:

```
You: I need to book an appointment with a skin doctor

👩‍⚕️ MedyBot: I can help you with that! For skin-related concerns, I recommend Dr. Robert Wilson, our experienced Dermatologist in Gurgaon.

What's the reason for your visit, and when would you like to schedule it?

You: I have persistent acne. Can I see him tomorrow at 2 PM?

👩‍⚕️ MedyBot: I've prepared your appointment details:

**Date:** Tomorrow (August 2, 2025)
**Time:** 2:00 PM
**Cause:** Persistent acne
**Doctor:** Dr. Robert Wilson (Dermatologist) — Gurgaon

📋 **Before Your Visit:**
- Avoid using new skincare products 24 hours before
- Make a list of current medications and skincare routine
- Note when the acne started and any triggers you've noticed

Would you like any advice on managing acne until your appointment?
```

### Appointment Information Provided

For each appointment, Nirog provides:
- **Complete date and time**
- **Doctor's name and specialty**
- **Location/city**
- **Reason for visit**
- **Pre-appointment preparation tips**
- **Relevant medical advice**

---

## 🧭 Page Navigation Feature

### How Navigation Works

Nirog can direct you to different pages or sections using a special format:

```
👩‍⚕️ MedyBot: page: [page-name]
```

### Navigation Examples

#### Example 1: Appointment Page
```
You: Take me to the appointment booking page

👩‍⚕️ MedyBot: page: appointment-booking

I'm directing you to the appointment booking page where you can schedule a visit with one of our doctors. Would you like me to help you choose the right specialist for your needs?
```

#### Example 2: Emergency Information
```
You: Show me emergency information

👩‍⚕️ MedyBot: page: emergency-info

I'm taking you to the emergency information page. Remember, for immediate medical emergencies, call:
- India: 102 (Ambulance) or 108 (Emergency Response)
- Always seek immediate help for chest pain, difficulty breathing, or severe injuries.
```

### Common Navigation Requests
- "Take me to the appointment page"
- "Show me the doctor list"
- "Go to emergency information"
- "Navigate to medication guide"

---

## 🧠 Understanding Nirog's Responses

### Response Structure

Nirog's responses typically follow this structure:

1. **Acknowledgment** - Shows understanding of your concern
2. **Main Advice** - Primary recommendations or information
3. **Additional Details** - Supporting information or alternatives
4. **Safety Warnings** - When to seek professional help
5. **Follow-up** - Questions or next steps

### Response Formatting Elements

#### 💊 **Medication Sections**
- Clear dosage instructions
- Frequency and timing
- Maximum daily limits
- Important warnings

#### ⚠️ **Warning Indicators**
- When to see a doctor immediately
- Serious symptoms to watch for
- Emergency situations

#### 🏠 **Home Care Tips**
- Self-care measures
- Lifestyle recommendations
- Natural remedies

#### 📋 **Preparation Lists**
- Pre-appointment instructions
- What to bring or prepare
- Questions to ask your doctor

### Tone and Language

Nirog communicates with:
- **Empathy**: "I understand you're feeling unwell..."
- **Clarity**: Simple, non-technical language
- **Support**: Encouraging and reassuring tone
- **Caution**: Always emphasizes safety and professional consultation

---

## 💡 Best Practices for Medical Queries

### How to Ask Effective Questions

#### ✅ **Good Examples:**
```
"I have a headache that started this morning, it's throbbing on the right side, and I feel nauseous."

"My 5-year-old has a fever of 100.5°F and is complaining of ear pain."

"I've had a persistent cough for 3 days with yellow phlegm and chest tightness."
```

#### ❌ **Less Effective Examples:**
```
"I feel bad."
"Something's wrong."
"I'm sick."
```

### Information to Include

When describing symptoms, mention:
- **Duration**: How long you've had the symptoms
- **Severity**: Mild, moderate, or severe
- **Location**: Where exactly you feel the problem
- **Triggers**: What makes it better or worse
- **Associated symptoms**: Other things you've noticed
- **Your age** (especially for children)
- **Current medications** you're taking

### Follow-Up Questions

Don't hesitate to ask:
- "Can you explain that in simpler terms?"
- "What should I do if the symptoms get worse?"
- "How long should I wait before seeing a doctor?"
- "Are there any side effects I should watch for?"
- "Can I take this with my other medications?"

---

## 🎯 Advanced Usage Tips

### Making the Most of Context Memory

Nirog remembers your entire conversation, so you can:

#### Build on Previous Topics
```
You: I have a headache

👩‍⚕️ MedyBot: [Provides headache advice]

You: What if the paracetamol doesn't work?

👩‍⚕️ MedyBot: If the paracetamol doesn't relieve your headache, you could try:
- Ibuprofen 400mg as an alternative
- Apply a cold compress to your forehead
- Rest in a quiet, dark room

If the headache persists or worsens after 4-6 hours, consider seeing a doctor.
```

#### Reference Previous Conversations
```
You: You mentioned Dr. Sarah Johnson earlier. What are her qualifications?

👩‍⚕️ MedyBot: Dr. Sarah Johnson is our Cardiologist based in Vrindavan. She specializes in heart-related conditions including:
- Chest pain evaluation
- Blood pressure management
- Heart rhythm disorders
- Preventive cardiology

She's available Monday through Friday, 9 AM to 5 PM.
```

### Getting Specific Information

#### Ask for Detailed Explanations
```
You: Can you explain what causes high blood pressure?

👩‍⚕️ MedyBot: High blood pressure (hypertension) can be caused by several factors:

**Primary Causes:**
- Genetics and family history
- Age (risk increases with age)
- Lifestyle factors

**Lifestyle Factors:**
- High sodium (salt) intake
- Lack of physical activity
- Excessive alcohol consumption
- Smoking
- Chronic stress
- Obesity

**Medical Conditions:**
- Kidney disease
- Sleep apnea
- Thyroid disorders
- Diabetes

**Prevention Tips:**
- Maintain healthy weight
- Exercise regularly (30 min/day)
- Limit sodium to 2,300mg/day
- Eat potassium-rich foods
- Manage stress effectively

Would you like specific advice on any of these areas?
```

### Using Nirog for Health Education

Ask educational questions like:
- "What's the difference between viral and bacterial infections?"
- "How do vaccines work?"
- "What are the warning signs of diabetes?"
- "How can I improve my sleep quality?"

---

## 🛡️ Safety Guidelines & Limitations

### What Nirog CAN Do

#### ✅ **Appropriate Uses:**
- Provide general health information and education
- Suggest over-the-counter medications with proper dosages
- Explain common medical conditions in simple terms
- Guide you on when to seek professional medical help
- Help format appointment requests with doctors
- Offer basic first aid and home care advice
- Provide preventive health recommendations

### What Nirog CANNOT Do

#### ❌ **Inappropriate Uses:**
- **Diagnose medical conditions** - Only doctors can provide diagnoses
- **Prescribe prescription medications** - Only licensed physicians can prescribe
- **Replace emergency medical care** - Call emergency services for emergencies
- **Provide specialized medical procedures** - Complex treatments require specialists
- **Store your medical records** - No permanent data storage
- **Guarantee medical outcomes** - All advice is general guidance only

### Emergency Situations - When NOT to Use MedyBot

**Call Emergency Services Immediately For:**
- **Chest pain** or pressure
- **Difficulty breathing** or shortness of breath
- **Severe allergic reactions** (swelling, difficulty breathing)
- **Loss of consciousness** or fainting
- **Severe bleeding** that won't stop
- **Signs of stroke** (face drooping, arm weakness, speech difficulty)
- **Severe burns** or injuries
- **Poisoning** or overdose
- **Suicidal thoughts** or mental health crisis

**Emergency Numbers:**
- **India**: 102 (Ambulance), 108 (Emergency Response)
- **International**: Your local emergency services

### Medical Disclaimer Reminders

- **Educational Purpose Only**: MedyBot provides information, not medical advice
- **No Doctor-Patient Relationship**: Conversations don't establish medical care
- **Individual Variation**: Medical needs vary by person
- **Professional Consultation Required**: Always consult healthcare providers
- **No Liability**: Users responsible for their medical decisions

---

## 🔧 Troubleshooting Common Issues

### Conversation Issues

#### Problem: Nirog Gives Generic Responses
**Solution:**
- Be more specific about your symptoms
- Include duration, severity, and location
- Mention your age and any relevant medical history
- Ask follow-up questions for clarification

#### Problem: Responses Are Too Technical
**Solution:**
```
You: Can you explain that in simpler terms?
You: I don't understand the medical terms you used
You: Can you break that down for me?
```

#### Problem: Nirog Doesn't Remember Previous Messages
**Solution:**
- This indicates a session restart - context is lost
- Restart the conversation with `python chat_bot.py`
- Provide relevant background information again

### Technical Issues

#### Problem: Slow Response Times
**Causes & Solutions:**
- **Slow internet**: Check your connection speed
- **API rate limits**: Wait 10-15 seconds between messages
- **Long conversation**: Restart for a fresh session
- **Server issues**: Try again in a few minutes

#### Problem: "API Key Error" Messages
**Solutions:**
1. Verify your API key in the `.env` file
2. Check for typos or extra spaces
3. Generate a new key from Google AI Studio
4. Restart your terminal after making changes

#### Problem: Unexpected Program Termination
**Solutions:**
1. Check for error messages in the terminal
2. Verify all dependencies are installed
3. Ensure stable internet connection
4. Restart the program: `python chat_bot.py`

### Getting Better Results

#### Tips for Clearer Communication:
- **Use complete sentences** rather than single words
- **Provide context** about your situation
- **Ask specific questions** rather than general ones
- **Mention your location** for doctor recommendations
- **Be honest** about symptoms and concerns

#### Example of Effective Communication:
```
❌ Poor: "Stomach hurts"

✅ Better: "I've had stomach pain for 2 days. It's a cramping pain in my lower abdomen that gets worse after eating. I also feel nauseous and have had loose stools twice today."
```

---

## 📞 Additional Resources

### When You Need More Help

#### For Technical Issues:
- Check [`FAQ.md`](FAQ.md) for common questions
- Review [`README.md`](README.md) for detailed setup instructions
- Follow [`QUICK_START_GUIDE.md`](QUICK_START_GUIDE.md) for basic setup

#### For Medical Emergencies:
- **Never rely on MedyBot for emergencies**
- Call your local emergency services immediately
- Go to the nearest emergency room
- Contact your personal physician

#### For General Health Information:
- Consult with qualified healthcare professionals
- Visit reputable medical websites
- Contact your local health department
- Speak with pharmacists for medication questions

### Maximizing Your MedyBot Experience

#### Regular Usage Tips:
- **Start fresh sessions** for unrelated health topics
- **Keep conversations focused** on one health issue at a time
- **Ask for clarification** when needed
- **Follow up** on previous advice

#### Building Health Awareness:
- Use MedyBot to **learn about health topics**
- **Prepare questions** for your doctor visits
- **Understand medications** before taking them
- **Stay informed** about preventive care

---

## 🎯 Quick Reference Guide

### Essential Commands
```bash
# Start MedyBot
python chat_bot.py

# Exit conversation
Type: exit, quit, or bye
```

### Common Question Patterns
- **Symptoms**: "I have [symptom] for [duration]..."
- **Medications**: "What can I take for [condition]?"
- **Appointments**: "I need to see a [specialist] for [reason]"
- **Navigation**: "Take me to [page name]"
- **Education**: "Can you explain [medical topic]?"

### Key Features Summary
- ✅ **Health consultation** with medication suggestions
- ✅ **Appointment booking** with 5 specialist doctors
- ✅ **Context-aware** conversations with memory
- ✅ **Page navigation** for organized information
- ✅ **Real-time timestamps** for accurate scheduling
- ✅ **Safety reminders** and professional consultation guidance

---

**🏥 Ready to make the most of your conversations with Nirog? Start with specific questions and don't hesitate to ask for clarification!**

---

*Remember: MedyBot is designed for educational and informational purposes only. Always consult qualified healthcare professionals for medical advice, diagnosis, and treatment.*

**Last Updated**: January 2025 | **Version**: 2.0 | **Powered by**: Google Gemini 2.5 Pro