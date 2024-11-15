from setuptools import setup, find_packages

setup(
    name="audio/video Transcribator",  # Название вашего модуля
    version="0.1.2",  # Версия
    packages=find_packages(),  # Автоматически находит все пакеты
    install_requires=[  # Зависимости, если они есть
        "openai-whisper"
    ],
    url="https://github.com/ai-collab-incubator/transcribator",  # URL вашего репозитория
    author="pauchai",
    author_email="paul.khimyack@gmail.com",
    description="For transcribe audio video",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)