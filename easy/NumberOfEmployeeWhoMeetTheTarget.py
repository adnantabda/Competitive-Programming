def NumberOfEmployeeWhoMeetTheTarget(hours , target):
    count = 0
    hours.sort(reverse=True)
    for i in range(0 , len(hours)):
        if (hours[i]>= target):
            count = count + 1
        else:
            break
    return count


print(NumberOfEmployeeWhoMeetTheTarget([0,1,2,3,4] , 2))