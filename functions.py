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
		
		

#def getJpgEof(lst, currentIdx):
#	marker = 0
#	while marker != 255:
#		currentIdx += 1
#		marker = lst[currentIdx]
#		print(lst[currentIdx])
#	
#	
#	if lst[currentIdx+1] == 0xd9:
#		currentIdx += 1
#		return currentIdx
#	elif lst[currentIdx+1] != (0x00 or 0x01 or 0xd0 or 0xd1 or 0xd2 or 0xd3 or 0xd4 or 0xd5 or 0xd6 or 0xd7 or 0xd8):
#		currentIdx += 1
#		blockLength = int.from_bytes(b'lst[currentIdx+1] lst[currentIdx+2]', "big")
#		currentIdx += blockLength
#		getJpgEof(lst, currentIdx)
#	else:
#		getJpgEof(lst, currentIdx)
	
	
	
# Informationen dazu unter: https://stackoverflow.com/questions/4585527/detect-eof-for-jpg-images?answertab=votes#
# funktioniert nur leider noch nicht ganz (Die Ausgespuckten Werte ergeben keinen Sinn)
def getJpgEof(lst, currentIdx):
	marker = 0
	while marker != 0xff:
		marker = lst[currentIdx+1]
		currentIdx += 1
		
		
	if lst[currentIdx+1] == 0xd9:
		currentIdx += 1
		return currentIdx
	elif lst[currentIdx+1] != (0x00 or 0xd0 or 0xd1 or 
							   0xd2 or 0xd3 or 0xd4 or 0xd5 or 
							   0xd6 or 0xd7 or 0xd8 or 0xd9):
		currentIdx += 1
		x = lst[currentIdx+1]
		y = lst[currentIdx+2]
		blockLength =  y*256 + x
		currentIdx += blockLength
		currentIdx = getJpgEof(lst, currentIdx)
		return currentIdx
	else:
		currentIdx = getJpgEof(lst, currentIdx)
		return currentIdx