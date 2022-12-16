A=int(input())
rs_100=A//100
rs_50=A%100 //50
rs_20=(A%100)%50 //20
rs_10=(A%100)%50 %20//10
rs_5=(A%100)%50 %20%10//5
rs_2=(A%100)%50 %20%10%5//2
rs_1=(A%100)%50 %20%10% 5% 2//1
print(f"{rs_100} nota(s) de R$ ")
print(f"{rs_50} nota(s) de R$ 50,00")
print(f"{rs_20} nota(s) de R$ 20,00")
print(f"{rs_10} nota(s) de R$ 10,00")
print(f"{rs_5} nota(s) de R$ 5,00")
print(f"{rs_2} nota(s) de R$ 2,00")
print(f"{rs_1} nota(s) de R$ 1,00")

"""a=int(input())
print(a)
for i in [100, 50, 20, 10, 5, 2, 1]:
    print(f"{a//i} nota(s) de R$ {i},00")
    a=a%i  """