#struct takes any data and convert to bytes format
from struct import *

#data to be stored as bytes. pack(format, values). In this case format is two integers "i" 6 and 19 and one float "f" 4.73.  See Python Documentation for pack format
packed_data = pack("iif", 6, 19, 4.73)
print(packed_data) #print or display in byte format

#shows how much memory to store
print(calcsize("i"))
print(calcsize("f"))
print(calcsize("iif"))

#convert byte to normal readable.  unpack(format, values in byte format)
original_data = unpack("iif", packed_data)
print(original_data)

#quicker way
print(unpack("iif", packed_data))