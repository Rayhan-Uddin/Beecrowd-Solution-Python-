a = float(input())
# intervals the number
# belongs: [0,25] (25,50], (50,75], (75,100].
# If the read number is less than zero or
# greather than 100, the program must print the message
# “Fora de intervalo” that means "Out of Interval".
if a>=0 and a <= 25:
    print("Intervalo (0,25]")
elif a > 25 and a <= 50:
    print("Intervalo (25,50]")
elif a > 50 and a <= 75:
    print("Intervalo (50,75]")
elif a > 75 and a <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
