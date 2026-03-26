import os
import logging
import google.cloud.logging
from dotenv import load_dotenv
import re

from google.adk import Agent
from google.adk.tools.tool_context import ToolContext

import google.auth
import google.auth.transport.requests
import google.oauth2.id_token

# --- Setup Logging and Environment ---

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()

model_name = os.getenv("MODEL")

# ── ADK Tool: Text Statistics ──────────────────────────────────────────────────

def analyze_text_stats(tool_context: ToolContext, text: str) -> dict:
    """Computes reading statistics for the input text and saves them to session state."""
    word_count = len(text.split())
    sentence_count = max(1, len(re.findall(r"[.!?]+", text)))
    reading_time_min = round(max(0.1, word_count / 200), 1)

    stats = {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "reading_time_min": reading_time_min,
    }

    # Persist stats to ADK session state so the caller can retrieve them
    tool_context.state["text_stats"] = stats
    tool_context.state["input_text"] = text

    logging.info(
        f"[analyze_text_stats] word_count={word_count}, "
        f"sentences={sentence_count}, reading_time={reading_time_min}min"
    )
    return stats


# ── Agent Instruction ──────────────────────────────────────────────────────────

INSTRUCTION = """
You are an expert Content Intelligence Agent. Your job is to fully analyze
any text the user provides and present the findings in a clear, readable format.

WORKFLOW:
1. First, call the 'analyze_text_stats' tool with the user's text.
   This computes reading statistics and stores them in session state.
2. Then respond in the following structured format — use plain language, not JSON:

---
**Content Type:** <one of: News Article | Academic | Business Report | Legal Document | Technical | Email | Social Media | Other>

**Summary**
<A clear 3–5 sentence summary of the main ideas.>

**Key Points**
• <concise takeaway>
• <concise takeaway>
• <concise takeaway>
(3 to 7 bullet points total)

**Sentiment:** <Positive | Negative | Neutral | Mixed>
<One sentence explaining why.>

**Action Items**
• <explicit task or next step>
• <explicit task or next step>
(Write "None found." if no action items are present in the text.)

**Reading Stats** (from analysis tool)
• Words: <word_count>
• Sentences: <sentence_count>
• Est. reading time: <reading_time_min> min
---

RULES:
- Always call the analyze_text_stats tool first and use its returned values for the Reading Stats section.
- Be factual, concise, and objective.
- Do not add any text outside the format above.
"""


# ── Root Agent (ADK entry point) ───────────────────────────────────────────────

root_agent = Agent(
    name="content_intelligence_agent",
    model=model_name,
    description=(
        "Analyzes any text and returns structured intelligence: "
        "classification, summary, key points, sentiment, and action items."
    ),
    instruction=INSTRUCTION,
    tools=[analyze_text_stats],
    output_key="analysis_result",  # Stores final output in ADK session state
)
