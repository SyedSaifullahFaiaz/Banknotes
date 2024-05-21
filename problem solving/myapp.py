num = input()
num = num.split()

a = float(num[0])
b = float(num[1])
c = float(num[2])
d = float(num[3])

G1 = 2 * (a / 10)
G2 = 3 * (b / 10)
G3 = 4 * (c / 10)
G4 = 1 * (d / 10)

avrg = (G1 + G2 + G3 + G4)

avrg = "{:.1f}".format(avrg)

print("Media:", avrg ,end="\n")



if float(avrg) > 7.0:
    print("Aluno aprovado.", end="\n")
elif float(avrg) < 5.0:
    print("Aluno reprovado.", end="\n")          
else:
    print( "Aluno em exame.", end="\n")

    e = float(input())

    print("Nota do exame:", e, end="\n")

    avrg = (avrg + e) / 2

    if avrg >= 5.0:
        print("Aluno aprovado.", end="\n")

        print("Media final:", avrg, end="\n")

    else:
        print("Aluno reprovado.", end="\n")  

        print("Media final:", avrg, end="\n")





