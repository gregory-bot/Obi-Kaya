# Obi-Kaya Smart Community Assistant Agent
![Obi-Kaya Chatbot Screenshot](images/WhatsApp%20Image%202025-06-29%20at%2010.07.45_e846fa43.jpg)

Obi-Kaya is a Smart Community Assistant Agent designed to empower Google Developer Group (GDG) organizers, especially in Sub-Saharan Africa, to maximize their community's impact, secure partnerships, and sustain engagement. The agent analyzes community data, generates actionable recommendations, crafts partnership/sponsorship pitches, and provides strategies for ongoing engagement. It is multilingual and can respond in most African languages.

---

## Project Structure

```
obi_kaya_agent/
    __init__.py
    agent.py
.env
```
- **agent.py:** Main file containing the agent definition and all tool implementations.
- **__init__.py:** Marks the directory as a Python package.
- **.env:** (Not committed) Holds your API keys and secrets.

---

## Requirements

- Python 3.8+
- `google-adk`
- `google-generativeai`

---

## Installation

### 1. Clone or Fork the Repository

```sh
git clone https://github.com/gregory-bot/Obi-Kaya.git
cd Obi-Kaya
```
*(If you haven't already, you can fork the original guide repo at https://github.com/mwanyumba7/Obi-Kaya and clone your fork)*

### 2. Create a Virtual Environment (Recommended)

```sh
python -m venv env
source env/Scripts/activate  # On Windows
# or
source env/bin/activate      # On Mac/Linux
```

### 3. Install Required Packages

```sh
pip install google-adk google-generativeai
```

### 4. Set Up Environment Variables

Create a `.env` file in your project root with your Gemini API key:
```
GOOGLE_API_KEY=your-gemini-api-key-here
```
*(Never commit your API key to GitHub!)*

---

## Step-by-Step Guide: Building the Agent

### 1. Project Setup

- Ensure your folder structure matches the one above.
- All code is in `obi_kaya_agent/agent.py`.

### 2. Implemented Tools

#### a. `generate_recommendations_from_input`
- Analyzes community data (text or PDF content) and returns structured, actionable recommendations in three categories:
  - Event Ideas & Timing
  - Social Media Strategy
  - Ongoing Engagement (Beyond Events)
- Accepts user input, builds a prompt for Gemini LLM, and returns recommendations as a dictionary.

#### b. `generate_partnership_pitch`
- Generates a personalized partnership/sponsorship pitch using community data.
- Pitch includes:
  - Community Overview
  - Engagement Metrics
  - Impact Statements
  - Value Proposition
  - Next Steps

#### c. `answer_community_general_question`
- Answers general questions about community building, being a tech community organizer, creating and measuring impact, and troubleshooting Bevy platform issues.
- References best practices and support resources.

### 3. Defining the Agent

- The agent is defined in `agent.py` using the `Agent` class from `google.adk.agents`.
- Includes name, model, description, detailed instructions, and the three tools above.

### 4. Running and Viewing the Agent in ADK Web UI

- **Start the ADK Web UI:**
  ```sh
  adk web
  ```
- **Open your browser** and go to the URL provided (usually http://localhost:8000).
- **Select your agent** (`obi_kaya_agent`) and interact with it using the web interface.
---
![Obi-Kaya Chatbot Screenshot](images/WhatsApp%20Image%202025-06-29%20at%2010.18.34_3cdd9037.jpg)

## Example Usage

- **Get recommendations:** Upload a PDF report or paste community data, and ask for event or engagement ideas.
- **Generate a partnership pitch:** Provide your community stats and request a sponsorship pitch.
- **Ask a general question:**  
  - "How do I increase engagement in my developer community?"  
  - "How do I troubleshoot event registration on Bevy?"

---

## Deployment (Render.com Example)

1. **Push your code to GitHub.**
2. **Create a new Web Service on [Render.com](https://render.com/):**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `adk web --host 0.0.0.0 --port 10000`
   - **Add Environment Variable:**  
     - `GOOGLE_API_KEY=your-gemini-api-key-here`
3. **Deploy!**  
   Your app will be available at `https://your-app-name.onrender.com`.

---

## API Usage

You can connect any frontend (e.g., React) to the backend by making HTTP requests to the deployed API endpoints.

**Example (fetch in React):**
```js
fetch('https://obi-kaya.onrender.com/your-endpoint', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ user_text: "Hello" })
})
  .then(res => res.json())
  .then(data => {
    // handle response
  });
```

---

## Credits & Acknowledgements

- This repository and agent were also guided by [Brayan Kai's Obi-Kaya project](https://github.com/mwanyumba7/Obi-Kaya).
- Built using [google-adk](https://github.com/google/adk) and [google-generativeai](https://github.com/google/generative-ai-python).

---

## Support & Resources

- [google-adk documentation](https://github.com/google/adk)
- [Bevy support](https://help.bevy.com/hc/en-us/categories/22880458639767-Community-Enterprise-Pro)
- [Bevy blog](https://bevy.com/b/blog)
- [FasterCapital: Measuring Community Impact](https://fastercapital.com/topics/measuring-and-analyzing-community-growth-and-impact.html)
- [David Spinks' Community Insights](https://davidspinks.substack.com/)

---

## License

[MIT](LICENSE)
