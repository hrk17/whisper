# whisper
Speech transcription

To run backend:
poetry install

eval $(poetry env activate)
poetry run uvicorn backend.src.main:app