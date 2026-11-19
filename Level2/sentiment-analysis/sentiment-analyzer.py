import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def analyze_sentiment(text: str) -> str:
    prompt = f"""
    Analyze the sentiment (Positive, Negative or Neutral) of a given text and respond in the following format:
    Sentiment:<Positive/Negative/Neutral>
    Reason:<short explanation>

    Text:
    {text}
    """
    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=60,
        temperature=0.0
    )
    return completion.choices[0].message.content

inputText = "I am really happy with the new update!"
response = analyze_sentiment(inputText)
print(response)