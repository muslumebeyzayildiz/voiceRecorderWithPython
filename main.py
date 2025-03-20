import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import numpy as np

# Örnekleme frekansı (Hz)
SAMPLE_RATE = 44100  # Genellikle 44100 veya 48000 kullanılır

# Kayıt süresi (saniye)
DURATION = 5

# Kanal sayısı (1: Mono, 2: Stereo)
CHANNELS = 2

def record_audio(duration, sample_rate, channels):
    """
    Belirtilen süre, örnekleme frekansı ve kanal sayısı ile sesi kaydeder.
    """
    print("Kayıt başlıyor...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype=np.int16)
    sd.wait()  # Kayıt tamamlanana kadar bekle
    print("Kayıt tamamlandı.")
    return recording

# Ses kaydını başlat
audio_data = record_audio(DURATION, SAMPLE_RATE, CHANNELS)

# SciPy ile kaydetme
write("recording_scipy.wav", SAMPLE_RATE, audio_data)
print("Kayıt 'recording_scipy.wav' olarak kaydedildi.")

# Wavio ile kaydetme
wv.write("recording_wavio.wav", audio_data, SAMPLE_RATE, sampwidth=2)
print("Kayıt 'recording_wavio.wav' olarak kaydedildi.")





