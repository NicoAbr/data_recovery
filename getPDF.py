import pathlib
import functions as f
runNo = 1
hd = pathlib.Path('data_deleted.img')

with hd.open('rb') as file:
	hdData = file.read()

idxBeginn = f.getIdx(hdData, b'%PDF')
print(idxBeginn)

idxXref = f.getIdx(hdData, b'xref')
print(idxXref)

idxStartxref = f.getIdx(hdData, b'startxref')
print(idxStartxref)

idxEnd = f.getIdx(hdData, b'%%EOF')
print(idxEnd)

for x in idxBeginn:
	with hd.open('rb') as file:
		file.seek(x)
		beginn = file.read(10)
		print(beginn)
