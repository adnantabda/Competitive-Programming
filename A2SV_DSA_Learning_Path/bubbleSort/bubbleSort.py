def bubble_sort(list):

    for pass_num in range(0 , len(list)):
        for i in range(pass_num):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1] , list[i]



list = [54,26 , 93, 17 , 77, 31 , 44, 55, 20]
bubble_sort(list)
print(list)