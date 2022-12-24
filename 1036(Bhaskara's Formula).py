import math
a,b,c=list(map(float,(input()).split()))
d=(b**2)-(4*a*c)
if d<0 or a==0:
    print("Impossivel calcular")
else:
    D=math.sqrt(d)
    R1=(-b+D)/(2*a)
    R2=(-b-D)/(2*a)
    print(f"R1 = {R1:.5f}\nR2 = {R2:.5f}")




