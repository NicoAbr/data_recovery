# Find JPG
import pathlib
import functions as f
import numpy as np
unNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

headerIdx = []
for idx in range(len(hdData)):
	if (hdData[idx] == 0xff and 
		hdData[idx+1] == 0xd8 and
		hdData[idx+2] == 0xff and
		hdData[idx+3] == 0xe0 and
		hdData[idx+4] == 0x00 and
		hdData[idx+5] == 0x10 and
		hdData[idx+6] == 0x4a and
		hdData[idx+7] == 0x46 and
		hdData[idx+8] == 0x49 and
		hdData[idx+9] == 0x46 and
		hdData[idx+10] == 0x00):
		headerIdx.append(idx)
		
print(headerIdx)

# using function to get all WAVE header
#idx_list = f.getIdx(hdData, b'JFIF')
#print(idx_list)