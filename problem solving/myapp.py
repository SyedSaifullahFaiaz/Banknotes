age = int(input())

yrs = int(age / 365)
age = age - (yrs * 365)

months = int(age / 30)
age = age - (months * 30)

days = int(age)

print(yrs, "ano(s)", end="\n")
print(months, "mes(es)", end="\n")
print(days, "dia(s)", end="\n")