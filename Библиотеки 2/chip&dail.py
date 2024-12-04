import wave
import struct

name, number = input(), int(input())
source = wave.open(name, mode="rb")
dest = wave.open(name, mode="wb")

dest.setparams(source.getparams())
frames_count = source.getnframes() 

data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
newdata = []
deleted = data[::number]

for frame in data:
    if not data in deleted: newdata.append(data)
    
newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata) 

dest.writeframes(newframes) 
source.close()
dest.close()