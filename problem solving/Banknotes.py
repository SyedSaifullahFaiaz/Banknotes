num = float(input())

bankn1 = 100
bankn2 = 50
bankn3 = 20
bankn4 = 10
bankn5 = 5
bankn6 = 2


if num / bankn1 <= 0: 
    print(0, "nota(s) de R$ 100.00", end="\n" )
else:
    print(int(num / bankn1), "nota(s) de R$ 100.00", end="\n")
    num = float(num - float(num / bankn1)*bankn1)

if num / bankn2 < 1: 
    print(0, "nota(s) de R$ 50.00", end="\n" )
else:
    print(int(num/bankn2), "nota(s) de R$ 50.00", end="\n")
    num = float(num - float(num / bankn2)*bankn2)

if num / bankn3 < 1: 
    print(0, "nota(s) de R$ 20.00", end="\n" )
else:
    print(int(num/bankn3), "nota(s) de R$ 20.00", end="\n")
    num = float(num - float(num / bankn3)*bankn3)

if num / bankn4 < 1: 
    print(0, "nota(s) de R$ 10.00", end="\n" )
else:
    print(int(num/bankn4), "nota(s) de R$ 10.00", end="\n")
    num = float(num - float(num / bankn4)*bankn4)

if num / bankn5 < 1: 
    print(0, "nota(s) de R$ 5.00", end="\n" )
else:
    print(int(num/bankn5), "nota(s) de R$ 5.00", end="\n")
    num = float(num - float(num / bankn5)*bankn5)

if num / bankn6 < 1: 
    print(0, "nota(s) de R$ 2.00", end="\n" )
else:
    print(int(num/bankn6), "nota(s) de R$ 2.00", end="\n")
    num = float(num - float(num / bankn6)*bankn6)










 




















