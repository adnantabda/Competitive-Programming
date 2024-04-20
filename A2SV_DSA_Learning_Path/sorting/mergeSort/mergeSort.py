def merge_sort(a_list):
    
    if len(a_list) > 1:

        mid_value = len(a_list) // 2
        left_value = a_list[:mid_value]
        right_value = a_list[mid_value:]

        merge_sort(left_value)
        merge_sort(right_value)


        i = 0 
        j = 0 
        k = 0
        while i < len(left_value) and j < len(right_value):

            if left_value[i] < right_value[j]:
                a_list[k] = left_value[i]
                i +=1

            else:
                a_list[k] = right_value[j]
                j +=1

            k +=1

        while i < len(left_value):
            a_list[k] = left_value[i]
            i +=1
            k +=1

        while j < len(right_value):
            a_list[k] = right_value[j]
            j +=1
            k +=1

    return a_list


print(merge_sort([1,4,2,5,2,4,2,6,3,7,8]))
