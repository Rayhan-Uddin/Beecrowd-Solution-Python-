n1,n2,n3,n4=list(map(float,(input()).split()))

avrg=(n1*2+n2*3+n3*4+n4*1)/(10)
print(f"\nMedia: {avrg:.1f}")
if avrg>=7.00:
    print("Aluno aprovado.")
elif avrg<5:
    print('Aluno reprovado.')
elif avrg>=5.0 and avrg<=7 :
    print("Aluno em exame.")
    m=float(input())
    print(f"Nota do exame: {m:.1f}")
    m=(avrg+m)/2
    if m>5.0:
        print("Aluno aprovado.")
        print(f"Media final: {m:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {m:.1f}")

