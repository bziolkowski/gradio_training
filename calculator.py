def calc(text):
    operation_list =  text.split()
    arg1 = int(operation_list[0])
    arg2 = int(operation_list[2])
    operation = operation_list[1]

    if operation == "+":
        result = arg1 + arg2

    elif operation == "-":
        result = arg1 - arg2

    elif operation == "*":
        result = arg1 * arg2

    else:
        result = arg1 / arg2

    return result
