i = 0
nm = []
nim = []
tgs = []
uts = []
uas = []
akhir = []

stop = False
no=0
while (not stop):
    nama = raw_input              ("Nama             :")
    nm.append(nama)
    nim_mahasiswa = input         ("NIM              :")
    nim.append(nama)
    tugas = input                 ("Tugas            :")
    tgs.append(tugas)
    Uts = input                   ("Uts              :")
    uts.append(Uts)
    Uas = input                   ("Uas              :")
    uas.append(Uas)
    data = raw_input              ("Tambah data [Y/T]:")
    if (data == 'T'):
        stop = True
    akhir = (tugas+Uts+Uas)
    no +=1
print "=========================================================================="
print" NO     |      NAMA     |  NIM    |   TUGAS   |    UTS     |  UAS   | AKHIR"
print"==========================================================================="
for n in range (i) :
	print" ",n +1,"| ",nama,"   |",nim,"  | ",tugas," | ",Uts,"    | ",Uas,"| ",akhir,"|"
