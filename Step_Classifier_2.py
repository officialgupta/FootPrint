# IMPORTS
from matplotlib.mlab import find
import numpy as np
import math, wave, pyaudio

CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2 # Look at this
RATE = 44100

percent = 0.03

PEOPLE = {
    "Brandon" : 1281,
    "Arvind" : 6481,
    "Bella" : 5566,
 }


def Pitch(signal):
    signal = np.fromstring(signal, 'Int16')
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing)) # difference of adjacent numbers
    frequency = round(len(index) *RATE /(2*np.prod(len(signal))))

    return frequency

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = CHUNK)

def Identify(data):
    FREQ = Pitch(data)

    for key in PEOPLE:
        if PEOPLE[key]*(1 - percent) <= FREQ <= PEOPLE[key]*(1 + percent):
            print "This is %s walking" % key
        else:
            print FREQ


for i in range(0, RATE/ CHUNK * 10):
    data = stream.read(CHUNK)
    Identify(data)