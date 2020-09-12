def sum_calc(value_list):
    result = 0

    for i in value_list:
        result += i
    return result


def sqrt_calc(value):
    return value ** 2


def multi_calc(value_list):
    result = 1

    for value in value_list:
        result *= value

    return result