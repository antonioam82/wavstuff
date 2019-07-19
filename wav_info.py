import wave
from VALID import ny
import subprocess

while True:
    print("*********WAV INFO*********\n")
    file=input("Enter wav file: ")
    with wave.open(file) as w:
        framerate = w.getframerate()
        frames = w.getnframes()
        channels = w.getnchannels()
        width = w.getsampwidth()
        
        print('\nSampling Rate: ',framerate, 'Hz')
        print('Length: ',frames, 'samples')
        print('Channels: ',channels)
        print('Sample Width: ',width, 'bytes\n')

        conti=ny(input('Continue?: '))
        if conti=="n":
            break
        subprocess.call(["cmd.exe","/C","cls"])
