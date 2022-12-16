
X_1,Y_1=list(map(float,input().split()))
X_2,Y_2=list(map(float,input().split()))

distance_1  =(X_2-X_1)**2 + (Y_2-Y_1)**2
distance=distance_1**0.5
print(f"{distance:.4f}")