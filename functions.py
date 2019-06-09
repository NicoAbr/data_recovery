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
		
		

def getJpgEof(lst, startIdx, idxCounter):
marker = []
	file.seek(idx_list[1])
	while marker != 0xff:
		marker = file.read(1)
		idxCounter += 1
	if file.read(1) != (0x00 or 0x01 or 0xd0 or 0xd1 or 0xd2 or 0xd3 or 0xd4 or 0xd5 or 0xd6 or 0xd7 or 0xd8):
		blockLength = int.from_bytes(file.read(2), "big")
		idxCounter += 2
	else:
		marker = []
		while marker != 0xff:
			marker = file.read(1)
			idxCounter += 1
	file.read(blockLength-2)
	idxCounter += blockLength-2