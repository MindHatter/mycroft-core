from mycroft.tts import TTSFactory

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
text = 'Привет. Что такое Медитация? Медитация и Здоровье'
tts = TTSFactory.create()
tts.get_tts(text, current_dir+'/test.wav')
