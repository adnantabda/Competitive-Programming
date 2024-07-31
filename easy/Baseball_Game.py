def cal_points(operations):
    records = []
    for i in operations:
        if records and i == "+":
            first_top = records[-1]
            second_top = records[-2]

            value = first_top + second_top
            records.append(value)
            print(records)
        elif records and i == "D":
            top = records[-1]
            print(records[-1])
            records.append(top * 2)
            print(records)
        elif records and i == "C":
            records.pop()
            print(records)

        else:
            records.append(int(i))
            print(records)

    return sum(records)


print(cal_points(["5","2","C","D","+"]))



