num = int(input("Enter the number: "))

i = 0
while i <= num:
    sum = int(i * (i + 1) / 2)
    i += 1

print(sum)