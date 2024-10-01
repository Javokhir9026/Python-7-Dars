import os
os.system("cls")
f = open("Fayl.txt","w")
n = int(input("Qancha qiymat kiritasiz: "))
for i in range(n):
    i = input(f"{i+1}-qiymat: ")
    f.write(i)
f = open("Fayl.txt","r")
matn = f.read()
ls = []
for i in matn:
    for j in range(i+1):
        ls[j] = i
print(ls)
f2 = open("New_Fayl.txt","w")


f.close()
f2.close()