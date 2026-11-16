import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_API_BASE')
)

def generate_commit(changes: str) -> str:
    prompt = f"""
    You are a Git Commit Generator. Analyze the given code change description and produce clean, Conventional Commit-style message, following the guidelines below:
    1. The output must be a single-line commit message in '<type>: <subject>' format.
    2. Choose the appropriate commit type from: feat, fix, or docs. 
    3. Generate a concise subject (<50 characters).

    Code Change Summary:
    {changes}
    """
    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.0
    )
    return completion.choices[0].message.content

code_changes = 'Added a new user registration endpoint and fixed a typo in the README file.'
response = generate_commit(code_changes)
print(response)