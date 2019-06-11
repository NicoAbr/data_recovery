import pathlib as p
import functions as f
import os

runNo = 1
hd = p.Path('data_deleted.img')
path = p.Path('recovered_data')
if os.path.isdir(path) == False:
	os.mkdir('recovered_data')

with hd.open('rb') as file:
	hdData = file.read()

# recover Wave files
# using function to get all WAVE header
idx_list = f.getIdx(hdData, b'WAVE')

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)

		if filetype == b'RIFF':
			data = file.read(int.from_bytes(filelen, "little"))

			# write data to new file
			new_file = p.Path("recovered_Data\wavfile"+str(runNo)+".wav")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(filetype)
				file.write(filelen)
				file.write(rifftype)
				file.write(data)

# recover AVI files			
# using function to get all AVI header
idx_list = f.getIdx(hdData, b'AVI ')
runNo = 1

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-8)
		filetype = file.read(4)
		filelen = file.read(4)
		rifftype = file.read(4)

		# find only RIFF AVI data
		if filetype == b'RIFF':
			data = file.read(int.from_bytes(filelen, "little"))

			# write data to new file
			new_file = p.Path("recovered_Data\\avifile"+str(runNo)+".avi")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(filetype)
				file.write(filelen)
				file.write(rifftype)
				file.write(data)
				
								
# recover FLAC files
# using function to get all FLAC header
idx_list = f.getIdx(hdData, b'fLaC')
runNo = 1

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element)
		filetype = file.read(4)
		metablockinfo = file.read(1)
		metablocklen = file.read(3)

		data = file.read(int.from_bytes(metablocklen, "little"))

		# write data to new file
		new_file = p.Path("recovered_Data\\flacfile"+str(runNo)+".flac")
		runNo += 1

		with new_file.open('wb') as file:
			file.write(filetype)
			file.write(metablockinfo)
			file.write(metablocklen)
			file.write(data)			


# recover JPG files
# using function to get all FLAC header
idx_list = f.getIdx(hdData, b'JFIF') 
runNo = 1

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-6)
		startMarker = file.read(4)
		
		if startMarker == b'\xff\xd8\xff\xe0':
			eofIdx = f.getJpgEof(hd, element-4)
			file.seek(element-6)
			data = file.read(eofIdx-(element-6))
			
			new_file = p.Path("recovered_Data\jpgfile"+str(runNo)+".jpg")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(data)