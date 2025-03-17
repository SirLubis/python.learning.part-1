# Level 4 secara fungsi mirip level 3 tapi bedanya gini

# Buat kondisi dimana jika salah langsung berhenti di pertama. (Kayak gerbang gitu)

# kalau benar lanjut ke bulan hijriah 
# 1=muharram
# 2=safar
# 3= rabiul awal
# Dst.


# Memberikan (int) sebelum input dan mengurung semuanya untuk menghilangkan fungsi input pada baris-baris lainnya
i=int(input("Masukkan angka 1-12 : "))

# Gerbang masuk dalam kategori

# Jangan lupa letakkan maka sepertinya yang tertera dibawah "if"
if i < 1 or i > 12 :
    maka = "Tolong baca lagi perintahnya negro"
else:
    if i==1 :
        maka="Muharram"
    elif i==2 :
        maka="Safar"
    elif i==3 :
        maka="Rabiul Awal"
    elif i==4 :
        maka="Rabiul Akhir"
    elif i==5 :
        maka="Jumadil Awal"
    elif i==6 :
        maka="Jumadil Akhir"
    elif i==7 :
        maka="Rajab"
    elif i==8 :
        maka="Sya'ban"
    elif i==9 :
        maka="Ramadhan"
    elif i==10 :
        maka="Syawal"
    elif i==11 :
        maka="Dzulqodah"
    elif i==12 :
        maka="Dzuhijjah"

print(maka)