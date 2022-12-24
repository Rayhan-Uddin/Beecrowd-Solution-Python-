salary = float(input())

if(salary > 0 and salary <= 2000):
 print(f"Isento")
elif(salary > 2000 and salary <= 3000):
 resto = salary - 2000
 resultado = resto * 0.08
 print(f"R$ {resultado:0.2f}")
elif(salary > 3000 and salary < 4500):
 resto = salary - 3000
 resultado = (resto * 0.18) + (1000 * 0.08)
 print(f"R$ {resultado:0.2f}")
else:
 resto = salary - 4500
 resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
 print(f"R$ {resultado:0.2f}")