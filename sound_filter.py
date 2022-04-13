import wave
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft, fftshift, ifft
from scipy import signal
from sys import stdout


#read the audio file
file_name = input("Audio file name -> ").strip() + ".wav"
low_cut_off = int(input( "Enter lower cut off frequancy  -> "))
high_cut_off = int(input("Enter higher cut off frequancy -> "))
audio = wave.open(file_name, 'rb')

#extract data from the file
frame_rate = audio.getframerate()
nchannels = audio.getnchannels()
sampwidth = audio.getsampwidth()
nframes = audio.getnframes()

low = 2 * low_cut_off / frame_rate
high = 2 * high_cut_off /frame_rate

types = {
    0 : ['Low pass filter', 'lowpass'],
    1 : ['High pass filter', 'highpass'],
    2 : ['Band pass filter', 'bandpass'],
    3 : ['Band stop filter', 'bandstop']
}

for i in range(4):
    print(f'{i} : {types[i][0]}')

type_ = int(input("Enter the type of the filrer -> ").strip())

print(types[type_][1])

b, a = signal.butter(3, [low, high], types[type_][1], analog=False)

print("\nAudio input data\n-------------------\n")
print(f"Frame rate   -> {frame_rate} Hz")
print(f"nchannels    -> {nchannels}")
print(f"sample width -> {sampwidth}\n")


def process_chunk(start_, duration_ = 10):

    data = np.array([], dtype="int16")

    #set position of audio
    global audio
    audio.rewind()
    audio.setpos(start_ * frame_rate * duration_)
    
    percentage = audio.tell() / audio.getnframes() * 100
    percentage = "Filtering percentage -> {:.2f} %".format(percentage)
    stdout.write('\r' + percentage)
    stdout.flush() # important

    for _ in range(duration_):
        tempFrame = np.asarray(np.frombuffer(audio.readframes(frame_rate), dtype='int16'))
        if tempFrame.shape[0] == 0:
            break
        data = np.concatenate((data, tempFrame))

    output = signal.lfilter(b, a, data)
    filtered_bytes = output.astype("int16").tobytes()

    return filtered_bytes



def main():
    duration = nframes / frame_rate

    destin = wave.open(f"{low_cut_off} Hz {high_cut_off} Hz filteredSound.wav", 'wb')
    destin.setnchannels(nchannels)
    destin.setframerate(frame_rate)
    destin.setsampwidth(sampwidth)

    for i in range(int(duration / 10) + 1):
        result = process_chunk(i)
        destin.writeframes(result)

    percentage = "Filtering percentage -> {:.2f} %".format(100)
    stdout.write('\r' + percentage)
    stdout.flush() # important

    destin.close()


if __name__ == "__main__":
    main()



