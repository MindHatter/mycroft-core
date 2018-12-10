import sys
from mycroft.tts import TTS

import os
import os.path
import time
from threading import Thread, Lock
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.util.log import LOG


def handle_speak(event):
    global screen
    utterance = event.data.get('utterance')
    utterance = TTS.remove_ssml(utterance)
    screen.set_question(utterance)
    screen.refresh()

def handle_utterance(event):
    global screen
    utterance = event.data.get('utterances')[0]
    screen.set_answer(utterance)
    screen.refresh()


def handle_message(event):
    pass


from mycroft.client.screen_dialog.screen_face import ScreenFace
screen = None

class LogMonitorThread(Thread):
    def __init__(self):
        global screen
        Thread.__init__(self)
        screen = ScreenFace()
        bus = WebsocketClient()  # Mycroft messagebus connection
        bus.on('speak', handle_speak)
        bus.on('message', handle_message)
        bus.on('recognizer_loop:utterance', handle_utterance)

    def run(self):
        while True:
            try:
                print(1)
            except KeyboardInterrupt as e:
                # User hit Ctrl+C to quit
                print("")
            except KeyboardInterrupt as e:
                LOG.exception(e)
                screen.close_window()
                sys.exit()
            finally:
                time.sleep(0.1)


def start_log_monitor(filename):
    if os.path.isfile(filename):
        thread = LogMonitorThread()
        thread.setDaemon(False)
        thread.start()

