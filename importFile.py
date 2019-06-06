import pathlib
import functions as f
import numpy as np
runNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

# using function to get all WAVE header
idx_list = f.getIdx(hdData, b'WAVE')
print(idx_list)

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)

		if filetype == b'RIFF':
			data = file.read(int.from_bytes(filelen, "little"))

			# write data to new file
			new_file = pathlib.Path("wavfile"+str(runNo)+".wav")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(filetype)
				file.write(filelen)
				file.write(rifftype)
				file.write(data)

# using function to get all AVI header
idx_list = f.getIdx(hdData, b'AVI ')
print(idx_list)
for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)

		# find only RIFF AVI data
		if filetype == b'RIFF':
			data = file.read(int.from_bytes(filelen, "little"))

			print(idx_list.index(element))
			print(filetype)
			print(filelen)
			print(rifftype)

			# write data to new file
			new_file = pathlib.Path("avifile"+str(runNo)+".avi")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(filetype)
				file.write(filelen)
				file.write(rifftype)
				file.write(data)

#idx_diff = idx_list[1]-idx_list[0]
#print(idx_diff)

	with new_file.open('wb') as file:
		file.write(filetype)
		file.write(filelen)
		file.write(rifftype)
		file.write(data)

start_idx = []
idx_list = f.getIdx(hdData, 0xd8)# 255 216 0xff und 0xd8
for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-1)
		potential_start = file.read(1)
		# print(potential_start)
		if potential_start == 0xff:
			start_idx.append(element-1)

# for element in idx_list:
# 	if hdData[element+1] == 0xd8:
# 		new_idx.append(element+1)
# print(new_idx)
# # idx_list = f.getIdx(hdData[my_ints], 0xd8)
print(start_idx)
# funktion starts with, dann auch follow by oder so?
