import wave
from VALID import ny
import subprocess
import os

def direct():
    while True:
        dire = input("Enter directory: ")
        if os.path.isdir(dire):
            os.chdir(dire)
            break
        print("DIRECTORY NOT FOUNDED")

def filefind():
    while True:
        filee=(input("Enter wav file: "))
        if filee in os.listdir():
            return filee
            break
        print("FILE NOT FOUNDED")

while True:
    print("**************WAV INFO**************\n")
    direct()
    file=filefind()
    with wave.open(file) as w:
        framerate = w.getframerate()
        frames = w.getnframes()
        channels = w.getnchannels()
        width = w.getsampwidth()
        data = len(w.readframes(frames))
        t=""
        if channels==1:
            t=" (Mono)"
        else:
            t=" (Stereo)"
                
        print('\nSampling Rate: ',framerate, 'Hz')
        print('Length: ',frames, 'samples')
        print('Channels: ',channels,t)
        print('Sample Width: ',width, 'bytes')
        print('Buffer Size: ',data, 'bytes\n')

        conti=ny(input('Continue?: '))
        if conti=="n":
            break
        subprocess.call(["cmd.exe","/C","cls"])
