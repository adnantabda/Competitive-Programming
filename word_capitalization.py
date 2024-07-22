word = input()
letters = []

for i in range(len(word)):
    if i == 0:
        letters.append(word[i].upper())

    else:
        letters.append(word[i])



new_word = ''.join(letters)

print(new_word)