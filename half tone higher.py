import os
import librosa
import IPython.display as ipd
#half tone higher
from IPython.display import Audio
y, sr=librosa.load("PARTICIPANTE_9.wav", sr=None)
wav_pitch_sf = librosa.effects.pitch_shift(y,sr,n_steps=1)
#plot_spec(data=wav_pitch_sf,sr=sr,title=f'Pitch shifting by {-5} steps',fpath="C:/Users/larit/Desktop/Segurança da Informação/PIBIC/")
ipd.Audio(wav_pitch_sf,rate=sr)
