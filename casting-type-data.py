# Casting
# Merubah satu data ke tipe lain
# tipe data = int, floar, str, bool

print("====INT====")
data_int = 1

print ("data =", data_int,"type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data float =", data_float, "type =", type(data_float) )
print("data string =", data_str, "type", type(data_str))
print("data bool =", data_bool, "type",type(data_bool)) #akan false jika int 0

#FLOAT
print("===FLOAT===")

data_float = 8.9
print("data =",data_float,"type data",type(data_float))

data_str = str(data_float)
data_int = int(data_float)
data_bool = bool(data_float)

print("data string",data_str,"type =",type(data_str))
print("data integer",data_int,"type =", type(data_int)) #akan dibulatkan kebawah
print ("data boolean =", data_bool,"type =",type(data_bool))

#BOOLEAN
print("===BOOLEAN===")
data_bool = False
print("data bool =",data_bool,"type",type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("data int =", data_int, "type =",type(data_int))
print("data str =", data_str,"type =",type(data_str))
print("data float =", data_float, "type =", type(data_float))

#STRING
print("====STRING====")
data_string=""
print("data string =", data_string,"type= ",type(data_string))

data_bool = bool(data_string) #false jika string kosong
data_int = int(data_string) #string harus angka
data_float = float(data_string) ##string harus angka

print("data bool =",data_bool, "type =", type(data_bool))
print("data int =", data_int, "type =",type(data_int))
print("data float =",data_float,"type =", type(data_float))




