# operasi komparasi

# setiap hasil dari operasi komparasi adalah booleaan (true or false)
# >,<,>=,=>,==,!=, is, is not

a = 8
b = 7


# lebih besar dari >
print("\n===LEBIH (>) DARI===\n")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = a > 9
print(a,">",9,"=",hasil)
hasil = b > 7
print(b,">",7,"=",hasil)

print("\n===KURANG (<) DARI===\n")
# kurang dari <
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = a < 9
print(a,"<",9,"=",hasil)
hasil = b < 7
print(b,"<",7,"=",hasil)

print("\n===LEBIH (>=) DARI SAMA DENGAN===\n")
# lebih dari >=
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = a >= 9
print(a,">=",9,"=",hasil)
hasil = b >= 7
print(b,">=",7,"=",hasil)

print("\n===KURANG (<=) DARI SAMA DENGAN===\n")
# kurang dari sama dengan <=
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = a <= 9
print(a,"<=",9,"=",hasil)
hasil = b <= 7
print(b,"<=",7,"=",hasil)

print("\n===  SAMA (==) DENGAN===\n")
# sama dengan ==
hasil = a == 3
print(a,"==",3,"=",hasil)
hasil = a == 9
print(a,"==",9,"=",hasil)
hasil = b == 7
print(b,"==",7,"=",hasil)

print("\n===  TIDAK SAMA (!=) DENGAN===\n")
# sama dengan !=
hasil = a != 3
print(a,"!=",3,"=",hasil)
hasil = a != 9
print(a,"!=",9,"=",hasil)
hasil = b != 7
print(b,"!=",7,"=",hasil)

# 'is' sebagai komparasi object indentity
print("\n===  object (is) identity===\n")
x = 5
y = 5
print (hex(id(x)))
print (hex(id(y)))

hasil = x is y
print(hasil)

# 'is not' sebagai komparasi object indentity
print("\n===  object (is not) identity===\n")
x = 5
y = 5
print (hex(id(x)))
print (hex(id(y)))

hasil = x is not y
print(hasil)
