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
print(idx_list)
for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)
		data = file.read(int.from_bytes(filelen, "little"))

		print(idx_list.index(element))
		print(filetype)
		print(filelen)
		print(rifftype)

	new_file = pathlib.Path("avifile"+str(idx_list.index(element)+1)+".avi")

	with new_file.open('wb') as file:
		file.write(filetype)
		file.write(filelen)
		file.write(rifftype)
		file.write(data)

# new_idx = []
# idx_list = f.getIdx(hdData, 0xff)	
# for element in idx_list:
# 	if hdData[element+1] == 0xd8:
# 		new_idx.append(element+1)
# print(new_idx)
# # idx_list = f.getIdx(hdData[my_ints], 0xd8)
# # print(idx_list)
# funktion starts with, dann auch follow by oder so?