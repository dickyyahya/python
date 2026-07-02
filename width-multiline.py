# width and multiline

# data

nama = "agus"
umur = 30
tinggi = 180
nomor_sepatu = 50

# string standar
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi} , nomor sepatu {nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline dengan menggunakan enter, newline \n
data_string = f"nama = {nama}, \numur = {umur}, \ntinggi = {tinggi} , \nnomor sepatu {nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {nama}
umur = {umur}

tinggi = {tinggi}
nomor sepatu = {nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_string = f"""
nama = {nama:>9}
umur = {umur:>8}
tinggi = {tinggi:>4}
nomor sepatu = {nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)