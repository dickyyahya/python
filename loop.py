# # print("woi")
# # # perulangan (loop)
# # # for kondisi:
# # #   aksi

# # # dengan list
# # denganList = [0,2,4,8,10]
# # print(list)
# # for b in denganList:
# #     print(b)

# # print("akhir dari program")

# # # dengan range
# # denganRange = range(1,5)
# # for i in denganRange:
# # #     print(i)

# # # # menggunakan string
# # # data_str = "koruptor mbg"

# # # for huruf in data_str:
# # #     print(huruf)

# # # latihan
# # # 1. Buat sebuah list yang berisi angka [5, 10, 15, 20, 25], lalu gunakan `for` untuk menampilkan setiap angka satu per satu.
# angka = [5,10,15,20,25]
# for i in angka:
#     print(i)
# # # 2. Buat list [2, 4, 6, 8, 10], kemudian gunakan perulangan `for` untuk menghitung jumlah seluruh angka di dalam list dan tampilkan hasilnya.
# total = 0
# angka = [2,4,6,8,10]
# for item in angka:
#     total = total + item
# print (total)
# # # 3. Gunakan `range()` untuk mencetak angka dari 1 sampai 10.
# angka = range(1,11)
# for item in angka:
#     print(item)
    
# # # 4. Gunakan `range()` untuk mencetak semua bilangan genap dari 2 sampai 20.
# angka = range(2,22,2)
# for i in angka:
#     print(i)
# # # 5. Gunakan `range()` untuk mencetak angka dari 10 hingga 1 secara menurun.
# angka = range (10,0,-1)
# for i in angka:
#     print(i)
#     print("end")
# # # 6. Buat variabel `nama = "Python"` lalu gunakan `for` untuk menampilkan setiap huruf pada variabel tersebut.
# nama = "Python"
# for i in nama:
#     print(i)
# # 7. Buat variabel `kata = "Indonesia"` lalu gunakan `for` untuk menghitung berapa banyak karakter yang ada pada string tersebut.
# jumlah = 0
# kata = "indonesia"
# for huruf in kata:
#     jumlah = jumlah + 1
# print(jumlah)
# # 8. Buat variabel `kata = "Pemrograman"` lalu gunakan `for` untuk mencetak hanya huruf vokal (a, i, u, e, o).
# kata = "Pemrograman"
# for huruf in kata:
#     if huruf == "a" or huruf == "i" or huruf == "u" or huruf == "e" or huruf == "o":
#         print(huruf)
# # 9. Buat list `nilai = [75, 80, 65, 90, 100, 55]` lalu gunakan `for` untuk mencetak hanya nilai yang lebih dari atau sama dengan 80.
# nilai = [75,80,65,90,100,55]
# for item in nilai:
#     if item >= 80:
#         print (item)

# # 10. Buat program yang menghasilkan output:
# # 1
# # 2
# # 3
# # 4
# # 5
# # Selesai
# angka = range(1,6)
# for i in angka:
#     print(i)
# print("Selesai")


# # 11. (Bonus) Buat program yang mencetak setiap karakter dari string `teks = "Belajar Python"` beserta nomor urutnya dengan format:
# # Karakter ke-1 : B
# # Karakter ke-2 : e
# # Karakter ke-3 : l
# # ...
# total = 0
# teks = "Belajar Python"
# for huruf in teks:
#     total = total + 1
#     print(f"Karakter ke-{total} {huruf}")

# latihan lagi
# Latihan Perulangan (Level 2)

# 1. Buat list:
#    angka = [3, 6, 9, 12, 15]
#    Gunakan for untuk mencetak setiap angka dikalikan 2.
# angka = [3,6,8,12,15]
# for item in angka:
#     print(item * 2)

# 2. Buat list:
#    angka = [10, 15, 20, 25, 30]
#    Gunakan for untuk menghitung jumlah seluruh angka.
# total = 0
# angka = [10,15,20,25,30]
# for item in angka:
#     total = total + item
# print(total)
# 3. Gunakan range() untuk mencetak angka 5 sampai 15.
# angka = range(5,16)
# for item in angka:
#     print(item)
# 4. Gunakan range() untuk mencetak semua bilangan ganjil dari 1 sampai 19.
# angka = range(1,19,1)
# for item in angka:
    # print(item)
# 5. Gunakan range() untuk mencetak angka dari 20 hingga 2 dengan kelipatan 2 secara menurun.
# angka = range (20,0,-2)
# for item in angka:
#     print(item)
# 6. Buat variabel:
#    nama = "Programming"
#    Gunakan for untuk mencetak setiap huruf.
# nama = "Programming"
# for huruf in nama:
#     print(huruf)
# 7. Buat variabel:
#    kata = "Universitas"
#    Gunakan for untuk menghitung jumlah karakter.
# total = 0
# kata = "Universitas"
# for huruf in kata:
#     total = total + 1
# print(total)


# 8. Buat variabel:
#    kata = "Informatika"
#    Gunakan for untuk mencetak hanya huruf konsonan.
kata = "Informatika"
for huruf in kata:
    if huruf != "a" and huruf != "i" and huruf != "I" and huruf != "u" and huruf != "e" and huruf != "o":
        print(huruf)

# 9. Buat list:
#    nilai = [45, 70, 85, 90, 60, 100]
#    Gunakan for untuk mencetak hanya nilai yang kurang dari 75.
# nilai = [45,70,85,90,60,100]
# for angka in nilai:
#     if angka < 75:
#         print(angka)

# 10. Buat program yang menghasilkan output:

# 10
# 20
# 30
# 40
# 50
# Selesai

# angka = range(10,60,10)
# for item in angka:
#     print(item)

# 11. Buat program yang mencetak setiap karakter dari string:
#     teks = "Belajar Coding"

#     Dengan format:
#     Huruf ke-1 : B
#     Huruf ke-2 : e
#     Huruf ke-3 : l
#     ...
# total = 0
# teks = "Belajar Coding"
# for huruf in teks:
#     total = total + 1
#     print(f"Huruf ke -{total}:{huruf}")
# 12. Buat list:
#     angka = [1,2,3,4,5,6,7,8,9,10]
#     Gunakan for untuk menghitung berapa banyak bilangan genap.
# jumlah = 0
# angka = [1,2,3,4,5,6,7,8,9,10]
# for item in angka:
#     if item % 2 == 0:
#         jumlah = jumlah + 1
# print(jumlah)

# 13. Buat list:
#     angka = [1,2,3,4,5,6,7,8,9,10]
#     Gunakan for untuk menghitung berapa banyak bilangan ganjil.
# jumlah = 0
# angka = [1,2,3,4,5,6,7,8,9,10]
# for item in angka:
#     if item % 2 ==1:
#         jumlah = jumlah +1
# print(jumlah)
# 14. Buat string:
#     kalimat = "Aku Belajar Python"
#     Hitung berapa banyak huruf vokal yang ada.
# jumlah = 0 
# kalimat = "Aku Belajar Python"
# for huruf in kalimat:
#     if huruf == "a" or huruf == "A" or huruf == "i" or huruf == "u" or huruf == "e" or huruf == "o":
#         jumlah = jumlah +1
# print(jumlah)
# 15. (Bonus)
#     Buat string:
#     kata = "Python"

#     Sehingga outputnya menjadi:

#     P
#     Py
#     Pyt
#     Pyth
#     Pytho
#     Python
# hasil = ""
# kata = "Python"
# for huruf in kata:
#     # print(huruf + 1)
#     hasil = hasil + huruf
#     print(hasil)