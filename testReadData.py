import pathlib
import functions as f

data = pathlib.Path('data_deleted.img')

with data.open('rb') as file:
	fileData = file.read()
#print(fileData)

length = len(fileData)

with data.open('rb') as file:
	fileBeg = file.read(16)
	print("file beginn: ", fileBeg)
	file.seek(length-16)
	fileEnd = file.read(16)
	print("file end: ", fileEnd)