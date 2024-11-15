import whisper 

class WhisperTranscribator:

    def __init__(self, model_type="small"):
        self.model = whisper.load_model(model_type)
    
    def __call__(self, filename):
        transcription = self.model.transcribe(filename ,language="ru",task="transcribe")
        return transcription
