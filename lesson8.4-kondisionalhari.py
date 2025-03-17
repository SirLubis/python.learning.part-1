# Nama hari

i = input("Masukan nama hari : ")


if(int(i))==1 :
    maka="Ahad"
elif(int(i))==2 :
    maka="Senin"
elif(int(i))==3 :
    maka="Selasa"
elif(int(i))==4 : 
    maka="Rabu"
elif(int(i))==5 :
    maka="Kamis"
elif(int(i))==6 :
    maka="Jum'at"
elif(int(i))==7 :
    maka="Sabtu"
else:
    maka="Kesalahan, tolong ketik ulang nama harinya"

print(maka)