import pathlib

import numpy as np

unNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()
	


x = hdData[1]
y = hdData[2]
z =  x*256 + y

print(z)
print(x)
print(y)



#blockLength = int.from_bytes(z, "big")



#print(blockLength)