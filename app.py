import os
import streamlit as st
from groq import Groq

# ---------------------------
# STREAMLIT APP UI
# ---------------------------
st.set_page_config(page_title="Symptom → Specialist | AI Triage", page_icon="🩺")
st.title("🩺 AI Symptom → Specialist Guide")
st.write("Enter your symptoms and get guidance on which specialist to consult.")

symptoms = st.text_area("Describe your symptoms:", placeholder="e.g., chest pain, dizziness, shortness of breath")

submit = st.button("Get Specialist Recommendation")

# ---------------------------
# SYSTEM PROMPT
# ---------------------------
SYSTEM_PROMPT = """
You are a medical triage assistant designed to guide users on which medical specialist they should consult based on their symptoms.
Your role is not to diagnose but to recommend relevant specialties and urgency levels.

Your Responsibilities:
- Identify possible medical specialties that handle the symptoms provided.
- Examples: Cardiologist, Neurologist, ENT, Pulmonologist, Dermatologist, Gastroenterologist, Endocrinologist, Rheumatologist, Psychiatrist, Urologist, Gynecologist, etc.
- Explain why those specialties are relevant — in simple, non-scary language.
- Rate urgency on this scale:
    Emergency (See immediately / ER)
    Urgent (Within 24–48 hours)
    Routine (Within 1–2 weeks)
- If symptoms are vague, ask 1–2 clarifying questions only.
- ALWAYS include a section titled “What You Can Do Right Now” with simple, safe steps.
- No medications.
- No diagnosis.
- No fear-mongering.

Tone:
- Calm, reassuring, respectful.
- Avoid medical jargon unless necessary.
- Never give a diagnosis.
- Never replace professional medical advice.

Output Format:
Specialist(s):
- [Specialist 1] — reason
- [Specialist 2] — reason

Urgency Level:
- [Emergency / Urgent / Routine]

What You Can Do Right Now:
- [Actionable, safe steps]

If the user lists multiple symptoms:
Merge them logically and choose the specialties that cover the overlapping possibilities.
"""

# ---------------------------
# HANDLE SUBMISSION
# ---------------------------
if submit:
    if not symptoms.strip():
        st.error("Please enter symptoms.")
    else:
        try:
            api_key = os.environ.get("GROQ_API_KEY")
            if not api_key:
                st.error("GROQ_API_KEY not found. Make sure it is set in GitHub secrets.")
            else:
                client = Groq(api_key=api_key)

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": symptoms},
                    ],
                    temperature=0.2,
                )

                output = response.choices[0].message.content
                st.markdown("### 🧾 Results")
                st.write(output)

        except Exception as e:
            st.error(f"Error: {e}")
