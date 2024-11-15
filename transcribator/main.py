from .whisper import WhisperTranscribator


if __name__ == "__main__":
    CFG_VIDEO_URL  = "https://disk.yandex.ru/i/qW0c5o0duhkt5w" 
    transcribator = WhisperTranscribator()
    
    transcribator("video_file.mp4")