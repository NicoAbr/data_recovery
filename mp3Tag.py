import pathlib
import functions as f
import numpy as np
unNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

# using function to get all WAVE header
idx_list = f.getIdx(hdData, b'TAG')
print(idx_list)

framesynIdx = []
for idx in range(len(hdData)):
	if (hdData[idx] == 0xff and (hdData[idx+1] & 0xe0) == 0xe0):
		framesynIdx.append(idx)

		
print(len(framesynIdx))

print((441087/38)/60)