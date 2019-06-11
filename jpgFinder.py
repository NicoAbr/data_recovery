# Find JPG
import pathlib
import functions as f
import numpy as np


runNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()



# Damit könnte man den kompletten Header finden, dauert aber ziemlich lange	
#headerIdx = []
#for idx in range(len(hdData)):
#	if (hdData[idx] == 0xff and 
#		hdData[idx+1] == 0xd8 and
#		hdData[idx+2] == 0xff and
#		hdData[idx+3] == 0xe0 and
#		hdData[idx+4] == 0x00 and
#		hdData[idx+5] == 0x10 and
#		hdData[idx+6] == 0x4a and
#		hdData[idx+7] == 0x46 and
#		hdData[idx+8] == 0x49 and
#		hdData[idx+9] == 0x46 and
#		hdData[idx+10] == 0x00):
#		headerIdx.append(idx)
#		
#print(headerIdx)



# using function to get all JPG header
idx_list = f.getIdx(hdData, b'JFIF') 
print(len(idx_list))

for element in idx_list:
	with hd.open('rb') as file:
		file.seek(element-6)
		startMarker = file.read(4)
		
		if startMarker == b'\xff\xd8\xff\xe0':
			eofIdx = f.getJpgEof(hd, element-4)
			print(eofIdx)
			file.seek(element-6)
			data = file.read(eofIdx-(element-6))
			
			new_file = pathlib.Path("jpgfile"+str(runNo)+".jpg")
			runNo += 1

			with new_file.open('wb') as file:
				file.write(data)
			

			



# alle Indizes werden in die Funktion gegeben und der entsprechnende
# EOF Indize kommt zurück (EOF steht für "end of file")
#for element in idx_list:
#	element -= 6;
#	
#	print(element)
#	print(f.getJpgEof(hdData, element))
#	print(" ")

