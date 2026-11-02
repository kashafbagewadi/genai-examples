import os
import sys
import textwrap
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY is not set. Check your .env file (or exported shell variables).")

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_API_BASE")
)

def generate_comment(code_snippet: str) -> str:
    prompt = f"""
    You're a software engineer, expert in understanding and explaining the code.
    Please read the given code snippet and generate a one-line comment explaining the provided code.

    Code Description:
    {code_snippet}
    """.strip()

    completion=client.chat.completions.create(
        model="gpt-6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.2
    )

    return completion.choices[0].message.content

sample_code_snippet = textwrap.dedent("""
    def calculate_area(length, width):
        return length * width
""").strip()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        code_snippet = " ".join(sys.argv[1:])
    else:
        ## method #1: When user enters multi-line code snippet
        # print("Paste the code snippet, then press Ctrl-D on a new line (Ctrl-D right away to use the example):")
        # code_snippet = sys.stdin.read().strip() or sample_code_snippet

        ## method #2: When user enters single/multi-line code snippet in a single line
        code_snippet = input("Provide the code snippet (Enter to use the example):").strip() or sample_code_snippet

    response = generate_comment(code_snippet)
    print(response)