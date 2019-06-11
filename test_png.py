import pathlib
import functions as f

data = pathlib.Path('data_deleted.img')

with data.open('rb') as file:
	fileData = file.read()


pngIdx = f.getIdx(fileData, b'PNG')

workingIdx = []
chunkLen = []
chunkType = []
    
for element in pngIdx:
    with data.open('rb') as file:
        file.seek(element+7)
        filelen = int.from_bytes(file.read(4), "big")
        
        if filelen == 13:
            workingIdx.append(element)
            chunkLen.append(filelen)

for element in range(len(workingIdx)):
    with data.open('rb') as file:
        file.seek(workingIdx[element]+7)
        firstChunk = file.read(chunkLen[element]+12)    
        endIdx = (workingIdx[element]+7)+(chunkLen[element]+12)

        while chunkType != b'IEND':
            nextChunkLen = int.from_bytes(file.read(4), "big")
            chunkType = file.read(4)
            file.read(nextChunkLen+4)
            endIdx += nextChunkLen+12
        
        chunkType = []
        file.seek(workingIdx[element]-1)
        dataLen = endIdx-workingIdx[element]-1
        recoveredBytes = file.read(dataLen)

        # write data to new file
        new_file = pathlib.Path("pngfile"+str(element+1)+".png")

        with new_file.open('wb') as file:
                file.write(recoveredBytes)

