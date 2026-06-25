#input user
#data yang dimasukan selalu string
data = input("masukan data : ")
print(data,type(data))

# jika kita ingin mengambil int
number_int = int(input("masukan data"))
print("number_int", number_int, type(number_int))

number_float = float(input("masukan data"))
print("float", number_float, type(number_float))

#boolean
boolean = bool(int(input("masukan angka")))
print("boolean", boolean, type(bool))