import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_API_BASE")
)

def convert_to_bullets(text: str) -> str:
    prompt = f"""Convert the given paragraph into concise, easy-to-read bullet points.

    Paragraph:
    {text}
    """

    completion=client.chat.completions.create(
        model="gpt-6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.1
    )

    return completion.choices[0].message.content

sample_text = "Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and enabling new innovations across healthcare, finance, and education."

response = convert_to_bullets(sample_text)
print(response)