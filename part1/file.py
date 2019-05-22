jenis = str(input("Jenis : "))
kode = int(input("Kode : "))
harga = int(input("Harga : "))

if jenis is 'a':
    diskon = harga * 0.1
elif jenis is 'b':
    diskon = harga * 0.15
elif jenis is 'c':
    diskon = harga * 0.2
else:
    diskon = 0

harga = harga - diskon

print("Harga setelah didiskon : ", harga)
