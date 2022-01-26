import os
import librosa
import IPython.display as ipd


#one tone higher
from IPython.display import Audio
y, sr=librosa.load("audio.wav", sr=None)
wav_pitch_sf = librosa.effects.pitch_shift(y,sr,n_steps=2)
ipd.Audio(wav_pitch_sf,rate=sr)
