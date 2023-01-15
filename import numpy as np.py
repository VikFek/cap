import numpy as np
import sounddevice as sd

# Define the target frequencies for each string
e_string = 329.63
A_string = 440
D_string = 587.33
G_string = 783.99
B_string = 987.77
e_string_2 = 1318.51

samplerate = 44100
duration = 3

while True:
    string = input("Which string would you like to tune (e, A, D, G, B, e): ")
    if string == "e":
        sd.play(np.sin(2*np.pi*e_string*np.arange(samplerate*duration)/samplerate), samplerate)
    elif string == "A":
        sd.play(np.sin(2*np.pi*A_string*np.arange(samplerate*duration)/samplerate), samplerate)
    elif string == "D":
        sd.play(np.sin(2*np.pi*D_string*np.arange(samplerate*duration)/samplerate), samplerate)
    elif string == "G":
        sd.play(np.sin(2*np.pi*G_string*np.arange(samplerate*duration)/samplerate), samplerate)
    elif string == "B":
        sd.play(np.sin(2*np.pi*B_string*np.arange(samplerate*duration)/samplerate), samplerate)
    elif string == "e2":
        sd.play(np.sin(2*np.pi*e_string_2*np.arange(samplerate*duration)/samplerate), samplerate)
    else:
        print("Invalid input. Please enter a valid string.")
