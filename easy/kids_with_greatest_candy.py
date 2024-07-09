def kids_with_greatest_candy(arr, extra):
    greatest_candy = max(arr)
    result = []

    for i in arr:
        if i + extra >= greatest_candy:
            result.append(True)
        else:
            result.append(False)

    return result


arr = [4,2,1,1,2]
extra = 1
print(kids_with_greatest_candy(arr, extra))
