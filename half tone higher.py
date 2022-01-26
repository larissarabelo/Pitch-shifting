import os
import librosa
import IPython.display as ipd
#half tone higher
from IPython.display import Audio
y, sr=librosa.load("audio.wav", sr=None)
wav_pitch_sf = librosa.effects.pitch_shift(y,sr,n_steps=1)
ipd.Audio(wav_pitch_sf,rate=sr)
