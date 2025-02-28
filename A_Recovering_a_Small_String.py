t =int(input())
letters = ['a', 'b' , 'c' , 'd' , 'e' , 'f' , 'g', 'h',
           'i', 'j' , 'k' , 'l' , 'm', 'n' , 'o' , 'p' , 'q',
           'r' , 's' , 't' , 'u' , 'v' , 'w', 'x' , 'y', 'z']

# letters = list(string.ascii_lowercase)
def determine(n):
    for a in range(len(letters)):
        for b in range(len(letters)):
            for c in range(len(letters)):
                if a+1 + b+1 + c+1 == n:
                    return  letters[a] + letters[b] + letters[c]
                

for _ in range(t):
    n = int(input())
    print(determine(n))



