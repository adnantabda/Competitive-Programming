test = int(input())
words = []
for i  in range(test):
    new_word = input()
    words.append(new_word)
    
for word in words:
    if len(word) > 10:
        new_word = "".join([word[0], str(len(word) - 2), word[-1]])
        print(new_word)
    else:
        print(word)
        
