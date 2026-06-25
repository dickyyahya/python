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


