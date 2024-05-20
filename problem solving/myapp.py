num = input()

num = num.split()
X = int(num[0])
Y = int(num[1])

Menu = {1 : 4.00, 2 : 4.50, 3 : 5.00, 4 : 2.00, 5 : 1.50}

if X in Menu:
    price = Menu[X]

    total_cost = price * Y

    print("Total: R$ ", f"{total_cost:.2f}", end="\n")

# if X == 1:
#     print("Total: R$ ", f"{4.00 * Y:.2f}", end="\n")
# elif X == 2:
#     print("Total: R$ ", f"{4.50 * Y:.2f}", end="\n")
# elif X == 3:
#     print("Total: R$ ", f"{5.00 * Y:.2f}", end="\n")
# elif X == 4:
#     print("Total: R$ ", f"{2.00 * Y:.2f}", end="\n")
# elif X == 5:
#     print("Total: R$ ", f"{1.50 * Y:.2f}", end="\n")
# else:
#     num = input()




