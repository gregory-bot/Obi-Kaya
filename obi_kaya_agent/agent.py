import datetime
import json
import os
from typing import Dict, List, Optional
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.generativeai import GenerativeModel
from google.genai import types
import vertexai
from vertexai.preview import reasoning_engines


def generate_recommendations_from_input(user_text: str, goal_or_request: Optional[str] = None) -> dict:
    """
    Analyze community data (text or PDF content) and return structured, actionable recommendations in three categories:
    - Event Ideas & Timing
    - Social Media Strategy
    - Ongoing Engagement (Beyond Events)
    Uses Gemini 2.0 to:
    - Reference community data, trends, and best practices
    - Phrase each suggestion as an actionable plan, referencing data and best practices
    Returns a dict with status and recommendations (organized by category)
    """
    if not user_text or len(user_text.strip()) < 50:
        return {
            "status": "error",
            "message": "Please provide valid community data (text or PDF content) for recommendations."
        }
    prompt = (
        "You are a professional community manager assistant for Google Developer Group organizers. "
        "Analyze the following community data and generate actionable recommendations in these three categories:"
        "\n1. Event Ideas & Timing: Suggest event types, formats, and optimal scheduling based on the data. Reference audience demographics, engagement trends, and best practices."
        "\n2. Social Media Strategy: Provide channel-specific guidance (Twitter/X, Instagram, Facebook, etc.), including post examples, hashtags, and optimal posting times. Reference best practices and analytics if available."
        "\n3. Ongoing Engagement (Beyond Events): Suggest tactics to keep members active between events (newsletters, online forums, content sharing, etc.), referencing research-backed strategies."
        "\n\nFor each category, provide 2-4 actionable, data-driven recommendations. Phrase each as a clear plan (e.g., 'do X, focusing on Y'), referencing the community's data and best practices. If possible, cite authoritative tips."
        f"\n\nCommunity Data:\n{user_text}"
        f"\n\nOrganizer's goal/request: {goal_or_request if goal_or_request else '[None]'}"
        "\n\nFormat your answer as a JSON object with keys: 'Event Ideas & Timing', 'Social Media Strategy', 'Ongoing Engagement'. Each key should contain a list of recommendations as strings."
    )
    try:
        model = GenerativeModel(model_name="gemini-2.0-flash")
        response = model.generate_content(prompt)
        try:
            recommendations = json.loads(response.text)
        except Exception:
            recommendations = response.text.strip()
        return {
            "status": "success",
            "recommendations": recommendations
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Unable to generate recommendations due to an internal error: {str(e)}"
        }

