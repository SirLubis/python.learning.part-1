# Buatlah teks algoritma, jika diberikan 3 buah inputan bilangan integer positif 
# (>0) sembarang yang merepresentasikan sisi-sisi segitiga. Tuliskanlah ke
# layar dari ke-3 inputan tersebut termasuk Segitiga Sama Sisi, atau Segitiga 
# Sama Kaki, atau Segitiga Sembarang. Jika salah satu atau lebih inputan yang 
# dimasukan adalah bilangan Nol atau Negatif (<= 0), maka dilayar akan 
# dikeluarkan pesan “Terdapat nilai yang bukan sisi segitiga”. Asumsi ketiga 
# buah bilangan integer tersebut dipastikan sudah membentuk segitiga. 
# <nama:CekSegitiga> {versi 2: Aturan segitiga Jumlah kedua sisinya harus lebih besar dari salah satu sisinya}

judul="Alat penebak segitiga"
print(judul)

a=int(input("Masukan panjang sisi 1 : "))
b=int(input("Masukan panjang sisi 2 : "))
c=int(input("Masukan panjang sisi 3 : "))

if a<=0 or b<=0 or c<=0 :
    maka="Ada angka yang tidak bisa didefinisikan (Harus lebih dari nol)"
else :
    if a==b==c :
        maka="Segitiga sama sisi"
    elif a==b!=c or b==c!=a or c==a!=b :
        maka="Segitiga sama kaki"
    elif a!=b!=c :
        maka="Segitiga sembarang"

print(maka)