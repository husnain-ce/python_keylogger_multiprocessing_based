import os, sounddevice as sd
from scipy.io.wavfile import write

class Mic:
    def __init__(self):
        self.file_path = os.getcwd() + "\\" + "audio.wav" 
        self.microphone_time = 60

    def microphone(self,mic_resp):
        while True:  
            check = mic_resp.value  
            fs = 44100
            myrec = sd.rec(int(self.microphone_time * fs) , samplerate= fs , channels = 2)
            sd.wait()
            write(self.file_path,fs , myrec)

            if check:
                break