# format string
# string
nama  = "yanto"
format_str = f"hello {nama}"
print(format_str)

# boolean 
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka 
angka = 888.9
format_str = f"angka {angka}"
print(format_str)

# bilangan bulat
angka = 45
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan 
angka = 90000000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 888.2387
format_str = f"desimal {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 888.2387
format_str = f"desimal {angka:010.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 90
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen ={persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 3000
jumlah = 9

format_string = f"harga total =Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (binary,octal, hexadesinal )
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)






