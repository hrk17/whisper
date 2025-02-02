# Relay
An audio transcription application integrating OpenAI's Whisper model.

## To run backend:
```poetry install
eval $(poetry env activate)
poetry run uvicorn backend.src.main:app
```

## To run frontend:
```npm install
npm run dev
```

## Run with docker:
```docker compose up -d```