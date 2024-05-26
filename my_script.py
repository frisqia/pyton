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
