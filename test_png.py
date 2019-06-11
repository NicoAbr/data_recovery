import pathlib
import functions as f

data = pathlib.Path('data_deleted.img')

with data.open('rb') as file:
	fileData = file.read()

# finding header of png files
pngIdx = f.getIdx(fileData, b'PNG')

# implementing variables for later use
workingIdx = []
chunkLen = []
chunkType = []

# finding indices of PNG files     
for element in pngIdx:
    with data.open('rb') as file:
        file.seek(element+7)
        filelen = int.from_bytes(file.read(4), "big")
        
        # sorting out indices that don't meet header expectations
        if filelen == 13:
            workingIdx.append(element)
            chunkLen.append(filelen)

# going to the start of each working png file
for element in range(len(workingIdx)):
    with data.open('rb') as file:
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
        new_file = pathlib.Path("pngfile"+str(element+1)+".png")
        with new_file.open('wb') as file:
                file.write(recoveredBytes)

