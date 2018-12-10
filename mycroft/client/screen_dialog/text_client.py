import sys
from mycroft.tts import TTS

import time
from threading import Thread, Lock
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.util.log import LOG


def handle_speak(event):
    pass
    global screen
    utterance = event.data.get('utterance')
    utterance = TTS.remove_ssml(utterance)
    with open('answer', 'w') as file:
        file.write(utterance)
    ##screen.set_question(utterance)
    #screen.refresh()

def handle_utterance(event):
    pass
    global screen
    utterance = event.data.get('utterances')[0]
    with open('question', 'w') as file:
        file.write(utterance)
    #screen.set_answer(utterance)
    #screen.refresh()


def handle_message(event):
    pass


#from mycroft.client.screen_dialog.screen_face import ScreenFace
screen = None
i=0

class LogMonitorThread(Thread):
    def __init__(self):
        global screen
        Thread.__init__(self)
        #screen = ScreenFace()


    def run(self):
        global screen
        global i
        while True:
            try:
                i = i+1
                print(i)
                #screen.contunue_game_loop()
            except KeyboardInterrupt as e:
                LOG.exception(e)
                #screen.close_window()
                sys.exit()
            finally:
                time.sleep(0.3)



def start_log_monitor():
    thread = LogMonitorThread()
    thread.setDaemon(True)
    thread.start()
