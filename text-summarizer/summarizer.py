import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_API_BASE')
)

def summarize(text: str) -> str:
    prompt = f"""
    Summarize the given paragraph into a single-line summary.

    Paragraph:
    {text}
    """

    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=80,
        temperature=0.5
    )
    return completion.choices[0].message.content

paragraph = "Artificial Intelligence enables machines to mimic human intelligence, performing tasks such as learning, problem-solving, and decision-making with increasing accuracy."
response = summarize(paragraph)
print(response)
