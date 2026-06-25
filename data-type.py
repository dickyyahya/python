#salah satu ciri data int tanpa ("")
# tipe data angka satuan tanpa koma (integer)
data_integer = 3
print("data =", data_integer)
print("-bertipe :",type(data_integer))

#tipe data angka dengan koma (float)
data_float = 2.4
print ("data =", data_float)
print ("-bertipe =", type(data_float))

#tipe data kumpulan karakter (string)
data_string = "budi"
print ("data =", data_string)
print ("-bertipe =",type(data_string))

#tipe data biner true/false (boolean)
data_bool = True
print ("data =", data_bool)
print ("-bertipe =", type(data_bool))

#tipe data khusus

#bilangan komplek
data_complex = complex(5,8)
print ("data =", data_complex)
print ("-bertipe =" , type(data_complex))


#tipe data dari bahasa c
from ctypes import c_double, c_char

data_c_double = c_double(40.8)
print("data :", data_c_double)
print("-bertipe", type(data_c_double))

############################
#latihan
# Soal 1 - Tipe Data Dasar

# Buat program yang:

# Membuat variabel nama berisi nama kamu (string).
nama = 'Budi'
# Membuat variabel umur berisi umur kamu (integer).
umur = 20
# Membuat variabel tinggi berisi tinggi badan kamu dalam meter (float).
tinggiBadan = 160.5
# Membuat variabel mahasiswa bernilai True atau False (boolean).
statusSiswa = True
# Lalu tampilkan:

# Nilai masing-masing variabel.
print ("Nama =",nama, "Umur =", umur, "Tinggi Badan =", tinggiBadan, "Status Siswa", statusSiswa)
# Tipe data masing-masing variabel menggunakan type().
print("Tipe Data Nama", type(nama),"Tipe Data Umur",type(umur), "Tipe Data Tinggi Badan", type(tinggiBadan), "Status Siswa", type(statusSiswa))

a = 10
b = 3.14
c = "Python"
d = False
e = complex(2,5)

print('a =',a)
print('type data a =', type(a))
print('b =',b)
print('type data b =', type(b))
print('c =',c)
print('type data c =', type(c))
print('d =',d)
print('type data d =',type(d))
print('e =',e)
print('type data e =', type(e))


#konversi data

angka = -1

# angka_float = float(angka)
# angka_string = str(angka)
angka_bool = bool(angka)
# print("angka float", angka_float)
# print("tipe data angka float",type(angka_float))
# print("angka string", angka_string)
# print("tipe data angka string",type(angka_string))
print("angka bool", angka_bool)
print("tipe data angka bool", type(angka_bool))

nama = "andi"
umur = 18
tinggi = 1.72

# str_umur = str(umur)
str_tinggi = str(tinggi)

print("Nama Saya "+nama)
print("umur saya "+ str(umur) + " tahun")
print ("tinggi saya "+ str_tinggi + " meter")

print (f"nama saya {nama} umur saya {umur} tinggi saya {tinggi}")

a=8
b=9
print(f"hasil ({a*b})hutan")