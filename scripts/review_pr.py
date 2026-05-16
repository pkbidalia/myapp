from openai import OpenAI

client = OpenAI(api_key="YOUR_KEY")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "Review this code for bugs and security issues."},
        {"role": "user", "content": open("diff.txt").read()}
    ]
)

print(response.choices[0].message.content)