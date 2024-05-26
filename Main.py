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
