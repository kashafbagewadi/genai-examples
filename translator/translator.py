import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_API_BASE')
)

def translate_to_language(text: str, language: str) -> str:
    prompt = f"""
    Translate the following English text into {language}. Return only the translation.

    Text:
    {text}
    """
    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.7
    )
    return completion.choices[0].message.content

input_text = "Good morning, how are you?"
spanish = translate_to_language(input_text, 'Spanish')
french = translate_to_language(input_text, 'French')

print(f"Spanish: {spanish}")
print(f"French: {french}")