import whisper

class WhisperTranscriber:
    def __init__(self, model_type="small", default_language="ru", default_task="transcribe"):
        """
        Инициализация класса с заданным типом модели и параметрами по умолчанию.
        :param model_type: Тип модели Whisper, например "tiny", "base", "small", "medium", "large".
        :param default_language: Язык по умолчанию, например "ru", "en".
        :param default_task: Задача по умолчанию, например "transcribe" или "translate".
        """
        self.model = whisper.load_model(model_type)
        self.default_language = default_language
        self.default_task = default_task
    
    def __call__(self, filename, **kwargs):
        """
        Транскрибирует аудиофайл с использованием заданных параметров.
        :param filename: Путь к аудиофайлу.
        :param kwargs: Дополнительные параметры для модели Whisper.
            Если 'language' и 'task' не переданы, используются значения по умолчанию.
        :return: Результат транскрипции.
        """
        # Добавляем параметры по умолчанию, если они не указаны в kwargs
        kwargs.setdefault("language", self.default_language)
        kwargs.setdefault("task", self.default_task)
        
        transcription = self.model.transcribe(filename, **kwargs)
        return transcription
