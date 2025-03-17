# input : i
# proses : 
# jika i = 0 output 'nol',
# jika i > 0 output 'positif',
# jika i < 0 outputnya 'negatif'

i = input("Masukan angka : ")

# Menggunakan if untuk awalan
# Menggunakan elif dibagian pertengahan
# Menggunakan else jika jawabannya sudah pasti

if(int(i))==0 :
    jwb="nol"
elif(int(i))>0 :
    jwb="positif"
else :
    jwb="negatif"

print(jwb)