
from mycroft.tts import TTS, TTSValidator
from mycroft.util.log import LOG
import base64, requests

class CrtTTS(TTS):
    def __init__(self, lang, config):
        super(CrtTTS, self).__init__(lang, config, CrtTTSValidator(
            self), 'wav')

    def get_tts(self, sentence, wav_file):
        credentials = {}
        crt_url = 'https://cp.speechpro.com/vktts/rest'
        # запрос без сессии
        crt_sessionless_path = '/v1/synthesize/sessionless'
        voice_name = self.config.get("voice_name", "Julia")

        r = requests.post(crt_url + crt_sessionless_path, json={
            "credentials": credentials,
            "voice_name": voice_name,
            "text": {"mime": "text/plain", "value": sentence},
            "audio": "audio/wav"
        })
        if r.status_code == 200:
            sound = base64.decodebytes(bytes(r.json()['data'], 'utf-8'))
            with open(wav_file, 'wb') as outfile:
                outfile.write(sound)
        else:
            LOG.error('CRT STT ERROR RESPONSE:'+str(r.json()))
        return (wav_file, None)  # No phonemes


class CrtTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(CrtTTSValidator, self).__init__(tts)

    def validate_lang(self):
        # TODO
        pass

    def validate_connection(self):
        try:
            from mycroft.configuration import Configuration
            config = Configuration.get()
            tts = CrtTTS('ru-RU', config)
            tts.get_tts('Привет', tts.filename)
            import os.path
            if os.path.isfile(tts.filename):
                return True
            else:
                return False
        except:
            raise Exception(
                'CrtTTS server could not be verified. Please check your '
                'internet connection.')

    def get_tts_class(self):
        return CrtTTS
