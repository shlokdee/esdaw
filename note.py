import numpy as np
import sounddevice as sd

samp_rate=48000


def playnote(midinote, duration=1.0):
    t=np.arange(int(samp_rate*duration))/samp_rate
    sd.play(0.2*np.sin(2*np.pi*(440* 2**((midinote - 69) / 12))*t), samplerate=samp_rate)
    sd.wait()

