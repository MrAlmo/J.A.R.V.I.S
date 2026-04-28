import os
import queue
import sounddevice as sd
import vosk
import json
import sys
import threading
import pyautogui
import time
import psutil
from pyautogui import moveTo
from brain import get_ai_response
from J_sound import *



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model")

data_queue = queue.Queue()

def callback(indata, frames, time, status):
    data_queue.put(bytes(indata))

def listen_open():
    model = vosk.Model(MODEL_PATH)
    rec = vosk.KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print("Vosk Listening...")

        while stopper:
            data = data_queue.get()

            try:
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    command = result.get('text', '').lower()

                    if command:
                        print(f"Вы сказали: {command}")
                        proceed_commnad(command)




            except FileExistsError:
                print(" File Vosk not exist ")


def proceed_commnad(command):

    stop_words = ["тихо", "замолчи", "хватит", "молчать"]

    if any(word in command for word in stop_words):
        jarvis.stop()
        return

    game = "dota2.exe"

    if "сосать" in command or "открыть доту" in command:
        jarvis.speak("Хорошо сэр, открываю Доту")
        file_path = "C:/Users/MrAlmo/Desktop/Dota 2.url"
        open_file(file_path)


    elif "запустить рейтинг" in command and is_prog_running(game):
        jarvis.speak("Сэр, запускаю рейтинговую игру. Удачи!")
        find_image_click("media/play_button.png", confidence=0.9)
        if find_image_location("media/raiting.png", minSearchTime=0.5) is not None:

            if find_image_click("media/find_game_button.png", confidence=0.9, minSearchTime=0.5):
                pass
            else:
                find_image_click("media/find_game_button_1.png", confidence=0.9, minSearchTime=0.5)


        else:
            print("small error")

            if find_image_click("media/raiting_gray.png", minSearchTime=0.5):

                if find_image_click("media/find_game_button.png", confidence=0.9, minSearchTime=0.5):
                    pass
                else:
                    find_image_click("media/find_game_button_1.png", confidence=0.9, minSearchTime=0.5)

            else:
                print("second small error")

    elif "кастом" in command and is_prog_running(game):
        jarvis.speak("Пытаюсь открыть кастомку")
        my_list = [(1134, 30), (627, 86), (405, 313), (1495, 560), (850, 660), (1011, 840), (1729, 1032)]
        for i in my_list:
            pyautogui.moveTo(i[0], i[1])
            pyautogui.click(interval=0.3)
            if i[0] == 850 and i[1] == 660:
                pyautogui.write("123")
        pyautogui.click()


    elif "сила" in command and is_prog_running(game):
        jarvis.speak("Выбираю вашего героя")
        pyautogui.write("sylla")
        if find_image_click("media/sylla_1.png", confidence=0.6):
            pyautogui.moveTo(1481, 825)
            pyautogui.click()

        else:
            print("sylla error")

    elif "принять приглашение" in command and is_prog_running(game):
        jarvis.speak("Принимаю приглашение")
        find_image_click("media/invitation_button.png", confidence=0.9)

    elif "отклонить приглашение" in command and is_prog_running(game):
        jarvis.speak("Отклоняю приглашение")
        find_image_click("media/decline_button.png", confidence=0.9)

    elif "отменить поиск" in command and is_prog_running(game):
        jarvis.speak("Отменяю поиск")
        find_image_click("media/cancel.png", confidence=0.9)

    elif "лобби" in command and is_prog_running(game):
        jarvis.speak("Запускаю лобби")
        find_image_click("media/play_button.png", confidence=0.9)
        if find_image_click("media/lobby_gray.png", confidence=0.9, region=(1528, 85, 338, 885), minSearchTime=0.5):
            find_image_click("media/lobby_create.png", confidence=0.9, minSearchTime=0.5)
            find_image_click("media/start_game_button.png", confidence=0.9, minSearchTime=0.5)
        elif find_image_click("media/lobby_create.png", confidence=0.9, minSearchTime=0.5):
            print("lobby_gray error")
            find_image_click("media/start_game_button.png", confidence=0.9, minSearchTime=0.5)
        else:
            print("lobby_create error")

    elif ("я отсосал" in command or "закрыть доту" in command) and is_prog_running(game):
        jarvis.speak("Хорошо сэр, закрываю доту")
        close_file(game)
        #os._exit(0)

    elif "облава" in command:
        jarvis._internal_speak("Останавливаю программу, До новых встреч!")
        global stop_flag
        stop_flag = False
        os._exit(0)

    elif "скип" in command:
        stop()

    elif "открой с тим" in command or "открой с тeм" in command :
        file_path = "C:/Users/Public/Desktop/Steam.lnk"
        open_file(file_path)

    elif "смена на первый" in command:
        file_path = "C:/Users/Public/Desktop/Steam.lnk"
        open_file(file_path)
        location = find_image_location("media/Monitor.png", confidence=0.9, minSearchTime=1)
        if location is not None:
            monitorL = pyautogui.center(location)
            x, y = monitorL.x, monitorL.y
            new_x = x - 65
            pyautogui.moveTo(new_x,y, duration=0.2)
            pyautogui.click()

            find_image_click("media/anotherAcc.png", minSearchTime=0.5, confidence=0.9)
            find_image_click("media/NextButton.png", minSearchTime=0.5, confidence=0.9)
            find_image_click("media/FirstAcc.png", minSearchTime=10, confidence=0.9)

        else:
            print(f"Twink error")

    elif "смена на второй" in command:
        file_path = "C:/Users/Public/Desktop/Steam.lnk"
        open_file(file_path)

        if find_image_click("media/MrAlmo.png", confidence=0.9, minSearchTime=0.5):
            find_image_click("media/anotherAcc.png", minSearchTime=0.5, confidence=0.9)
            find_image_click("media/NextButton.png", minSearchTime=0.5, confidence=0.9)
            find_image_click("media/secondAcc.png", minSearchTime=10, confidence=0.9)

        else:
            print("MrAlmo error")

    else:
        # print("Sorry, I don't understand.")
        print("J.A.R.V.I.S working...")
        answer = get_ai_response(command)
        jarvis.speak(answer)

def open_file(path):
    if os.path.exists(path):
        print("Path exists, opening")
        os.startfile(path)
        #stop()
    else:
        print("Path doesn't exist, opening")

def close_file(file):
    if is_prog_running(file):
        os.system(f'taskkill /f /im {file}')
    else:
        print("Program not running.")

def is_prog_running(prog_name):
    for proc in psutil.process_iter(['name']):
        try:
            if prog_name.lower() in proc.info['name'].lower():
                return True
        except Exception:
            pass
    return False

def find_image_location(image: str, confidence : float = 0.8, minSearchTime: float =0, region=None):
    try:
        location = pyautogui.locateOnScreen(image, confidence=confidence, minSearchTime=minSearchTime, grayscale=True, region=region)
        return location
    except Exception as e:
        print(f"Error {e}")
    return None

def find_image_click(image:str, confidence: float = 0.8, minSearchTime: float = 0, region=None):

    location = find_image_location(image, confidence=confidence, minSearchTime=minSearchTime, region=region)
    if location is not None:
        center = pyautogui.center(location)
        pyautogui.moveTo(center, duration=0.2)
        pyautogui.click()
        return True
    return False

stopper = True
stop_flag = True

def stop():
    global stopper
    stopper = False


# def accept_button():
#     while stop_flag:
#         time.sleep(3)
#         find_press()


if __name__ == "__main__":
    threading.Thread(target=listen_open).start()

    # threading.Thread(target=stop_f).start()

    # threading.Thread(target=accept_button).start()

