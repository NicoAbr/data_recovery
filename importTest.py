import pathlib
wav = pathlib.Path('data_deleted.img')

with wav.open('rb') as file:
   filetype = file.read(4) 
   filelen = file.read(4)
   #filelen = int.from_bytes(file.read(4), "little")
   rifftype = file.read(4)
    
print('filetype:', filetype)
print('filelen:', filelen)
print('rifftype:', rifftype)