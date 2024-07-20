import speech_to_text as s
from textblob import TextBlob
from langdetect import detect
def func(to):
   text=s.record_and_translate_to_text()
   t=TextBlob(text)
   lang=detect(t)
   sentence=TextBlob(t)
   sentence2=sentence.translate(from_lang=lang, to=to)
   return sentence2