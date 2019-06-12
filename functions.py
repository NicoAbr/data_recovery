""" Copyright (c) 2019, Tilljan Jansohn, tilljan.jansohn@student.jade-hs.de
						Robert Schirm, robert.schirm@student.jade-hs.de
						Nico Abraham, nico.abraham@student.jade-hs.de
	This code is published under the terms of the BSD license. """
	
def getIdx(lst, element):
	""" function to find more than one index with an wanted value in binary 
		data. Main code is taken from https://stackoverflow.com/questions/...
 			6294179/how-to-find-all-occurrences-of-an-element-in-a-list
		Input: 
			lst: List of binary data
			element: value to look for in binary data

		Output:
			List of indices of first bytes with wanted value
	"""
	result = []
	offset = -1
	while True:
		try:
			offset = lst.index(element, offset+1)
		except ValueError:
			return result
		result.append(offset)
		

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
	
		return currentIdx+1