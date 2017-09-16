from matplotlib.mlab import find
import pyaudio
import numpy as np
import math
import wave

chunk = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 20


def Pitch(signal):
    signal = np.fromstring(signal, 'Int16')
    crossing = [math.copysign(1.0, s) for s in signal]

    index = find(np.diff(crossing))

    print index

    f0=round(len(index) *RATE /(2*np.prod(len(signal))))

    return f0;


p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
channels = CHANNELS,
rate = RATE,
input = True,
output = True,
frames_per_buffer = chunk)

wf = wave.open('Sample4.wav', 'rb')
data = wf.readframes(chunk)
Frequency=Pitch(data)
print "%f Frequency" %Frequency


# Arvind Sample 1 : Frequency of 6481
# Brandon Sample 1 : Frequency of 1281
# Hello Sample 2: 10518
# Hello Sample 3: 10702
# Hello Sample 4: 10782
# Hello Sample 5: 10551
# Hello Sample 6 (Brandon): 10745
# Sample1: 1313
# Sample2: 6115
# Bella Samples: 5566
# Sample3 : 5765
# Sample4: 1270

