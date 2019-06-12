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
			# getting index of element with wanted value
			offset = lst.index(element, offset+1)
		# ending function at end of data
		except ValueError:
			return result
		# append each index to list
		result.append(offset)
		

def getJpgEof(dataPath, currentIdx):
	# going to the start of the header 
	# and read in markers
	with dataPath.open('rb') as file:
		file.seek(currentIdx)
		marker1 = file.read(1)
		marker2 = file.read(1)
		currentIdx += 2
		
		# check for end of file markers
		if (marker1 == b'\xff' and marker2 == b'\xd9'):
			return currentIdx
		
		# preclude SOS markers
		elif (marker1 == b'\xff' and marker2 != b'\xda'):
			# read in block length
			segmentLen = int.from_bytes(file.read(2), "big")
			currentIdx += segmentLen
			# recall getJpgEof function
			currentIdx = getJpgEof(dataPath, currentIdx)
			return currentIdx
		
		# check for SOS markers
		elif (marker1 == b'\xff' and marker2 == b'\xda'):
			marker1 = 0
			marker2 = 0
			
			# skip forward to the next block header
			while marker1 != b'\xff' or marker2 == (b'\x00' or b'\x01' or b'\xd0' or b'\xd1' or 
													b'\xd2' or b'\xd3' or b'\xd4' or b'\xd5' or 
													b'\xd6' or b'\xd7' or b'\xd8'):
				marker1 = file.read(1)
				marker2 = file.read(1)
				currentIdx += 1	
				file.seek(currentIdx)
			# read in block header markers
			marker1 = file.read(1)
			marker2 = file.read(1)
			# read in block length
			segmentLen = int.from_bytes(file.read(2), "big")
			currentIdx += segmentLen
			# recall getJpgEof function
			currentIdx = getJpgEof(dataPath, currentIdx)	
		
		# skip forward to end of file markers
		while marker1 != b'\xff' or marker2 != b'\xd9':
			marker1 = file.read(1)
			marker2 = file.read(1)
			currentIdx += 1	
			file.seek(currentIdx)
		
		# return end of file index
		return currentIdx+1