import openai
import tweepy
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load API keys from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # Google Trends API for U.S.

# Authenticate with X API
auth = tweepy.OAuthHandler(X_API_KEY, X_API_SECRET)
auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_SECRET)
api = tweepy.API(auth)

# Weekly schedule for persona-aligned tweets
WEEKLY_SCHEDULE = {
    "Monday": "Tech & Science Insight",
    "Wednesday": "Philosophical & Governance Reflection",
    "Friday": "Real-World Current Event Analysis",
    "Saturday": "Personal Reflection with Strategic Insight"
}

def get_us_trending_topics():
    """Fetch AI, governance, and innovation trends in the U.S. using Google News API or SerpAPI."""
    url = f"https://serpapi.com/search.json?q=AI+policy+USA&engine=google_news&gl=US&api_key={SERPAPI_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if "news_results" in data:
            trends = [article["title"] for article in data["news_results"][:5]]
            return trends
        else:
            return [
                "U.S. Congress debates AI regulation policy",
                "New AI-driven governance models proposed in Silicon Valley",
                "Quantum computing breakthroughs and their economic impact",
                "Ethical concerns over AI automation in the workplace",
                "Future of decentralized AI and digital sovereignty in the U.S."
            ]
    except Exception as e:
        print(f"❌ Error fetching U.S. trends: {e}")
        return [
            "How AI governance is shaping the next decade in the U.S.",
            "The risks and rewards of AI-led policymaking",
            "Philosophical implications of corporate AI sovereignty",
            "Why quantum computing may redefine national security",
            "The role of ethical leadership in AI-driven societies"
        ]

def generate_tweet(trending_topics, category):
    """Generate a persona-aligned, U.S.-specific tweet using GPT-4o."""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Corrected OpenAI API call

    prompt = f"""
    You are an AI-driven strategist and thought leader, targeting a U.S. audience.
    Generate a high-impact tweet under the "{category}" category, using an analytical and engaging tone.
    
    The tweet must:
    - Relate to AI, governance, or innovation in the U.S.
    - Reflect a strategic and philosophical perspective.
    - Be under 280 characters.
    - Use a powerful and engaging tone.

    Trending topics to consider:
    {trending_topics}

    Output only the tweet, no extra text.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        tweet_content = response.choices[0].message.content.strip()
        return tweet_content[:280]
    except Exception as e:
        print(f"❌ Error generating tweet: {e}")
        return None

def post_tweet():
    """Fetch U.S.-specific trends, generate an AI-powered tweet, and post it to X."""
    today = "Monday" #datetime.today().strftime('%A')

    if today in WEEKLY_SCHEDULE:
        category = WEEKLY_SCHEDULE[today]
        trending_topics = get_us_trending_topics()
        tweet_content = generate_tweet(trending_topics, category)

        if tweet_content:
            try:
                api.update_status(tweet_content)
                print(f"✅ Successfully posted: {tweet_content}")
            except Exception as e:
                print(f"❌ Error posting tweet: {e}")
        else:
            print("❌ No tweet generated.")
    else:
        print("📅 No scheduled tweet today.")

# Run the function
post_tweet()
