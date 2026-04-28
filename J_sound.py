import pyttsx3
import threading


class JarvisVoice:
    def __init__(self):
        self.stop_event = False

    def speak(self, text):
        print(f"JARVIS says: {text}")
        self.stop_event = False

        threading.Thread(target=self._internal_speak, args=(text,), daemon=True).start()

    def _internal_speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)


        voices = engine.getProperty('voices')
        for voice in voices:
            if "Russian" in voice.name or "ru" in voice.id.lower():
                engine.setProperty('voice', voice.id)
                break


        engine.say(text)
        engine.runAndWait()

        engine.stop()

    def stop(self):
        temp_engine = pyttsx3.init()
        temp_engine.stop()
        print("Interruption")



jarvis = JarvisVoice()