#we are looking for how many times the note or coin can go into the value
#i.e the number / the note or coin. 
#we then output that value as an integer
# we then need to calculate what the remaining value of out number is
# we can do this by multiplying the amount that the note or coin goes into our number by the note or coin in question
# then we take that value away from our number
# i.e number - ((number / note or coin) * note or coin) 
# we then move onto the next note or coin and repeat this process

num = float(input())

bankn1 = 100
bankn2 = 50
bankn3 = 20
bankn4 = 10
bankn5 = 5
bankn6 = 2

coin1 = 1.00
coin2 = 0.50
coin3 = 0.25
coin4 = 0.10
coin5 = 0.05
coin6 = 0.01

print("NOTAS:")
#$100
if num / bankn1 < 1:
    print(0, "nota(s) de R$ 100.00", end="\n" )
else:
    print(int(num / bankn1), "nota(s) de R$ 100.00", end="\n")
    num = float(num - int(num / bankn1)*bankn1)

#$50
if num / bankn2 < 1:
    print(0, "nota(s) de R$ 50.00", end="\n" )
else:
    print(int(num / bankn2), "nota(s) de R$ 50.00", end="\n")
    num = float(num - int(num / bankn2)*bankn2)
    
#$20
if num / bankn3 < 1:
    print(0, "nota(s) de R$ 20.00", end="\n" )
else:
    print(int(num / bankn3), "nota(s) de R$ 20.00", end="\n")
    num = float(num - int(num / bankn3)*bankn3)
    
#$10
if num / bankn4 < 1:
    print(0, "nota(s) de R$ 10.00", end="\n" )
else:
    print(int(num / bankn4), "nota(s) de R$ 10.00", end="\n")
    num = float(num - int(num / bankn4)*bankn4)
    
#$5
if num / bankn5 < 1:
    print(0, "nota(s) de R$ 5.00", end="\n")
else:
     print(int(num / bankn5), "nota(s) de R$ 5.00", end="\n")
     num = float(num - int(num / bankn5)*bankn5)
     
   

 #$2

#$2.00
if num / bankn6 < 1:
    print(0, "nota(s) de R$ 2.00", end="\n" )
else:
    print(int(num / bankn6), "nota(s) de R$ 2.00", end="\n")
    num = float(num - int(num / bankn6)*bankn6)
    
print("MOEDAS:")
#$1
if num / coin1 < 1:
    print(0, "moeda(s) de R$ 1.00", end="\n" )
else:
    print(int(num / coin1), "moeda(s) de R$ 1.00", end="\n")
    num = float(num - int(num / coin1)*coin1)
    
#$0.50
if num / coin2 < 1:
    print(0, "moeda(s) de R$ 0.50", end="\n" )   
else:
    print(int(num / coin2), "moeda(s) de R$ 0.50", end="\n")
    num = float(num - int(num / coin2)*coin2)
    
#$0.25
if num / coin3 < 1:
    print(0, "moeda(s) de R$ 0.25", end="\n" )   
else:
    print(int(num / coin3), "moeda(s) de R$ 0.25", end="\n")
    num = float(num - int(num / coin3)*coin3)
    
#$0.10
if num / coin4 < 1:
    print(0, "moeda(s) de R$ 0.10", end="\n" )   
else:
    print(int(num / coin4), "moeda(s) de R$ 0.10", end="\n")
    num = float(num - int(num / coin4)*coin4)

#$0.05
if num / coin5 < 1:
    print(0, "moeda(s) de R$ 0.05", end="\n" )   
else:
    print(int(num / coin5), "moeda(s) de R$ 0.05", end="\n")
    num = round((num - int(num / coin5)*coin5), 2)

#$0.01
if num / coin6 < 1:
    print(0, "moeda(s) de R$ 0.01", end="\n" )   
else:
    print(int(num / coin6), "moeda(s) de R$ 0.01", end="\n")
    num = float(num - int(num / coin6)*coin6)




