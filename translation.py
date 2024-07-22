first_word = input()
second_word = input()


def translate(first_word, second_word):
    right = len(second_word) - 1
    left = 0

    while left < len(first_word):
        if first_word[left] == second_word[right]:
            right -=1
            left +=1
        else:
            return "NO"
        
    return "YES"


if len(first_word) != len(second_word):
    print("NO")
else:
    print(translate(first_word, second_word))


