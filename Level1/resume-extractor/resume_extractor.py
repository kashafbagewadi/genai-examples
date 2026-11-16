import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
    base_url = os.environ.get('OPENAI_API_BASE')
)

def extract_keywords(text: str) -> str:
    prompt = f"""
    Extract exactly five comma-separated job-relevant keywords from a given resume paragraph.

    Paragraph:
    {text}
    """

    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0
    )
    return completion.choices[0].message.content

resume_paragraph = "Experienced DevOps engineer skilled in Python, Kubernetes, Docker, CI/CD pipelines, and cloud automation."
response = extract_keywords(resume_paragraph)
print(response)
