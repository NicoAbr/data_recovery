import pathlib
import functions as f
runNo = 1
pic = pathlib.Path('programmieraufgabe(1).pdf')

with pic.open('rb') as file:
	picData = file.read()

#print(picData)
length = len(picData)

with pic.open('rb') as file:
	picBeg = file.read(16)
	print(picBeg)
	file.seek(length-16)
	picEnd = file.read(16)
	print(picEnd)

idxBeginn = f.getIdx(picData, b'%PDF')
idxEnd = f.getIdx(picData, b'\n%%EOF\n')


#data = picData[idx_list[0]:(idx_list[0]+2)]
print(picData)