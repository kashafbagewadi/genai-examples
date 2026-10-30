import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE")
)

def clarify_bug(description: str) -> str:
    prompt = f"""
Please transform the following informal bug report into a clear, structured, and professional issue summary. 
Include sections such as Summary, Steps to Reproduce, Expected Behavior, and Actual Behavior where appropriate.

Bug Description:
{description}
""".strip()

    completion = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.0,
    )

    return completion.choices[0].message.content

DEFAULT_BUG = "Image upload is failing while trying to upload a profile image."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        bug = " ".join(sys.argv[1:])
    else:
        bug = input("Describe the bug (Enter to use the example): ").strip() or DEFAULT_BUG

    response = clarify_bug(bug)

    print("=== Clarified Bug Summary ===")
    print(response)
