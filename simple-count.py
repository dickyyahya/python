# latihan konversi satuan temperature
#program konversi celcius ke satuan lain

print ("\nPROGRAM KONVERSI SATUAN TEMPERATURE\n")

####CELCIUS####
# celcius
celcius = float(input('Masukan suhu dalam celcius : '))
print("Suhu dalam celcius adalah",celcius,"Celcius")
# reamur
reamur = (4/5) * celcius
print ("Suhu dalam reamur adalah", reamur,"Reamur")
#fahrenhait
fahrenhait = ((9/5) * celcius) + 32
print ("Suhu dalam fahrenhait adalah", fahrenhait,"Fahrenhait")
#kelvin
kelvin = celcius + 273
print ("Suhu dalam kelvin adalah", kelvin, "Kelvin")
###END CELCIUS####

####REAMUR####
#reamur
reamur = float(input("Masukan suhu reamur :"))
print("Suhu dalam reamur adalah :", reamur, "Reamur")
# celcius
celcius = (5/4) * reamur
print("Suhu dalam celcius adalah :", celcius,"celcius")
#fahrenhait
fahrenhait = ((9/4) * reamur) + 32
print ("Suhu dalam fahrenhait adalah :", fahrenhait,"fahrenhait")
#kelvin
kelvin = ((5/4) * reamur) + 273 
print ("Suhu dalam kelvin adalah :", kelvin, "Kelvin")

###END REAMUR###

###FAHRENHAIT###
fahrenhait = float(input("Masukan Suhu fahrenhait : "))
print("Suhu dalam fahrenhait adalah :", fahrenhait,"fahrenhait")
# celcius
celcius = (5/9) * (fahrenhait - 32)
print("Suhu dalam celcius adalah :", celcius,"celcius")
# reamur
reamur = (4/9) * (fahrenhait - 32)
print("Suhu dalam reamur adalah :", reamur,"reamur")
###END FAHRENHAIT ###

###KELVIN###
# kelvin
kelvin = float(input("Masukan Suhu Kelvin "))
print("Suhu dalam kelvin",kelvin,"kelvin")
#celcius
celcius = kelvin - 273
print("suhu dalam celcius",celcius,"celcius")
#reamur
reamur = (4/5) * (kelvin - 273)
print("suhu dalam reamur", reamur,"reamur")

####END KELVIN###