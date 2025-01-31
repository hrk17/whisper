from fastapi import APIRouter, File, UploadFile
from backend.src.services.whisper import WhisperService
from backend.src.models.audio_request import AudioRequest

router = APIRouter()
whisper_service = WhisperService()

@router.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Receives an audio file via POST request and returns its transcription.

    Args:
        file (UploadFile): The uploaded audio file.

    Returns:
        JSON response with the transcribed text.
    """

    audio_bytes = await file.read()

    # Pass the bytes to WhisperService for transcription
    transcription = whisper_service.transcribe(audio_bytes)
    return {"transcription": transcription}

@router.get("/test/")
async def test():
    return "Success"