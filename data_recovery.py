import pathlib as p
import functions as f
import os


def data_recovery(deleted_data):
	hd = p.Path(deleted_data)

	path = p.Path('recovered_data')
	if os.path.isdir(path) == False:
		os.mkdir('recovered_data')

	with hd.open('rb') as file:
		hdData = file.read()

	# recover WAVE files
	# finding header of wave files
	waveIdx = f.getIdx(hdData, b'WAVE')

	for counter, element in enumerate(waveIdx):
		with hd.open('rb') as file:
			file.seek(element-8)
			filetype = file.read(4)
			filelen = file.read(4)
			rifftype = file.read(4)

			if filetype == b'RIFF':
				data = file.read(int.from_bytes(filelen, "little")-4)

				# creating and writing new file
				new_file = p.Path("recovered_data\wavfile"+str(counter+1)+".wav")
				with new_file.open('wb') as file:
					file.write(filetype)
					file.write(filelen)
					file.write(rifftype)
					file.write(data)

					
	# recover AVI files			
	# finding header of avi files
	aviIdx = f.getIdx(hdData, b'AVI ')

	for counter, element in enumerate(aviIdx):
		with hd.open('rb') as file:
			file.seek(element-8)
			filetype = file.read(4)
			filelen = file.read(4)
			rifftype = file.read(4)

			# find only RIFF AVI data
			if filetype == b'RIFF':
				data = file.read(int.from_bytes(filelen, "little")-4)

				# creating and writing new file
				new_file = p.Path("recovered_data\\avifile"+str(counter+1)+".avi")
				with new_file.open('wb') as file:
					file.write(filetype)
					file.write(filelen)
					file.write(rifftype)
					file.write(data)
					
									
	# recover FLAC files
	# finding header of flac files
	flacIdx = f.getIdx(hdData, b'fLaC')

	for counter, element in enumerate(flacIdx):
		with hd.open('rb') as file:
			file.seek(element)
			filetype = file.read(4)
			metablockinfo = file.read(1)
			metablocklen = file.read(3)

			data = file.read(int.from_bytes(metablocklen, "little"))

			# creating and writing new file
			new_file = p.Path("recovered_data\\flacfile"+str(counter+1)+".flac")
			with new_file.open('wb') as file:
				file.write(filetype)
				file.write(metablockinfo)
				file.write(metablocklen)
				file.write(data)			


	# recover JPG files
	# finding header of jpg files
	jpgIdx = f.getIdx(hdData, b'JFIF') 

	# sorting out indices that don't meet header expectations  
	for counter, element in enumerate(jpgIdx):
		with hd.open('rb') as file:
			file.seek(element-6)
			startMarker = file.read(4)
			
			if startMarker == b'\xff\xd8\xff\xe0':
				# find end of file indice
				eofIdx = f.getJpgEof(hd, element-4)
				# reading in all needed binary data
				file.seek(element-6)
				data = file.read(eofIdx-(element-6))
				
				# creating and writing new file
				new_file = p.Path("recovered_data\jpgfile"+str(counter+1)+".jpg")
				with new_file.open('wb') as file:
					file.write(data)
					
					
	# recover PNG files				
	# finding header of png files
	pngIdx = f.getIdx(hdData, b'PNG')

	# implementing variables for later use
	workingIdx = []
	chunkLen = []
	chunkType = []

	# sorting out indices that don't meet header expectations    
	for element in pngIdx:
		with hd.open('rb') as file:
			file.seek(element+7)
			filelen = int.from_bytes(file.read(4), "big")
			
			if filelen == 13:
				workingIdx.append(element)
				chunkLen.append(filelen)

	# going to the start of each working png header
	for element in range(len(workingIdx)):
		with hd.open('rb') as file:
			file.seek(workingIdx[element]+7)
			firstChunk = file.read(chunkLen[element]+12)
			
			# counting end index for later reading of the needed image part    
			endIdx = (workingIdx[element]+7)+(chunkLen[element]+12)

			# going from chunk to chunk till the end of the file
			while chunkType != b'IEND':
				nextChunkLen = int.from_bytes(file.read(4), "big")
				chunkType = file.read(4)
				file.read(nextChunkLen+4)
				# keeping end index counter up
				endIdx += nextChunkLen+12
			
			# reading in all needed binary data 
			chunkType = []
			file.seek(workingIdx[element]-1)
			dataLen = endIdx-workingIdx[element]-1
			recoveredBytes = file.read(dataLen)

			# creating and writing new file
			new_file = p.Path("recovered_data\pngfile"+str(element+1)+".png")
			with new_file.open('wb') as file:
					file.write(recoveredBytes)