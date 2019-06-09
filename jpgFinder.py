# Find JPG
import pathlib
import functions as f
import numpy as np

#import binascii
#binary_string0 = binascii.unhexlify("ff")
#binary_string1 = binascii.unhexlify("d8")
#binary_string2 = binascii.unhexlify("ff")
#binary_string3 = binascii.unhexlify("e0")
#binary_string4 = binascii.unhexlify("00")
#binary_string5 = binascii.unhexlify("10")
#binary_string6 = binascii.unhexlify("4a")
#binary_string7 = binascii.unhexlify("46")
#binary_string8 = binascii.unhexlify("49")
#binary_string8 = binascii.unhexlify("46")
#binary_string8 = binascii.unhexlify("00")

#binary_string = binary_string0+binary_string1+binary_string2+binary_string3+binary_string4+binary_string5+binary_string6+binary_string7+binary_string8
unNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()


	
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

# using function to get all WAVE header
idx_list = f.getIdx(hdData, b'JFIF')  
for element in idx_list:
	element -= 4;
	
	print(element)
	print(f.getJpgEof(hdData, element))
	print(" ")

