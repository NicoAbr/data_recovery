import pathlib
wav = pathlib.Path('test.wav')

with wav.open('rb') as file:
    filetype = file.read(4)
    filelen = file.read(4)
    rifftype = file.read(4)
    
print('filetype:', filetype)
print('filelen:', filelen)
print('rifftype:', rifftype)