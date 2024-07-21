number = input()
number = number.split(" ")
k = int(number[-1])
number = int(number[0])

for i in range(k):
    if number % 10 == 0:
        number //= 10
    else:
        number -= 1

print(number)