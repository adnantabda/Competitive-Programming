n , k = map(int, input().split())
list_ = list(map(int, input().split()))

k -= 1
count = 0 
for i in list_:
    if i >= list_[k] and i >= 1:
        count += 1

print(count)