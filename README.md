# FootPrint
An app that recognises footprints

## Inspiration
We were inspired to combine our common interests in IoT to create an application that improved lives. Creating a simple, but diverse application that could improve IoT integration in the home.

## What it does
A low power application that can accurately identify a home member based upon the sound of their footsteps.

## How we built it
We recorded 400 footsteps each for 2 different people, and used audacity to split that into 400 individual WAVE files. Using pyAudioAnalysis the data was fed into a classifier with SVM, which we can then use to determine who is walking. 

## Challenges we ran into
We first tried to accomplish the task by looking only at the most common frequencies in the sound. This worked, but only under the conditions of around 20 seconds of audio. It was highly influenced by external noise. We solved this by using a classifier and machine learning. 

## Accomplishments that we're proud of
The confidence level with which the SVM outputs from the classifier. 

## What we learned
How to use python to analyse audio data. And use the parameters from this for machine learning and neural net analysis for classification.

## What's next for FootPrint
-Using a fixed position of sensors and enough time, a custom neural net training could be implemented. We began an implementation using TensorFlow and Google Cloud which would work given enough footstep sound data, and would be scalable. Using this we should be able to increase confidence level.

-Also, integration with IoT; with usages including security for unknown footsteps being detected, and integration with other devices such as locks, lights, heating and music which can all be controlled automatically by human detection. Zigbee connection would be strongly considered here.
