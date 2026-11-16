import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_API_BASE")
)

def compare(item1: str, item2: str) -> str:
    prompt = f"""
    Compare the chipset used in two given major iPhone models {item1} and {item2}. Include the CHIP NAME in response and ensure the response is in ONE WORD only.
    """.strip()

    completion = client.chat.completions.create(
        model="gpt-6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.5
    )

    return completion.choices[0].message.content

response = compare("iphone 13", "iphone 17")
print(response)