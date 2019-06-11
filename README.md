# data_recovery
zweite Abgabe Angewandtes Programmieren


Infos zu flac von https://xiph.org/flac/

Infos zu mp3 von http://mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
		https://www.codeproject.com/Articles/8295/MPEG-Audio-Frame-Header

Infos zu png von https://www.w3.org/TR/PNG-Structure.html

Infos zu jpg von https://stackoverflow.com/questions/4585527/detect-eof-for-jpg-images?answertab=votes#


data_recovery.py is an function, which can find different deleted data types from an hard drive image.
The function searches for specific byte constructs and write the data related parts in new files.
Datatypes which can be recovered, are: *.AVI, *.JPG, *.WAV, *.PNG, *.FLAC

The informations for *.AVI data are found in https://en.wikipedia.org/wiki/Resource_Interchange_File_Format
*.AVI data is an specific Resource Interchange File Format(RIFF). Thats why every *.AVI file starts with a
four byte sized "RIFF" information followed by a four byte length information which is the length of the whole data counted
from current position. 

The informations for *.JPG data get from https://stackoverflow.com/questions/4585527/detect-eof-for-jpg-images?answertab=votes#
All *.JPG files begin with two specific bytes (ff d8) followed by different data blocks. Evereyone of these blocks begins with
an "ff" byte, followed by a random byte. The two bytes after this are a Big-Endian bytelength information of the current data block.
A *.JPG file always ends with the two specific bytes "ff" and "d9". After this end piont is found the whole data in between the start
(ff d8) and the end (ff d9) can be write into a file with the *.JPG ending.


		
		