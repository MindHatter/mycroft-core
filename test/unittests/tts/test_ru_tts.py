import unittest
from mycroft.tts import TTS, TTSValidator
from mycroft.tts.yandex_tts import YandexTTSValidator


class TestTTS(unittest.TestCase):
    def test_yandex_tts_conntection(self):
        validator = YandexTTSValidator(TTSValidator)
        validator.validate_connection()
        self.assertEqual(validator.validate_connection(),True)