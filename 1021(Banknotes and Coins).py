#type 1
'''A=float(input())
rs_100=A//100
rs_50=A%100 //50
rs_20=(A%100)%50 //20
rs_10=(A%100)%50 %20//10
rs_5=(A%100)%50 %20%10//5
rs_2=(A%100)%50 %20%10%5//2

#MEDAS
rs_1=(A%100)%50 %20%10% 5% 2//1

rs_0_50=(A%100)%50 %20%10% 5% 2%1//0.50
rs_0_25=(A%100)%50 %20%10% 5% 2%1%0.50//0.25
rs_0_10=(A%100)%50 %20%10% 5% 2%1%0.50%0.25//0.10
rs_0_05=(A%100)%50 %20%10% 5% 2%1%0.50%0.25%0.10//0.05
rs_0_01=(A%100)%50 %20%10% 5% 2%1%0.50%0.25%0.10%0.05//0.01
print("NOTAS:")
print(f"{rs_100} nota(s) de R$ 100.00 ")
print(f"{rs_50} nota(s) de R$ 50,00")
print(f"{rs_20} nota(s) de R$ 20,00")
print(f"{rs_10} nota(s) de R$ 10,00")
print(f"{rs_5} nota(s) de R$ 5,00")
print(f"{rs_2} nota(s) de R$ 2,00")

print("MOEDAS:")
print(f"{rs_0_50} nota(s) de R$ 0.50")
print(f"{rs_0_25} nota(s) de R$ 0.25")
print(f"{rs_0_10} nota(s) de R$ 0.10")
print(f"{rs_0_05} nota(s) de R$ 0.05")
print(f"{rs_0_01} nota(s) de R$ 0.01")
'''

#type 2
from typing import List

a = float(input())
if a>=0 and a<=1000.00:
    notas:list[int]=[100, 50, 20, 10, 5, 2]
    meodaas=[1, 0.50, 0.25, 0.10, 0.05,0.01]
print("NOTAS:")
for i in notas:
    print(f"{int(a / i)} nota(s) de R$ {i}.00")
    a = float(f'{a % i:.2f}')

print("MOEDAS:")

for i in meodaas:
    print(f"{int(a / i)} nota(s) de R$ {i:.2f}")
    a = float(f'{a % i:.2f}')
#type 3
'''
A=float(input())
N=A
a=N/100
b=N%100
c=b/50
d=b%50
e=d/20
f=d%20
g=f/10
h=f%10
i=h/5
j=h%5
k=j/2
l=j%2

E=A*100
B=(int(E))
m=B%100
n=m/50
o=m%50
p=o/25
q=o%25
r=q/10
s=q%10
t=s/5
u=s%5
print("NOTAS:")
print(f"{int(a)} nota(s) de R$ 100.00")
print(f"{int(c)} nota(s) de R$ 50.00")
print(f"{int(e)} nota(s) de R$ 20.00")
print(f"{int(g)} nota(s) de R$ 10.00")
print(f"{int(i)} nota(s) de R$ 5.00")
print(f"{int(k)} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{int(l)} moeda(s) de R$ 1.00")
print(f"{int(n)} moeda(s) de R$ 0.50")
print(f"{int(p)} moeda(s) de R$ 0.25")
print(f"{int(r)} moeda(s) de R$ 0.10")
print(f"{int(t)} moeda(s) de R$ 0.05")
print(f"{int(u)} moeda(s) de R$ 0.01")''''''