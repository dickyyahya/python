# operasi logika atau boolean
# not, or, and, xor

# not (kebalikan)
print("======NOT========")
a = True
b = False
c = not a
d = not b
print ("Hasil dari NOT a :",c)
print ("Hasil dari NOT b :",d)


# or (jika salah satu nilai true maka bernilai true seperti penjumlahan)
print("=======OR========")
a = True
b = True
c = a or b
print(a,"OR",b, "=",c)
a = True
b = False
c = a or b
print(a,"OR",b, "=",c)
b = False
a = True
c = a or b
print(a,"OR",b, "=",c)
a = False
b = False
c = a or b
print(a,"OR",b, "=",c)

# and (jika dua bauh nilai true maka bernilai true seperti perkalian)
print("=======AND========")
a = True
b = True
c = a and b
print(a,"AND",b, "=",c)
a = True
b = False
c = a and b
print(a,"AND",b, "=",c)
b = False
a = True
c = a and b
print(a,"AND",b, "=",c)
a = False
b = False
c = a and b
print(a,"AND",b, "=",c)

# xor (akan true jika salah satu nilai true, sisanya false)
print("=======XOR========")
a = True
b = True
c = a ^ b
print(a,"XOR",b, "=",c)
a = True
b = False
c = a ^ b
print(a,"XOR",b, "=",c)
b = False
a = True
c = a ^ b
print(a,"XOR",b, "=",c)
a = False
b = False
c = a ^ b
print(a,"XOR",b, "=",c)