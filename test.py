import ollama
from J_sound import speak

response = ollama.chat(model='llama3', messages=[
  {'role': 'user', 'content': 'Привет! Представься как Джарвис. На Русском и коротко'},
])
speak(response['message']['content'])