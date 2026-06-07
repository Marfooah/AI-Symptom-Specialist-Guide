# 🩺 AI Symptom → Specialist Guide

An AI-powered healthcare navigation assistant that helps users determine which medical specialist they should consult based on their symptoms.

Instead of attempting to diagnose medical conditions, the application uses a Large Language Model (LLM) to analyze symptom descriptions, recommend relevant specialists, assess urgency levels, and provide safe next-step guidance.

Built with Streamlit and Groq's Llama 3.3 70B model.

---

🚀 Live Demo: https://ai-symptom-specialist-guide.streamlit.app/

## 📸 Application Preview

<img width="2876" height="1638" alt="image" src="https://github.com/user-attachments/assets/047b5f7a-096a-468e-b989-1824a72a14e0" />
<img width="2876" height="600" alt="image" src="https://github.com/user-attachments/assets/5d6cea5b-a77a-4650-be28-4aa54b51cf26" />

---

## 📌 Problem Statement

Many people experience symptoms but are unsure which specialist to visit.

Questions like:

* Should I see a Cardiologist or Pulmonologist?
* Is this urgent or can it wait?
* Which doctor handles these symptoms?

often lead to confusion, delayed care, or unnecessary anxiety.

This project aims to simplify the first step of healthcare navigation by helping users identify the most relevant medical specialist and understand the urgency of seeking care.

---

## ✨ Features

### 🧠 AI-Powered Symptom Analysis

Users can describe symptoms in natural language, such as:

```text
Chest discomfort, dizziness, and shortness of breath.
```

The AI analyzes the symptoms and generates structured guidance.

---

### 👨‍⚕️ Specialist Recommendations

Suggests one or more relevant specialists, including:

* Cardiologist
* Neurologist
* Dermatologist
* Pulmonologist
* ENT Specialist
* Gastroenterologist
* Endocrinologist
* Rheumatologist
* Psychiatrist
* Urologist
* Gynecologist
* And more

Each recommendation includes a simple explanation of why that specialist may be relevant.

---

### 🚨 Urgency Assessment

Categorizes symptoms into one of three urgency levels:

| Level     | Meaning                          |
| --------- | -------------------------------- |
| Emergency | Immediate medical attention / ER |
| Urgent    | Within 24–48 hours               |
| Routine   | Within 1–2 weeks                 |

---

### 🛡️ Safe AI Design

This application is intentionally designed with healthcare safety guardrails:

✅ Does not diagnose conditions

✅ Does not prescribe medications

✅ Avoids fear-mongering

✅ Encourages professional medical consultation

✅ Provides only specialist guidance and urgency recommendations

---

### 💡 Practical Next Steps

Every response includes:

#### What You Can Do Right Now

Examples:

* Rest and monitor symptoms
* Stay hydrated
* Seek urgent care if symptoms worsen
* Prepare information for a doctor visit

---

## 🏗️ Project Structure

```bash
AI-Symptom-Specialist-Guide/
│
├── app.py
├── requirements.txt
├── README.md
```

---

## ⚙️ How It Works

### Step 1

User enters symptoms through the Streamlit interface.

Example:

```text
Persistent headaches, dizziness, and blurred vision.
```

### Step 2

The symptom description is sent to Groq's Llama 3.3 70B model.

### Step 3

A carefully engineered system prompt instructs the model to:

* Recommend specialists
* Explain reasoning
* Determine urgency
* Ask clarifying questions if needed
* Provide safe guidance

### Step 4

The response is displayed in a structured format.

---

## 🛠️ Tech Stack

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| Python                  | Core programming language      |
| Streamlit               | Frontend web application       |
| Groq API                | LLM inference                  |
| Llama 3.3 70B Versatile | Symptom analysis and reasoning |
| Prompt Engineering      | Medical triage workflow        |
| Environment Variables   | Secure API key management      |

---

## 🧠 Prompt Engineering Highlights

The system prompt constrains the model to act as a healthcare navigation assistant rather than a diagnostic system.

Key design principles:

* Recommend specialists only
* No diagnosis
* No medications
* Calm and reassuring communication
* Structured output format
* Clarifying questions when symptoms are vague
* Mandatory safety guidance section

This reduces hallucinations and encourages safer AI behavior in healthcare-related interactions.

---

## Example Output

### User Input

```text
Chest pain, dizziness, and shortness of breath.
```

### AI Response

```text
Specialist(s):
- Cardiologist — Chest discomfort and shortness of breath can involve the heart.
- Pulmonologist — Breathing-related symptoms may require lung evaluation.

Urgency Level:
- Emergency

What You Can Do Right Now:
- Seek immediate medical attention.
- Avoid strenuous activity.
- Do not drive yourself if symptoms are severe.
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Symptom-Specialist-Guide.git

cd AI-Symptom-Specialist-Guide
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variable

Mac/Linux:

```bash
export GROQ_API_KEY="your_api_key"
```

Windows:

```bash
set GROQ_API_KEY=your_api_key
```

---

## Run Locally

```bash
streamlit run app.py
```

Application will launch at:

```text
http://localhost:8501
```

---

## Future Enhancements

* Multi-language support
* Voice symptom input
* Medical specialty search database
* Symptom history tracking
* PDF consultation summary generation
* Healthcare provider directory integration
* Retrieval-Augmented Generation (RAG) with trusted medical sources

---

## Learning Outcomes

This project demonstrates:

* Generative AI application development
* Prompt engineering
* Responsible AI design
* LLM integration using APIs
* Streamlit development
* User-centered healthcare AI workflows
* AI safety and guardrail implementation

---

## Important Disclaimer

This project is for educational and informational purposes only.

It does not provide medical diagnoses, treatment recommendations, or professional medical advice.

Always consult a qualified healthcare professional regarding medical concerns.

For emergencies, contact local emergency services immediately.

---

## Author

**Ayesha Tariq**

AI Builder | AI Engineer | Creating practical AI applications that solve real-world problems.

---

## License

This project is licensed under the MIT License.
