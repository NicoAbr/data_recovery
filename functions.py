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
def getJpgEof(lst, currentIdx):
	marker = 0
	# sucht ab dem übergebenen JPG Header bis er auf 0xff (255) stößt
	while marker != 0xff:
		marker = lst[currentIdx+1]
		currentIdx += 1
		
	# wenn er nach dem 0xff auf 0xd9 stößt ist der EOF gefunden
	if lst[currentIdx+1] == 0xd9:
		currentIdx += 1
		return currentIdx
	# wenn nach dem 0xff keiner der Marker 0xd0 bis 0xd9 auftaucht
	# sind die nächsten beiden Bytes die Längenangabe für den Block
	# Um diese Länge wird dann nach forne geskipt und die funktion mit der
	# aktualisierten Indizierung neu aufgerufen (rekursiv)
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
	# wenn der Marker 0xd0 bis 0xd9 oder 0x00 ist, dann sucht er nach dem nächsten 
	# 0xff indem die funktion mit den aktualisierten marker aufgerufen wird.
	else:
		currentIdx = getJpgEof(lst, currentIdx)
		return currentIdx