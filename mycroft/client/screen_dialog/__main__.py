from .text_client import (
        start_log_monitor
    )
from threading import Thread
from mycroft.tts import TTS

def handle_speak(event):
    utterance = event.data.get('utterance')
    utterance = TTS.remove_ssml(utterance)
    with open('answer', 'w') as file:
        file.write("11" + utterance)
    ##screen.set_question(utterance)
    #screen.refresh()

def handle_utterance(event):
    utterance = event.data.get('utterances')[0]
    with open('question', 'w') as file:
        file.write("11"+utterance)
    #screen.set_answer(utterance)
    #screen.refresh()


def handle_message(event):
    pass

def main():

    # Monitor system logs
    #start_log_monitor()
    from mycroft.messagebus.client.ws import WebsocketClient
    bus = WebsocketClient()  # Mycroft messagebus connection
    bus.on('speak', handle_speak)
    bus.on('message', handle_message)
    bus.on('recognizer_loop:utterance', handle_utterance)

    def connect():
        bus.run_forever()

    event_thread = Thread(target=connect)
    event_thread.setDaemon(True)
    event_thread.start()



if __name__ == "__main__":
    main()
