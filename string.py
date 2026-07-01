data = "ini adalah string" 
print (data)
print(type(data))

# 1. cara membuat string

'''
1. dengan menggunakan single quote = '...'
2. dengan menggunakan double quote = "..."

'''
data = 'Menggunakan single qu`ote'
print (data)

data = "menggunakan double quote"
print(data)

print('"Halo"')
print("'Halo'")
print("Halo")

# menggunakan tanda \

# membuat tanda ' menjadi string
print('mari jum\'at')
print('g\'day is\'t')

# backslash
print("C\\user\\budi")

# tab 
print("ucup\t\t\tbudi, jauh")

# backspace
print("budi \bmgus, dekat")

# newline
print("baris pertama.\nbaris kedia.") #LF -> line feed
print("baris pertama.\rbaris kedua.") #CR -> carriage retur
print("baris pertama.\r\baris kedua.") #CRF -> line feed

#3. String literal atau raw

#hati hati
print('C:\new folder') #akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : agus
Kelas : 5
Alamat : bui      
      """)

# multiline literal string dan RAW
print(r"""
    Nama : agus
    Kelas : 5
    Alamat : bui 
    web : www.budi.com/kodok  
""")