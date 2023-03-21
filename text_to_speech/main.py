# import speech as speech
from gtts import gTTS
from speech_text import speech_text

# import

from playsound import playsound
# speech = "/speech.txt"
audio = "new_speech.mp3"
language = 'en'
sp = gTTS(
    text=speech_text,
    lang=language, slow=False)
sp.save(audio)
playsound(audio)
