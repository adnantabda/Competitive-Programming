username = input()
sum_ = 0
track = []
for i in username:
    if i not in track:
        sum_ +=1
        track.append(i)

if sum_ % 2 == 0 :
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")