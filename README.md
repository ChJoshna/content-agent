# 🧠 Content Intelligence Agent  
GenAI Academy APAC Edition 2026 — Track 1 Project  
Built with Google ADK + Gemini, deployable on Google Cloud Run  

Python | Google ADK | Gemini | Cloud Run  

---

## 📌 Overview  

The **Content Intelligence Agent** is an AI-powered text analysis system built using Google's Agent Development Kit (ADK).  

It accepts any unstructured text and transforms it into structured, human-readable insights — including summary, key points, sentiment analysis, action items, and reading statistics.  

This project demonstrates how a **single-agent architecture with tool integration** can deliver powerful content understanding workflows.

---

## 🎯 What It Does  

Submit any text and get back structured intelligence:

| Category | Output |
|--------|--------|
| 🧾 Content Type | Classifies text (News, Technical, Email, etc.) |
| 📝 Summary | 3–5 sentence concise overview |
| 🔑 Key Points | Extracts main ideas into bullets |
| 💬 Sentiment | Positive / Negative / Neutral / Mixed |
| ✅ Action Items | Detects actionable tasks |
| 📊 Reading Stats | Word count, sentence count, reading time |

---

## 🏗️ Architecture  

This project follows a **tool-augmented single-agent pattern** using Google ADK:

root_agent (content_intelligence_agent)
│
├── Tool: analyze_text_stats
│ → Computes word count, sentence count, reading time
│ → Stores results in session state
│
└── LLM Execution (Gemini)
→ Reads user input + tool output
→ Generates structured intelligence report

root_agent (content_intelligence_agent)
│
├── Tool: analyze_text_stats
│ → Computes word count, sentence count, reading time
│ → Stores results in session state
│
└── LLM Execution (Gemini)
→ Reads user input + tool output
→ Generates structured intelligence report

content-agent/
├── agent.py ← Core agent + tool logic
├── requirements.txt ← Dependencies
├── .env ← Environment variables (not committed)
└── README.md ← Project documentation


---

## 🛠️ Tech Stack  

- **Google ADK** — Agent orchestration framework  
- **Gemini (via Vertex AI / API)** — LLM for reasoning  
- **Google Cloud Logging** — Observability  
- **Python 3.10+** — Core language  
- **dotenv** — Environment management  

---

## 🚀 Getting Started  

### Prerequisites  

- Python 3.10+  
- Google Cloud project  
- Authenticated `gcloud` CLI  
- Gemini model access  

---

### Local Setup  

```bash
# 1. Clone repository
git clone https://github.com/ChJoshna/content-agent.git
cd content-agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment variables
echo "MODEL=`MODEL`" > .env

# 5. Authenticate with Google Cloud
gcloud auth application-default login

# 6. Run the agent
python agent.py
```
🔄 How It Works
Step 1 — Tool Execution

The agent first calls:

analyze_text_stats(text)

This calculates:

Word count
Sentence count
Estimated reading time

Step 2 — AI Reasoning

The Gemini model then:

Classifies content type
Generates summary
Extracts key points
Determines sentiment
Identifies action items

📊 Sample Output
---
Content Type: Business Report

Summary:
This report outlines quarterly revenue growth...

Key Points:
• Revenue increased by 18%
• Expansion in APAC region
• Operational costs reduced

Sentiment: Positive  
Strong growth indicators and optimistic tone.

Action Items:
• Review expansion strategy
• Monitor cost optimization

Reading Stats:
• Words: 250
• Sentences: 15
• Est. reading time: 1.2 min
---


Explore the features of the agent at:
https://content-service-623667884898.europe-west1.run.app

👤 Author

ChJoshna
GitHub: https://github.com/ChJoshna

Built for: GenAI Academy APAC Edition 2026
