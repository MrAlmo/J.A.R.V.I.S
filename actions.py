from J_sound import *
import os

def action_open_dota():
    jarvis.speak("Запускаю Доту, сэр. Удачной игры.")
    file_path = "C:/Users/MrAlmo/Desktop/Dota 2.url"
    os.startfile(file_path)

def action_close_dota():
    jarvis.speak("Закрываю игру. Надеюсь, вы победили.")
    os.system('taskkill /f /im dota2.exe')

def action_stop_program():
    jarvis._internal_speak("Останавливаю программу, До новых встреч!")
    os._exit(0)

ACTIONS = {
    "open_dota": action_open_dota,
    "close_dota": action_close_dota,
    "stop_program": action_stop_program,
    "none": lambda: None
}