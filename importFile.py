import pathlib
import numpy as np
hd = pathlib.Path('data_deleted.img')


with hd.open('rb') as file:
	hdData = file.read()



idx = hdData.index(b'WAVE')
print(idx)

# find more than one index (from: https://stackoverflow.com/questions/...
# 			6294179/how-to-find-all-occurrences-of-an-element-in-a-list)
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

# using function to get all WAVE header
idx_list = indices(hdData, b'WAVE')
print(idx_list)


#filetype = hdData[(idx-8):(idx-4)]
#filelen = int.from_bytes(hdData[(idx-4):idx], "little")
#rifftype = hdData[idx:(idx+4)]

#print('filetype:', filetype)
#print('filelen:', filelen)
#print('rifftype:', rifftype)

#wav = hdData[(idx-8):(idx+filelen-8)]

with hd.open('rb') as file:
	file.seek(idx-8)
	filetype = file.read(4)
	filelen = file.read(4)
	rifftype = file.read(4)
	data = file.read(int.from_bytes(filelen, "little"))

new_file = pathlib.Path('NorduSonn.wav')

with new_file.open('wb') as file:
	file.write(filetype)
	file.write(filelen)
	file.write(rifftype)
	file.write(data)
