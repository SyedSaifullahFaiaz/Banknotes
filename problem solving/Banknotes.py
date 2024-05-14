num = float(input())

bankn1 = 50
bankn2 = 20
bankn3 = 10
bankn4 = 5
Coin1 = 2
Coin2 = 1
Coin3 = 0.50
Coin4 = 0.20
Coin5 = 0.10
Coin6 = 0.05
Coin7 = 0.02
Coin8 = 0.01

print(num)
if num / bankn1 < 1: 
    print(0, "£50 notes", end="\n" )
else:
    print(int(num / bankn1), "£50 notes", end="\n")
    num = float(num - int(num / bankn1)*bankn1)

#£20
if num / bankn2 < 1: 
    print(0, "£20 notes ", end="\n" )
else:
    print(int(num/bankn2), "£20 notes ", end="\n")
    num = float(num - int(num / bankn2)*bankn2)

#£10
if num / bankn3 < 1: 
    print(0, "£10 notes", end="\n" )
else:
    print(int(num/bankn3), "£10 notes", end="\n")
    num = float(num - int(num / bankn3)*bankn3)

#£5
if num / bankn4 < 1: 
    print(0, "£5 notes", end="\n" )
else:
    print(int(num/bankn4), "£5 notes", end="\n")
    num = float(num - int(num / bankn4)*bankn4)

#£2
if num / Coin1 < 1: 
    print(0, "£2 coins", end="\n" )
else:
    print(int(num/Coin1), "£2 coins", end="\n")
    num = float(num - int(num / Coin1)*Coin1)

#£1
if num / Coin2 < 1: 
    print(0, "£1 coins", end="\n" )
else:
    print(int(num/Coin2), "£1 coins", end="\n")
    num = float(num - int(num / Coin2)*Coin2)

#50p
if num / Coin3 < 1: 
    print(0, "50p coins", end="\n" )
else:
    print(int(num/Coin3), "50p coins", end="\n")
    num = float(num - int(num / Coin3)*Coin3)

#20p
if num / Coin4 < 1: 
    print(0, "20p coins", end="\n" )
else:
    print(int(num/Coin4), "20p coins", end="\n")
    num = float(num - int(num / Coin4)*Coin4)

#10p
if num / Coin5 < 1: 
    print(0, "10p coins", end="\n" )
else:
    print(int(num/Coin5), "10p coins", end="\n")
    num = float(num - int(num / Coin5)*Coin5)

#5p
if num / Coin6 < 1: 
    print(0, "5p coins", end="\n" )
else:
    print(int(num/Coin6), "5p coins", end="\n")
    num = float(num - int(num / Coin6)*Coin6)

#2p
if num / Coin7 < 1: 
    print(0, "2p coins", end="\n" )
else:
    print(int(num/Coin7), "2p coins", end="\n")
    num = float(num - int(num / Coin7)*Coin7)

#1p
if num / Coin8 < 1: 
    print(0, "1p coins", end="\n" )
else:
    print(int(num/Coin8), "1p coins", end="\n")
    num = float(num - int(num / Coin8)*Coin8)







 




















