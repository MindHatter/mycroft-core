from mycroft.configuration import Configuration
from mycroft.tts import TTS, TTSValidator
from mycroft.util.log import LOG

class AbkTTS(TTS):
    def __init__(self, lang, config):
        super(AbkTTS, self).__init__(lang, config, AbkTTSValidator(
            self), 'wav')

    def get_tts(self, sentence, wav_file):
        import requests
        abk_url = '***'
        r = requests.get(abk_url + '/tts', params={'query': sentence, 'voice': self.voice})
        with open(wav_file, 'wb') as outfile:
            outfile.write(r.content)
        LOG.debug('Abk TTS: speech result in "' + wav_file + '"')
        return (wav_file, None)  # No phonemes

class AbkTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(AbkTTSValidator, self).__init__(tts)

    def validate_lang(self):
        # TODO
        pass

    def validate_connection(self):
        try:
            config = Configuration.get()
            tts = AbkTTS('ru-RU', config)
            tts.get_tts('Привет', tts.filename)
            import os.path
            if os.path.isfile(tts.filename):
                return True
            else:
                return False
        except:
            raise Exception(
                'AbkTTS server could not be verified. Please check your '
                'internet connection.')

    def get_tts_class(self):
        return AbkTTS
