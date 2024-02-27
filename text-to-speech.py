import locale
from gtts import gTTS
import os

language = locale.getdefaultlocale()[0]

languages = ['en', 'fr','zh-CN','pt','es']


for lang in languages:
    tts = gTTS(text='Hello world', lang=lang)
    tts.save(f'output_{lang}.mp3')
    os.system(f'output_{lang}.mp3')
