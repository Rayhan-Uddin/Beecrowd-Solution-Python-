a,b,c=list(map(float,(input()).split()))
ar=0.5*(a+b)*(c)
prmt = a+b+c
if a+b>c and a+c>b and b+c>a:
    print(f"Perimetro = {prmt:.1f}")

else:
    print(f"Area = {ar:.1f}")




