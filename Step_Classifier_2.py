# IMPORTS
from matplotlib.mlab import find
import matplotlib.pyplot as plt
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


plt.ion()

def Pitch(signal):
    signal = np.fromstring(signal, 'Int16')
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing)) # difference of adjacent numbers
    frequency = round(len(index) *RATE /(2*np.prod(len(signal))))


    p = np.log10(np.abs(np.fft.rfft(signal)))
    f = np.linspace(0, RATE/2.0, len(p))
    plt.clf()
    plt.axis([0,2049,0,10])
    plt.plot(p)
    plt.pause(0.0001)

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
   


#for i in range(0, RATE/ CHUNK * 30):
while True:
    data = stream.read(CHUNK)
    Identify(data)
