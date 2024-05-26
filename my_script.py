import datetime as dt

hari_ini = dt.date.today() # memunculkan tanggal hari ini
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}") #%A memunculkan harinya
tanggal = dt.date(2005,10,10)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")

print("silahkan masukan anggal, \nbulan dan tahun\n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Hari lahir anda adalah :{tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

#hitung umur
hari_ini = dt.date.today()
umur = hari_ini - tanggal_lahir
print(f"umur anda adalah: {umur}") #umur hari
umur_tahun = umur.days// 365
print(umur)
print(f"umur anda adalah : {umur_tahun}") #umur tahun
umur_bulan_sisa = (umur.days % 365)//30
print(f"umur anda adalah: {umur_bulan_sisa} bulan") #sisa bulan

#if
nama = input("siapa nama anda?")
if nama == "ucup" : print("kece badai") 
print(f"terimakasih {nama}")

#space berarti masih berada di dalam fungsi
if nama == "ucup": 
    print("kamu ganteng abiess")
    print("kamu juga kece")
    print(f"terimakasih {nama}")
else:
    print("kamu bukan ucup")

if nama == "cia":
    print("hai besstie")
elif nama == "kokoh":
    print("hai koh")
elif nama == "oppa":
    print('anyoeng')
else:
    print("salam kenal")
print("ini adalahh akhir program")

#kalkulator sederhana
print(10*"=")
print("kalkulator sederhana")
print(10*"=" + "\n")
angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukan angka 2 : "))

#percabangan
if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "_":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("masukan yg bener dong!")
print("akhir program")

#looping (perulangan/percabangan)
angka= [0,1,2,3,4]
for i in angka:
    print(f"i sekarang -> {i}") #i sekarang -> 0,i sekarang -> 1,i sekarang -> 2,i sekarang -> 3,i sekarang -> 4
print("akhir dari program")

#dengan range
angka_range = range(1,5) #dimuai dari 1 dan berhenti sebelum angka 5
for i in angka_range:
    print(f"i sekarang -> {i}") #i sekarang -> 1,i sekarang -> 2,i sekarang -> 3,i sekarang -> 4
print("akhir dari program")

#contoh lain
angka_range = range(1,10) #dimuai dari 1 dan berhenti sebelum angka 10
for i in angka_range:
    print("saya kece") #akan memunculkan saya keren sebanyak 8kali
print("akhir dari program")

#menggunakan string / looping per huruf
data_str= "saya ganteng abies" 
for huruf in data_str:
    print(huruf) #saya ganteng abies menjadi horizontal
print("akhir dari program")

# #while loop
# angka = 10
# while angka > 5:
#     print("cia cantik") #akan berjalan terus karena dia true maka akan berjalan terus
# print("cukup")
# angka = 0
# while angka < 5:
#     angka += 1
#     print(f"angka sekarang ->{angka}") #cia cantik,angka sekarang ->2,cia cantik,angka sekarang ->3,cia cantik,angka sekarang ->4,cia cantik,angka sekarang ->5,cia cantik
#     print("cia cantik") 
# print("cukup")

#continue, pass, break
#pass -> berfungsi sebagai dummy, tidak akan di eksekusi
angka = 0
while angka < 5:
    angka +=1
    if angka == 3:
        print("whadap") # maka akan di declare setelah angka 2 kemudian lanjut ke angka 3 hingga terakhir
    print(angka)

#pass
angka = 0
while angka < 5:
    angka +=1
    if angka == 3:
        pass #ini tidak akan dieksekusi jadi akan nge loop hingga angka terakhir
    print(angka)


 #continue
angka = 0
while angka < 5:
     angka +=1
     if angka == 3:
         print("nice!") #whatsupp! whatsupp!,nice!,whatsupp!,whatsupp!,finish
         continue #ini tidak akan dieksekusi
     print("whatsupp!") # akan membuat loop meloncat ke step selanjutnya
print("finish")

#break
angka = 0
while angka < 5:     
    angka +=1
    if angka == 3:
        print("nice!") #whatsupp!,whatsupp!,nice!,finish
        break #dia hanya berhenti mengeksekusi jadi setelah nice berhenti
    print("whatsupp!") # akan membuat loop meloncat ke step selanjutnya
print("finish")

#perulangan membuat segitiga
sisi = 4
#dummy variable
count = 1
for i  in range(sisi):
    print("*"*count) #*,**,***,****
    count += 1

print("akhir for")
#menggunakan while
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
print("akhir while")

#ganjil saja
print("awal while")
sisi = 10
count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    if (count%2): 
        print(" "*spasi,"+",*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break # akan berhenti jika count melebihi sisi
print("akhir ganjil")

#List
#kumpulan data number
data_angka = [1,2,3]
print(data_angka)

#kumpulang data string
data_str = ["cia", "jojo", "ilham"]
print(data_str)

#kumpulan data boolean
data_bool =[True,False, True]
print(data_bool)

#kumpulan campuran
data_mix = [1,"ayam",2, "japri", "jaja",True]
print(data_mix)

# alternatif membuat list
data_range = range(0,10) #range(0, 10)
print(data_range)
data_list = list(data_range)
print(data_list) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#list denan for loop
dataListFror = [i **2 for i in range(0,10)] 
print(dataListFror) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#list pakai for if
listForIf =[i for i in range(0,10) if i != 5]
print(listForIf) #[0, 1, 2, 3, 4, 6, 7, 8, 9]

listForIf =[i for i in range(0,10) if i%2 == 0]
print(listForIf) #[0, 2, 4, 6, 8]