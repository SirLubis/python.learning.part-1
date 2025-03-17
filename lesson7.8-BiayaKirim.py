# Latihan Soal 1

# Dibaca 2 buah nilai integer sembarang yang merepresentasikan berat barang 
# (kg) dan jarak pengiriman (km), maka buatlah teks algoritma untuk 
# menghitung biaya pengiriman barang berdasarkan berat dan jarak. Aturan 
# biaya pengiriman adalah: Biaya dasar: Rp10.000, Biaya perkg: Rp5.000, dan
# Biaya per km: Rp2.000. <<Nama File: BiayaKirim>>

# Inisialisasi
bd = 10000

# Input 
s = input("Masukkan berat barang (per kilogram) : ")
j = input("Masukkan jarak pengiriman (per kilometer) : ")

# Output
a = (s * 5000 ) + (j * 2000) + bd

# Print
print(a)