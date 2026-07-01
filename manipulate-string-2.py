# # operator dalam bentuk method
# # merubah case dari string

# # merubah semua ke uppercase
# kataUpper = "cihuy"
# kataUpper = kataUpper.upper()
# print(kataUpper)

# # merubah ke lower case
# kataLower = "PrIkItIWWW"
# kataLower = kataLower.lower()
# print(kataLower) 

# # pengecekan dengan isX method
# # contoh untuk pengecekan lower case
# cekKata = "fufuffa"
# cekLower = cekKata.islower()
# print(cekLower)

# # contoh untuk pengecekan Upper case
# cekUpper =  cekKata.isupper()
# print(cekUpper)

# # contoh untuk pengecekan semuanya huruf
# cekAllHuruf = cekKata.isalpha()
# print(cekAllHuruf)

# # contoh untuk pengecekan huruf and angka
# cekHurufAngka = cekKata.isalnum()
# print (cekHurufAngka)
# # contoh untuk pengecekan angka saja
# cekOnlyAngka = cekKata.isdecimal()
# print(cekOnlyAngka)
# # contoh untuk pengecekan spasi, tab, newline in
# cekSpasi = cekKata.isspace()
# print(cekSpasi)
# # contoh untuk pengecekan kata diawali huruf besar
# cekAwalBesar = cekKata.istitle()
# print(cekAwalBesar)

# # ngecek komponen startswith() endwith()
# # startswith()
# cek_start = "Kopdes Mbg".startswith("Kopdes")
# print(cek_start)
# # endwith()
# cek_end = "Kopdes Mbg".endswith("Mbg")
# print(cek_end)

# # penggambungan komponen join() split()
# pisah = ['ayam','pitik','bebek']
# gabungKoma = ", ".join(pisah)
# gabungSpasi = " ".join(pisah)
# gabungSpasi = " ".join(pisah)
# gabungSpasi = " ".join(pisah)
# gabungan = "ehm ".join(pisah)

# print(pisah)
# print(gabungKoma)
# print(gabungSpasi)
# print(gabungan)

# pisahKata = "ayamjjpitikjjbebek"
# print(pisahKata.split('jj'))

# # alokasi karakter rjust(), ljust(), center()
# # rjust()
# kanan = "kanan".rjust(10,"=")
# print("'"+kanan+"'")
# # ljust()
# kiri = "kiri".ljust(10,"*")
# print("'"+kiri+"'")
# # center
# tengah = "tengah".center(10,"~")
# print("'"+tengah+"'")

# # kebalikaknya dengan menghapus
# tengah = tengah.strip("~") #menghilangkan tanda ~
# print(tengah)

# latihan
# Buat program sederhana yang:

# Meminta pengguna memasukkan sebuah kalimat.
inputUser = input("Masukan Kata :")
# Menampilkan:
print(inputUser)
# versi uppercase,
print(inputUser.upper())
# versi lowercase,
print(inputUser.lower())
# apakah semua huruf kecil,
cekHurufKecil = inputUser.islower()
print(cekHurufKecil)
# apakah semua huruf besar,
cekHurufBesar = inputUser.isupper()
print(cekHurufBesar)
# apakah hanya huruf,
cekJustWord = inputUser.isalpha()
print(cekJustWord)
# apakah huruf dan angka,
cekJustWordNumber = inputUser.isalnum()
print(cekJustWordNumber)
# apakah hanya angka,
cekJustNumber = inputUser.isnumeric()
print(cekJustNumber)
# apakah Title Case.
cekFirstUpper = inputUser.istitle()
print(cekFirstUpper)
# Tampilkan kalimat tersebut dalam format:
# rata kiri,
print(inputUser.ljust(10,"+"))
# rata kanan,
print(inputUser.rjust(10,"~"))
# rata tengah (panjang 40 karakter).
print(inputUser.center(40,"$"))
# Tambahkan karakter = pada hasil rata tengah, kemudian hapus kembali karakter tersebut menggunakan strip().
print(inputUser.strip("$"))

