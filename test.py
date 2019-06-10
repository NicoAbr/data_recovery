# finding PNG files
import pathlib
import functions as f
import numpy as np
runNo = 1
hd = pathlib.Path('data_deleted.img')

unNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()
	
# using function to get all PNG header
#idx_list = f.getIdx(hdData, b'')
#print(idx_list)

headerIdx = []
for idx in range(len(hdData)):
	if (hdData[idx] == 137 and 
		hdData[idx+1] == 80 and
		hdData[idx+2] == 78 and
		hdData[idx+3] == 71 and
		hdData[idx+4] == 13 and
		hdData[idx+5] == 10 and
		hdData[idx+6] == 26 and
		hdData[idx+7] == 10):

		headerIdx.append(idx)
		
print(headerIdx)