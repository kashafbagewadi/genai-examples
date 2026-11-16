import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_API_BASE')
)

def generate_haiku(topic: str) -> str:
    parameterized_prompt = f"""
    Generate three-line haikus using 5-7-5 syllable pattern based on a given topic.

    Topic:
    {topic}
    """

    completion=client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": parameterized_prompt}],
        max_tokens=200,
        temperature=0.0
    )
    return completion.choices[0].message.content

topic = "sky"
response = generate_haiku(topic)
print(response)
