import pathlib
import functions as f
import numpy as np
runNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

# using function to get all WAVE header
idx_list = f.getIdx(hdData, b'WAVE')

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)
		data = file.read(int.from_bytes(filelen, "little"))

	new_file = pathlib.Path("wavfile"+str(runNo)+".wav")
	runNo += 1

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

		if filetype == b'RIFF':
			data = file.read(int.from_bytes(filelen, "little"))

			print(idx_list.index(element))
			print(filetype)
			print(filelen)
			print(rifftype)

			new_file = pathlib.Path("avifile"+str(runNo)+".avi")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(filetype)
				file.write(filelen)
				file.write(rifftype)
				file.write(data)