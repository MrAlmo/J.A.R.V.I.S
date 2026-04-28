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


def get_intent(user_text):
    prompt = f"""
    Ты — модуль управления Джарвиса. Твоя задача — понять, чего хочет пользователь.
    Доступные команды:
    - open_dota: если пользователь хочет поиграть, запустить доту или открыть игру.
    - close_dota: если пользователь хочет закрыть игру или говорит что проиграл.
    - stop_program: если пользователь хочет остановить работу этого скрипта, лучше переспросить "Вы точно хотите остановить эту программу?".
    - none: если это просто вопрос или беседа.

    Ответь ТОЛЬКО названием команды. Никаких лишних слов.
    Текст пользователя: "{user_text}"
    """

    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt},
    ])

    return response['message']['content'].strip().lower()