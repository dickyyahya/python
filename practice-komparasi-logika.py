# # # kasus ++++++++3-------10++++++
# # # inputUser=float(input("masukan angka :"))
# # # nilaiKurang3 = inputUser <= 3 
# # # nilaiLebih10 = inputUser >= 10
# # # hasilKeduanya = nilaiKurang3 or nilaiLebih10
# # # print("nilai", hasilKeduanya )

# # # kasus ------3++++++10-------
# # inputUser = float(input("masukan nilai :"))
# # nilaiKurang3 = inputUser >= 3 
# # nilaiLebih10 = inputUser <= 10
# # hasilKeduanya = nilaiKurang3 and nilaiLebih10
# # print("nilai", hasilKeduanya )

# #--------0+++++++5------8+++++11-----
# # inputUser = float(input("masukan nilai :"))
# # a = inputUser > 0
# # b = inputUser < 5
# # c = inputUser > 8
# # d = inputUser < 11

# # print (a and b or c and d) 

# #++++++++0---------5++++++8------11++++++
# inputUser = float(input("masukan nilai :"))
# a = inputUser < 0
# b = inputUser > 5
# c = inputUser < 8
# d = inputUser > 11

# print (a or (b and c) or d ) 




# =========================
# LATIHAN LOGIKA BOOLEAN
# =========================

# Soal 1
# ++++++-4------9++++++
x = float(input("Masukkan nilai: "))
print(x < -4 or x > 9)

# Soal 2
# ------2++++++++6------
x = float(input("Masukkan nilai: "))
print(x > 2 and x < 6)

# Soal 3
# ++++0------5++++
x = float(input("Masukkan nilai: "))
print(x < 0 or x > 5)

# Soal 4
# ------3++++7------12++++
x = float(input("Masukkan nilai: "))
print(x > 3 and x < 7 or x > 12 )

# Soal 5
# ++++-8------1++++5------10++++
x = float(input("Masukkan nilai: "))
print(x < -8 or (x > 1 and x < 5 ) or x > 10 )

# Soal 6
# ------0++++4------8++++12------
x = float(input("Masukkan nilai: "))
print(x > 0 and x < 4 or x > 8 and x < 12)

# Soal 7
# ++++-15------5++++10------20++++
x = float(input("Masukkan nilai: "))
print(x < -15 or x > 5 and x < 10 or x > 20)

# Soal 8
# ------10++++-2------3++++9------
x = float(input("Masukkan nilai: "))
print(x > -10 and x < -2 or x > 3 and x < 9)

# Soal 9
# ++++-20-------5++++0------6++++15------
x = float(input("Masukkan nilai: "))
print(x<-20 or x > -5 and x < 0 or x > 6 and x < 15)