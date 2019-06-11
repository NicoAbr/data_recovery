# Find JPG
import pathlib
import functions as f

runNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

# using function to get all JPG header
idx_list = f.getIdx(hdData, b'JFIF') 

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-6)
		startMarker = file.read(4)
		
		if startMarker == b'\xff\xd8\xff\xe0':
			eofIdx = f.getJpgEof(hd, element-4)
			file.seek(element-6)
			data = file.read(eofIdx-(element-6))
			
			new_file = pathlib.Path("jpgfile"+str(runNo)+".jpg")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(data)
