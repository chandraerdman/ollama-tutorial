# Test App for talking to Ollama chat bot.
import ollama

stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
