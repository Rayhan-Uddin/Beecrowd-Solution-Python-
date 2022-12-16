A,B,C=list(map(float,input().split()))

pi = 3.14159

triangeld = 0.5 * (A * C)
radius_circle = pi * (C ** 2)
trapezium = 0.5 * (A + B) * C
square = B ** 2
ractangel = A * B
print(f"TRIANGULO: {triangeld:.3f}")
print(f"CIRCULO: {radius_circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {ractangel:.3f}")


