length = int(input())
string = input()
storage = set()
if length < 26:
    print("NO")
else:
    for i in string:
        i = i.lower()
        if i not in storage:
            storage.add(i)
        

    if len(storage) >= 26:
        print("YES")
    else:
        print("NO")