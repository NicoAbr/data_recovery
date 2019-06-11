import pathlib
import functions as f
nbytes = 16	# Wie viele Bytes sollen angezeigt werden?
data = pathlib.Path('data_deleted.img')

with data.open('rb') as file:
	fileData = file.read()
#print(fileData)	# Printet die gesamte Datei!!!!!!

length = len(fileData)

with data.open('rb') as file:
	fileBeg = file.read(nbytes)
	print("file beginn: ", fileBeg)
	file.seek(length-nbytes)
	fileEnd = file.read(nbytes)
	print("file end: ", fileEnd)