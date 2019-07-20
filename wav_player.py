import winsound
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
    direct()
    file=filefind()
    print("PLAYING: ",file)
    winsound.PlaySound(file,winsound.SND_ALIAS)
    
    print("FINISH\n")
    
    conti=ny(input('Continue?: '))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
