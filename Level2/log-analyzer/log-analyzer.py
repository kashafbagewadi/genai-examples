import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def analyze_log_anomaly(log_file_path: str) -> str:
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()
    
    system_prompt = (
        "You are an auditor. Read the given logs and focus ONLY on the [CRITICAL] line. "
        "Provide a two-part summary: 1) The error type, 2) Immediate Impact."
    )
    user_prompt = f"Logs:\n{logs}"

    completion = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=80,
        temperature=0.1,
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    print(analyze_log_anomaly("/root/openaiproject/app.log"))