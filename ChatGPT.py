import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("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")
)

question = input("Ask me anything: ")
def answer(question):
    response = client.chat.completions.create(
    messages=[
        {
        "role": "user",
        "content": question
        }
    ],
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=1024,
    n=1,
    stop=None
    )
    return response
    print(response)