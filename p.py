import os
os.system("cls")

ls = [30,50,60,90,80]
m = max(ls)
mi = min(ls)
s  = 0
for i in ls:
    if not i == m and not i == mi:
        s += i
ort = float
ort = s / 3
print(s)
print(ort)