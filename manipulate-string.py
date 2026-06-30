# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_awal = "budi"
nama_tengah = "anwar"
nama_akhir = "abe"

nama_full = nama_awal + " " + nama_tengah + " " + nama_akhir
print(nama_full)

# 2. menghitung panjang string
panjangNama = len(nama_full)
print("panjang dari "+ nama_full +"="+ str(panjangNama))

# 3.operator untuk string
# mengecek apakah ada komponen char atau string di string

a = "a"
status = a in nama_full
print(a + " ada di " + nama_full + "=" + str(status))

A = "A"
status = A in nama_full
print(A + " ada di " + nama_full + "=" + str(status))

a = "a"
status = a not in nama_full
print(a + " ada di " + nama_full + "=" + str(status))

# mengulang string
print("ha"*9)
print(9*"ha")

# indexing

print("index ke - 0 = " + nama_full[0]) #menghitungnya dari seperti array dari 0 
print("index ke - 9 = " + nama_full[9])
print("index ke - (-1) = " + nama_full[-1]) # menghitung dari belakang
# print("index ke - (15) = " + nama_full[15]) error
# range
print("index ke - [4:9] = " + nama_full[4:8]) #menghitungnya dari seperti array dari 4 tapi dikurangi 1
print("index ke -[0,2,4,6,8,10]:" +nama_full[0:11:2])

# item paling kecil
print ("paling kecil :" + min(nama_full))
# item paling besar
print("paling besar :" + max(nama_full))

ascii_code = ord (" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# operator dalam bentuk method
data = "kadal asli banten"
jumlah = data.count("a")
print("jumlah a pada " + data + "=" + str(jumlah))

# practice
nama_awal = "Siti"
nama_tengah = "Nur"
nama_akhir = "Aisyah"

# Gabungkan menjadi nama lengkap.
nama_full = nama_awal +  nama_tengah + nama_akhir
print("Nama full saya adalah :" + nama_full) 
# Hitung panjang nama.
panjang_Nama = len(nama_full)
print("Jumlah karakter di nama saya :" + str(panjang_Nama))
# Cek apakah huruf "i" ada pada nama.
i = "i"
status = i in nama_full
print("cek i apakah ada :" + str(status))
# Cek apakah huruf "Z" ada pada nama.
Z = "Z"
status = Z in nama_full
print("cek Z apakah ada :" + str(status))
# Cetak karakter pertama.
print(nama_full[0])
# Cetak karakter terakhir.
print(nama_full[-1])
# Cetak 5 karakter pertama.
print(nama_full[0:5])
# Cetak setiap karakter dengan langkah 2 (step = 2).
print(nama_full[::2])
# Tampilkan karakter terkecil dan terbesar.
print(max(nama_full))
print(min(nama_full))
# Hitung jumlah huruf "a" pada nama lengkap.
data = nama_full.count("a")
print("a disini ada " + str(data))