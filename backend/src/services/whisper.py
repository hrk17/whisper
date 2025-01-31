
import io
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
import torch

class WhisperService:
    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
        self.model.config.forced_decoder_ids = None

    def transcribe(self, audio_bytes: bytes):
        audio_buffer = io.BytesIO(audio_bytes)
        
        # Load the audio file
        waveform, sample_rate = torchaudio.load(audio_buffer)

        if sample_rate != 16000:
            transform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            waveform = transform(waveform)
        
        if waveform.shape[0] > 1:
            waveform = torch.mean(waveform, dim=0, keepdim=True)  # Convert to mono -- weird issues with dual channel


        chunk_size = 30 * 16000  # 30 seconds * 16000 samples per second
        waveform_np = waveform.squeeze().numpy()

        chunks = [waveform_np[i : i + chunk_size] for i in range(0, len(waveform_np), chunk_size)]

        # process in chunks
        full_transcription = []
        for chunk in chunks:
            input_features = self.processor(chunk, sampling_rate=16000, return_tensors="pt").input_features
            with torch.no_grad():
                predicted_ids = self.model.generate(input_features, max_new_tokens=256)
            transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
            full_transcription.append(transcription)

        return " ".join(full_transcription)