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
def getJpgEof(dataPath, currentIdx):
	with dataPath.open('rb') as file:
		file.seek(currentIdx)
		marker1 = file.read(1)
		marker2 = file.read(1)
		currentIdx += 2
				
		if (marker1 == b'\xff' and marker2 == b'\xd9'):
			return currentIdx
			
		elif (marker1 == b'\xff' and marker2 != b'\xda'):
			segmentLen = int.from_bytes(file.read(2), "big")
			currentIdx += segmentLen
			currentIdx = getJpgEof(dataPath, currentIdx)
			return currentIdx
			
		elif (marker1 == b'\xff' and marker2 == b'\xda'):
			marker1 = 0
			marker2 = 0
		
			while marker1 != b'\xff' or marker2 == (b'\x00' or b'\x01' or b'\xd0' or b'\xd1' or 
													b'\xd2' or b'\xd3' or b'\xd4' or b'\xd5' or 
													b'\xd6' or b'\xd7' or b'\xd8'):
				marker1 = file.read(1)
				marker2 = file.read(1)
				currentIdx += 1	
				file.seek(currentIdx)
			marker1 = file.read(1)
			marker2 = file.read(1)
			segmentLen = int.from_bytes(file.read(2), "big")
			currentIdx += segmentLen
			currentIdx = getJpgEof(dataPath, currentIdx)	
		
		while marker1 != b'\xff' or marker2 != b'\xd9':
			marker1 = file.read(1)
			marker2 = file.read(1)
			currentIdx += 1	
			file.seek(currentIdx)
	
		return currentIdx
