A,B,C,D=list(map(int,(input()).split()))
#if B is greater than C and D is greater than A and
# if the sum of C and D is greater than
# the sum of A and B and if C and D were positives values and
# if A is even, write the message
if B>C and D>A and C+D>A+B and D>0 and (A % 2) == 0 :
    print("Valores aceitos")
else:   print("Valores nao aceitos")