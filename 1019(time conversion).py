sec=int(input())
min=sec//60
sec=sec % 60
hour=min//60
min=min%60

print(f"{hour:.0f}:{min:.0f}:{sec:.0f}")