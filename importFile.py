import pathlib
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

idx = hdData.index(b'WAVE')

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
