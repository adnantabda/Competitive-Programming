opstack = []
output = []
input_ = "A + B * C"
input_list = input_.split(" ")
for i in input_list:
    if i in "1234567890":
        output.append(i)

    if i == "(":
        opstack.append(i)

    if i == ")":
        opstack.pop()

    if i == "+-/*":
        opstack.append(i)


