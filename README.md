# data_recovery
zweite Abgabe Angewandtes Programmieren


Infos zu flac von https://xiph.org/flac/

Infos zu mp3 von http://mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
		https://www.codeproject.com/Articles/8295/MPEG-Audio-Frame-Header

Infos zu png von https://www.w3.org/TR/PNG-Structure.html

Infos zu jpg von https://stackoverflow.com/questions/4585527/detect-eof-for-jpg-images?answertab=votes#


data_recovery.py is an function, which can find different deleted data types from an hard drive image.
The function searches for specific byte constructs and writes the data related parts in new files.
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

-The information for *.PNG data is mainly taken from https://www.w3.org/TR/PNG-Structure.html
 PNG Data is an compressed image format that consists of a header of 8 bytes which is followed by many chunks with variables sizes.
 The header always starts with an 68 hex value and the letters PNG as ASCII code. Each chunk starts with 4 bytes that describe the length
 of that chunk minus 12 bytes. After the number of bytes the chunktype ist written in ASCII code. With these two informations 
 the programm can jump from chunk to chunk until the last chunk of the file is found. The last chunk is always from type 'IEND'. 


		

License:
Copyright 2019 Tilljan Jansohn, tilljan.jansohn@student.jade-hs.de
               Robert Schirm, robert.schirm@student.jade-hs.de
               Nico Abraham, nico.abraham@student.jade-hs.de 

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright 
notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  		