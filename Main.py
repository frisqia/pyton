import time
start_time = time.time()
print("hello world")
#ini coment
"""ini komen multiline"""
a = 10
print (a)

print(time.time() - start_time, "detik")
for i in range(1,1000):
    a= 10


# kita bisa mengcompile python ke bytecode
# cara mengcompile buka terminal dan tulisan python - m py_compile Main.py
# code yang di compile terbukti lebih cepat dengan yang di interprated

# alt + shift untuk copas code
# variabel adalah tempat menyimpa data
a = 10
x = 5
panjang = 1000
print ("Nilai a = ", a) 
print ("Nilai a = ", x)
print ("Nilai a = ", panjang)

#penamaan tidak boleh pakai space/int , -,
#boleh menggunakan underscore, camelCase

nilai_y = 15
juta10 = 10000
nilaiZ= 17.5

#pemanggilan kedua
print ("Nilai a = ", a) 
a = 7
print ("Nilai a = ", a) 
#assign in direct
b = a
print ("Nilai b = ", b) 

#tipe data yang ada di pithon 
#angka (integer)
data_integer = 1
print("data:", data_integer)
print("data:", data_integer, ", bertipe:", type(data_integer))
#float : angka dengan koma

data_float = 1.5
print("data:", data_float)
print("data:", data_float, ", bertipe:", type(data_float))

#string : kumpulan karakter
data_string = "ucup"
print("data:", data_string)
print("data:", data_string, ", bertipe:", type(data_string))

#boolean : biner true/false
data_boolean = True
print("data:", data_boolean)
print("data:", data_boolean, ", bertipe:", type(data_boolean))

#data khusus
#data komplek
data_complex = complex(5,6)
print("data:", data_complex)
print("data:", data_complex, ", bertipe:", type(data_complex))

#kita bisa menggunakan tipe data dari bahasa C
from ctypes import c_double, c_char, c_buffer #dll

data_c_double = c_double(10.5)
print("data:", data_c_double)
print("data:", data_c_double, ", bertipe:", type(data_c_double))

#mengubah tipe data
data_int = 9
print("data =", data_int, "type =", type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

#data yang dimasukan pasti string
data = input("Masukan data: ")
print ("data =", data, "type =", type(data))

#jika ingin mengambil int, maka
data_int = int(input("masukan angka: "))
print("data =", data_int, "type =", type(data_int))

#jia mengambil float
angka = float(input("masukan angka: "))
print("data =", angka, "type =", type(angka))

#boolean harus di jadikan ke integer terlebih dahulu
biner = bool(int(input("masukan nilai boolean: ")))
print("data = ", biner, "type =", type(biner))

#operasi aritmatika
a = 10
b = 3

#operasi tambah
hasil = a + b
print(a,"+", b, "=" , hasil)

#operasi pengurangan
hasil = a - b
print(a,"-",b,"=" ,hasil)

#perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

#pembagian
hasil = a / b
print(a,"/", b,"=", hasil)

#eksponen (pangkat)
hasil = a ** b
print(a,"**", b, "=", hasil)

#modulus/ sisa dari hasil pembagian (persen)
hasil = a % b
print(a, "%", b ,"=", hasil)

#floor division (pembulatan hasil dari pembagian)
hasil = a // b
print(a, "//", b ,"=", hasil)

#prioritas operasi

'''
1. ()
2. exponen **
3. perkalian dan teman - teman * / ** % //
4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x ,"**", y,"*", z,"+", x,"/", y, "-", y, "%", z, "//", x, "=", hasil) 

#(x**y)*z+x/y-y%z//x =
#(xy)*z+(x/y)-(y%z)//x =
#((xy)*z)+(x/y)-((yz)//x) =
#(xyz)+(xy)-(yzx) =
#hasil

#latihan konversi satuan temperature
#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")
celcius = float(input('Masukan suhu dalam celcius:'))
print("suhu adalah", celcius, "celcius")

#reamur = (4/5)*c
reamur = (4/5) * celcius
print("suhu reamur", reamur, "reamur")
#fahrenhit = ((9/5) *c) + 32
fahrenhit =((9/5) * celcius) + 32
kelvin = ((5/9) * (fahrenhit - 32)) + 273 #kelvin ke fahrenhit
print("suhu fahrenhit", reamur, "fahrenhit")
print("suhu kelvin dalam fahrenhit", kelvin, "kelvin")
#kelvin = celcius + 273
kelvin = celcius + 273
fahrenhit =((9/5)* (kelvin -273)) + 32 #fahrenhit ke kelvin
print("suhu dalam kelvin adalah", kelvin, "Kelvin")
print("suhu fahrenhit dalam kelvin", fahrenhit, "fahrenhit")

#operasi komperasi
d = 4
e = 2
hasil = d > 3 #lebih besar
print(d,'>',3,'=',hasil) #true
hasil = e > 3 
print(e, '>', 3, '=', hasil) #false
hasil = d < 3 #kurang dari
print (d, '<', 3,'=', hasil) #false
hasil = d >= 3 #lebih dari sama dengan
print(d,'>=', 3, '=', hasil)#true
hasil = e <= 3 #kurang dari sama dengan
print(e, '<=', 3, '=', hasil) #true karena nilai e adalah 2
hasil = d != 4 #tidak sama dengan 
print(d, '!=', 4, '=', hasil) #false karena nilai d adalah 4

#"is" sebagai komparasi object identity
x = 5 #ini adalah assigment membuat object
y = 10
print ('nilai x =',x, "id =", hex(id(x)))
print ('nilai y =',y, "id =", hex(id(y)))
hasil = x is y
print("x is 5 =" , hasil) #false 
hasil = x is not y
print("x is not 5 =" , hasil) #true
hasil = x or y #or yaitu jika salah satu true maka dia akan true
print(x, 'or', y, '=', hasil)
hasil = x ^ y #xor yaitu akan true jika salah satu true sisanya false
print(x, 'xor', y, '=', hasil)
hasil = x and y #and yaitu jika dua buah nilai true maka akan menghasilkan true
print(x, 'and', y, '=', hasil)

inputUser = float (input('masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n :'))
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print(isKurangDari)
isLebihDari = (inputUser > 10)
print(isLebihDari)
isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan :', isCorrect)

#operator bitwise / biner (masing masing bit)
hasil = x|y
print('nilai: ', hasil, 'binary:', format(hasil,'08b'))
hasil = x & y
print('nilai: ', hasil, 'binary:', format(hasil,'08b'))

#manipulating
salam = "bro!"
print("normal =" + salam)
salam = salam.upper()  #huruf besar
print ("upper =" + salam) 
alay = "kece abiseZZ"
print ("normal =" + alay)
alay = alay.lower() #huruf kecil
print("lower =" + alay)
salam = "sist"
apakah_Lower = salam.islower #boolean
print(salam + "is lower =" + str(apakah_Lower))
apakah_upper = salam.isupper #boolean
print(salam + "is upper =" + str(apakah_upper))

#isalpha() <----- untuk mengecek semuanya huruf
apakah_semuaHuruf = salam.isalpha #boolean
print(salam + "is alpha =" + str(apakah_semuaHuruf))
apakah_hurufangka =  salam.isalnum #boolean
print(salam + "is alnum =" + str(apakah_hurufangka))
apakah_angkaSaja = salam.isdecimal #boolean
print(salam + "is Decimal =" + str(apakah_angkaSaja))
apakah_spasiTabNewLine = salam.isspace #boolean
print(salam + "is space =" + str(apakah_spasiTabNewLine))
apakah_semuaKatadimulaidarihurufbesar = salam.istitle #boolean
print(salam + "is title =" + str(apakah_Lower))

judul = "it is okay not to be okay"
cek_judul = judul.istitle()
print(judul + "is title =" + str(cek_judul))

cek_start = "sajangnim Oppa".startswith("sajangnim") #ngecek komponen kalimat pertama
print("start =" + str(cek_start))
end_cek = "sajangnim Oppa".endswith("Oppa") #ngecek komponen kalimat terakhir
print("start =" + str(end_cek))
pisah = ['aku', 'sayang', 'kamu'] 
gabung = ','.join(pisah) #penggabungan komponen
print(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung) #pisah

gabung = "akusayangkamu" 
print(gabung.split('ehm')) #array

#alokasi karakter
kanan = "kanan".rjust(10)
print(""+kanan+"")
kiri = "kiri".ljust(10)
print(""+kiri+"")
tengah="tengah".center(10, "@") 
print(""+tengah+"")

tengah=tengah.strip("@") #menghilangkan tanda @
print("'"+tengah+"'")

#format string
#contoh generic
nama = "cia"
format_str = f"hello {nama}"
print(format_str)
#angka
angka = 2005.5
fromat_str= f"angka = {angka}"
print(fromat_str)
#boolean
boolean= True
format_str = f"boolean{boolean}"
print(format_str)
#bilangan bulat
angka = 15
format_str= f"bilangan bulat = {angka:d}"
print(format_str)
#ribuan
angka = 3000
format_str= f"ribuan = {angka:,}" #3,000
print(format_str)
#desimal
angka = 3000.92693
format_str= f"desimal = {angka:.3f}" #3000.679
print(format_str)
#loading zero
angka = 3000.92693
format_str= f"desimal = {angka:010.3f}" #003000.927
print(format_str)
#menampilkan tanda + / -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}" #-10
format_plus = f"plus = {angka_plus:+d}" #+10
print(format_minus)
print(format_plus)
#persen
persen= 0.083
format_persen= f"persen ={persen:.2%}" #8.30%
print(format_persen)
#melakukan operasi aritmatika dalam placeholde
harga = 10000
jumlah = 9
format_string = f"harga total = Rp.{harga*jumlah:,}" #Rp.90000
print(format_string)
#format angka lain(binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}" #0b11111111
format_octal = f"octal = {oct(angka)}" #0o377
format_hex = f"hex = {hex(angka)}" #0xff
print(format_binary)
print(format_octal)
print(format_hex)

#width and multiline
# data

nama ="ucup cucup"
umur = 17
tinggi = 172.5
noSepatu = 44
#string
data_string = f"nama{nama},umur{umur},tinggi{tinggi},sepatu{noSepatu}"
print(data_string) #namaucup cucup,umur17,tinggi172.5,sepatu44
#multiline
data_string = f"""
nama = {nama}, umur = {umur}
tinggi = {tinggi}
"""
print(data_string) 
#nama = ucup cucup, umur = 17   
#tinggi = 172.5
