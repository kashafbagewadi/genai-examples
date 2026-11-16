import os
import textwrap
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_API_BASE')
)

def generate_comment(code_snippet: str) -> str:
    prompt = f"""
    Analyze the given code snippet and produces a clear, one-line comment or docstring describing its purpose.

    Code snippet:
    {code_snippet}
    """

    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
        temperature=0.2
    )
    return completion.choices[0].message.content

code_snippet = textwrap.dedent("""
    def calculate_area(length, width):
        return length * width
    """).strip()
response = generate_comment(code_snippet)
print(response)
