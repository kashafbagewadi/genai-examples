import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
    base_url = os.environ.get('OPENAI_API_BASE')
)

def rewrite_email(text: str) -> str:
    prompt = f"""
    You're an AI Email Assistant that rewrites given messages into polite and professional emails.

    Email Message:
    {text}
    """

    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=60,
        temperature=0.1
    )

    return completion.choices[0].message.content

email_msg = "hey send me that report asap"
response = rewrite_email(email_msg)
print(response)