# data_recovery
zweite Abgabe Angewandtes Programmieren
Infos zu png von https://www.w3.org/TR/PNG-Structure.html


'data_recovery.py' is an function, which can find and recreate different deleted data types from an hard drive image which is 
given as a path in a parameter. The function searches for specific byte constructs and writes the data related parts in new 
files. The files are saved in the created directory 'revovered_data'.
Datatypes which can be recovered, are: *.AVI, *.JPG, *.WAV, *.PNG, *.FLAC

## Data types

The informations for *.AVI data are found [here](https://en.wikipedia.org/wiki/Resource_Interchange_File_Format)
*.AVI data is an specific Resource Interchange File Format (RIFF). Thats why every *.AVI file starts with a
four byte sized "RIFF" information followed by a four byte length information which is the length of the whole data counted
from current position. After this, four byte of rifftype follows, which is "AVI " in this case. With this information the data 
can rewrited from the beginning byte till "filelen + 8" (for RIFF header). 

The informations for *.WAV data get from the programming lecture "Angewandtes Programmieren" of Jade Hochschule Oldenburg. 
*.WAV data is an specific Resource Interchange File Format (RIFF) as well. Thats why the implementation of *.WAV recovery is similar
to the *.AVI recovery.

The informations for *.JPG data get from [here](https://stackoverflow.com/questions/4585527/detect-eof-for-jpg-images?answertab=votes#)
All *.JPG files begin with two specific bytes (ff d8) followed by different data blocks. Evereyone of these blocks begins with
an "ff" byte, followed by a random byte. The two bytes after this are a Big-Endian bytelength information of the current data block.
A *.JPG file always ends with the two specific bytes "ff" and "d9". After this end piont is found the whole data in between the start
(ff d8) and the end (ff d9) can be write into a file with the *.JPG ending.

The informations for *.FLAC data get from [here](https://xiph.org/flac/documentation_format_overview.html)
...


-The information for *.PNG data is mainly taken from [here](https://www.w3.org/TR/PNG-Structure.html)
 PNG Data is an compressed image format that consists 
 of a header of 8 bytes which is followed by many 
 chunks with variables sizes. The header always starts 
 with an 68 hex value and the letters PNG as ASCII 
 code. Each chunk starts with 4 bytes that describe the 
 length of that chunk minus 12 bytes. After the number 
 of bytes the chunktype ist written in ASCII code. With 
 these two informations the programm can jump from 
 chunk to chunk until the last chunk of the file is 
 found. The last chunk is always from type 'IEND'. 


## Install:
'data_recovery' is written and tested on python 3.7. To use the function for your own lost data you need the files:
- data_recovery.py
- functions.py

If you want to just test 'data_recovery' you will need:
- data_recovery_test.py
- data_deleted.img 
additionaly.


## License:
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
		