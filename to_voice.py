import translate as t
from gtts import gTTS
from playsound import playsound
def main():
    lang=input("Which language you want to translate: ")
    sentence=t.func(lang)
    record=gTTS(text=sentence, lang=lang, slow="False")
    record.save("record.mp3")
    playsound("record.mp3")