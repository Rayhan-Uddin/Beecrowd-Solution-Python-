x,y=list(map(int,(input()).split()))

if x==1:
    print(f"Total: R$ {float(4.00*y):.2f}")
elif x==2:
    print(f"Total: R$ {float(4.50*y):.2f}")
elif x == 3:
    print(f"Total: R$ {float(5.00 * y):.2f}")
elif x == 4:
    print(f"Total: R$ {float(2.00 * y):.2f}")
elif x==5:
    print(f"Total: R$ {float(1.50*y):.2f}")

