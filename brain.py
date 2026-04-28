import ollama

chat_history = [{'role': 'system', 'content': 'Ты — Джарвис, остроумный помощник Тони Старка. Отвечай кратко и на русском.'}]
def get_ai_response(user_text):
    global chat_history
    chat_history.append({'role': 'user', 'content': user_text})
    try:
        response = ollama.chat(model="llama3", messages=chat_history)
        ai_response = response['message']['content']
        chat_history.append({'role': 'assistant', 'content': ai_response})

        if len(chat_history) > 11:
            chat_history = [chat_history[0]] + chat_history[-10:]

        return ai_response
    except Exception as e:
        return f"Something wrong with intellect module: {e}"