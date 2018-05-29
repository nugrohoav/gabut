#PROGRAM UNTUK MENGGABUNG BEBERAPA DOKUMEN PDF
#29 Mei 2018
##############################################################################
import os
from PyPDF2 import PdfFileMerger
lok=''#lokasi penyimpanan pdf
x = [a for a in os.listdir(lok) if a.endswith(".pdf")]#ekstensi CASE SENSITIF
print(x)
merger = PdfFileMerger()

for i in x:
    i=lok+i
    merger.append(open(i, 'rb'))
nama=str(input('Simpan file sebagai:(tulis tanpa ekstensi)'))
with open(lok+nama, "wb") as fout:
    merger.write(fout)