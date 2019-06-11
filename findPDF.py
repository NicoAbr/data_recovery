import pathlib
import functions as f
runNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

idxBeginn = f.getIdx(hdData, b'%PDF')
print(idxBeginn)
idxXref = f.getIdx(hdData, b'xref')
print(idxXref)
idxStartxref = f.getIdx(hdData, b'startxref')
print(idxStartxref)
idxEnd = f.getIdx(hdData, b'%%EOF')
print(idxEnd)


#with hd.open('rb') as file:
#	for elementNo in range(len(idxEnd)):
#		idxLen = (idxEnd[elementNo] - startxref[elementNo])
#		file.seek(idxEnd[elementNo]-skip)
#		fileLength = int.from_bytes(file.read(skip), "little")
#		file.seek(idxBeginn[elementNo]+fileLength)
#		test = file.read(8)
#		print(test)

for elementNo in range(len(idxBeginn)):
	idxLen = (idxEnd[elementNo] - startxref[elementNo]-9) # Länge der länge
	print(idxLen)
	with hd.open('rb') as file:
		file.seek(idxEnd[elementNo]-idxLen)
		lenghtByte = file.read(idxLen)
		print(lenghtByte)
		fileLength = int.from_bytes(lenghtByte, "little")
		print(fileLength)
		file.seek(idxBeginn[elementNo]+fileLength)
		test = file.read(8)
		print(test)
		#fileData = file.read(length)

	#new_file = pathlib.Path("pdffile"+str(runNo)+".pdf")
	#runNo += 1

	#with new_file.open('wb') as file:
	#	file.write(fileData)
