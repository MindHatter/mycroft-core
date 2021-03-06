# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from mycroft.configuration import Configuration
from mycroft.tts import TTS, TTSValidator
from yandex_speech import TTS as yaTTS
from mycroft.util.log import LOG

class YandexTTS(TTS):
    def __init__(self, lang, config):
        super(YandexTTS, self).__init__(lang, config, YandexTTSValidator(
            self), 'wav')

    def get_tts(self, sentence, wav_file):
        LOG.debug('Yandex TTS: try to make speech "'+sentence+'"')
        print('YandexTTS: '+sentence)
        tts = yaTTS(self.voice, "wav", self.config.get("token"))
        tts.generate(sentence)
        tts.save(path=wav_file)
        LOG.debug('Yandex TTS: speech result in "' + wav_file + '"')
        return (wav_file, None)  # No phonemes


class YandexTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(YandexTTSValidator, self).__init__(tts)

    def validate_lang(self):
        # TODO
        pass

    def validate_connection(self):
        try:
            config = Configuration.get()
            tts = YandexTTS('ru-RU', config)
            tts.get_tts('Привет', tts.filename)
            import os.path
            if os.path.isfile(tts.filename):
                return True
            else:
                return False
        except:
            raise Exception(
                'YandexTTS server could not be verified. Please check your '
                'internet connection.')

    def get_tts_class(self):
        return YandexTTS
