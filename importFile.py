import pathlib
import functions as f
# import numpy as np
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

# using function to get all WAVE header
idx_list = f.getIdx(hdData, b'WAVE')
# print(idx_list)

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)
		data = file.read(int.from_bytes(filelen, "little"))

	new_file = pathlib.Path("wavfile"+str(idx_list.index(element)+1)+".wav")

	with new_file.open('wb') as file:
		file.write(filetype)
		file.write(filelen)
		file.write(rifftype)
		file.write(data)

idx_list = f.getIdx(hdData, b'AVI ')

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)
		data = file.read(int.from_bytes(filelen, "little"))

	new_file = pathlib.Path("avifile"+str(idx_list.index(element)+1)+".wav")

	with new_file.open('wb') as file:
		file.write(filetype)
		file.write(filelen)
		file.write(rifftype)
		file.write(data)