import time
start_time = time.time()

print ('Hello World!')
print (9)
print(True)
for i in range (1,1000):
    a=10
print(time.time()-start_time,'detik')

# compile python ke bytecode
# terminal python -m py_compile main.py
# cd __pycache__ trs run python main + tab

############################################
#variabel adalah tempat menyimpan data

#assigment Nilai
a = 10
b = 50
hewan = 'Burung'
jumlahBurung = 5

#pemanggilan pertama
print ('Saya mempunyai', hewan ,'sebanyak', jumlahBurung)

#penamaan
nilai_y = 70
juta50 = 50000000
nilaiZ = 20000

#pemanggilan kedua
print ("Berapa nilai y", nilai_y, "dan", "Berapa harga sawit 1 kuintal",juta50,"Berapa harga sate 1 kodi",nilaiZ)

