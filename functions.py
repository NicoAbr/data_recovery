# find more than one index (from: https://stackoverflow.com/questions/...
# 			6294179/how-to-find-all-occurrences-of-an-element-in-a-list)
def getIdx(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)
		
	
	
# Informationen dazu unter: https://stackoverflow.com/questions/4585527/detect-eof-for-jpg-images?answertab=votes#
# Funktion zum suchen der EOF Indizes. 
# funktioniert nur leider noch nicht ganz (Die Ausgespuckten Werte ergeben keinen Sinn)
# Übergeben wird die Datei und der Indize vom JPG Header
def getJpgEof(dataPath, currentIdx):

	with dataPath.open('rb') as file:
	
		file.seek(currentIdx)
		marker1 = file.read(1)
		marker2 = file.read(1)
#		print(marker1)
#		print(marker2)
		currentIdx += 2
				
		if (marker1 == b'\xff' and marker2 == b'\xd9'):
			return currentIdx
			
		elif (marker1 == b'\xff' and marker2 != b'\xda'):
			segmentLen = int.from_bytes(file.read(2), "big")
#			print(currentIdx)
#			print(segmentLen)
			currentIdx += segmentLen
#			print(currentIdx)
			currentIdx = getJpgEof(dataPath, currentIdx)
#			print(currentIdx)
#			print("Ich bin hier")
			
		elif (marker1 == b'\xff' and marker2 == b'\xda'):
#			print(currentIdx)
			file.seek(currentIdx)	
			marker1 = 0
			marker2 = 0
		
			while marker1 != b'\xff' or marker2 == (b'\x00' or b'\x01' or b'\xd0' or b'\xd1' or 
													b'\xd2' or b'\xd3' or b'\xd4' or b'\xd5' or 
													b'\xd6' or b'\xd7' or b'\xd8'):
				marker1 = file.read(1)
				marker2 = file.read(1)
				currentIdx += 1	
				file.seek(currentIdx)
#			currentIdx = getJpgSos(dataPath, currentIdx)
			marker1 = file.read(1)
			marker2 = file.read(1)
#			print(marker1)
#			print(marker2)
#			print("Ich bin hoffentlich fertig")
#			print(currentIdx)
			segmentLen = int.from_bytes(file.read(2), "big")
			currentIdx += segmentLen
#			print(currentIdx)
			currentIdx = getJpgEof(dataPath, currentIdx)
#		print(currentIdx)
#		print("error")
#		print(" ")
		
		return currentIdx	

def getJpgSos(dataPath, currentIdx):
	with dataPath.open('rb') as file:
	
		file.seek(currentIdx)	
		marker1 = 0
		marker2 = 0
		
		while marker1 != b'\xff' or marker2 == (b'\x00' or b'\x01' or b'\xd0' or b'\xd1' or 
												b'\xd2' or b'\xd3' or b'\xd4' or b'\xd5' or 
												b'\xd6' or b'\xd7' or b'\xd8'):
			marker1 = file.read(1)
			marker2 = file.read(1)
			currentIdx += 1	
			file.seek(currentIdx)
			
#		marker2 = file.read(1)
#		currentIdx += 1
#		if marker2 == 
#			print(currentIdx)
			currentIdx = getJpgSos(dataPath, currentIdx)
#		print("Hier bin ich")
#		print(marker1)
#		print(marker2)		
		return currentIdx
	
	
	
	
	
#	marker = 0
#	# sucht ab dem übergebenen JPG Header bis er auf 0xff (255) stößt
#	while marker != 0xff:
#		marker = lst[currentIdx+1]
#		currentIdx += 1
#		
#	# wenn er nach dem 0xff auf 0xd9 stößt ist der EOF gefunden
#	if lst[currentIdx+1] == 0xd9:
#		currentIdx += 1
#		return currentIdx
#	# wenn nach dem 0xff keiner der Marker 0xd0 bis 0xd9 auftaucht
#	# sind die nächsten beiden Bytes die Längenangabe für den Block
#	# Um diese Länge wird dann nach forne geskipt und die funktion mit der
#	# aktualisierten Indizierung neu aufgerufen (rekursiv)
#	elif lst[currentIdx+1] != (0x00 or 0x01 or 0xd0 or 0xd1 or 
#							   0xd2 or 0xd3 or 0xd4 or 0xd5 or 
#							   0xd6 or 0xd7 or 0xd8):
#		currentIdx += 1
#		x = lst[currentIdx+1]
#		y = lst[currentIdx+2]
#		blockLength =  y*256 + x
#		currentIdx += blockLength
#		currentIdx = getJpgEof(lst, currentIdx)
#		return currentIdx
#	# wenn der Marker 0xd0 bis 0xd9 oder 0x00 ist, dann sucht er nach dem nächsten 
#	# 0xff indem die funktion mit den aktualisierten marker aufgerufen wird.
#	else:
#		currentIdx = getJpgEof(lst, currentIdx)
#		return currentIdx