print(20*"=")
print("SIMPLE CALCULATOR")
print(20*"-")
angka1 = int(input("masukan angka ke 1 : "))
operator = input("masukan operator (+,-,*,/) : ")
angka2 = int(input("masukan angka ke 2 : "))
# tambah = "+"

if operator == "+":
    hasil =  angka1 + angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil =  angka1 - angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "*" or operator=="x":
    hasil =  angka1 * angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil =  angka1 / angka2
    print(f"hasilnya adalah {hasil}")
else:
    print("ngawur")
print("done")


