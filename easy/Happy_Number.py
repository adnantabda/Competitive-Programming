

def is_happy(n):
    numbers = [int(d) ** 2 for d in str(n)]
    number = sum(numbers)
    collection = []
    while number != 1 and number not in collection:
        collection.append(number)
        return is_happy(number)

    return number == 1





print(is_happy(2))
