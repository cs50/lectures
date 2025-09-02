# Prompts user.
# "In one sentence, what is CS50?"
# "In one word, what is CS50?"
# "In one word, which is better, Harvard or Stanford?"

from openai import OpenAI

client = OpenAI()

prompt = input("Prompt: ")

response = client.responses.create(
    input=prompt,
    model="gpt-5"
)

print(response.output_text)
