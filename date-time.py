import datetime as dt

print("Silahkan masukan tanggal \nbulan \ntahun")
tanggal = int(input("Tanggal \t :"))
bulan = int(input("Bulan \t\t :"))
tahun = int(input("tahun \t\t :"))

input_calendar = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah :{input_calendar}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal :{hari_ini}")

hitung_umur = hari_ini - input_calendar
hasil_hitung_umur = hitung_umur.days // 365
hitung_bulan = (hitung_umur.days % 365) // 30
print(f"Hari tanggal lahir anda : {input_calendar:%A}")
print(f"umur anda adalah :{hasil_hitung_umur} tahun, {hitung_bulan} bulan")
