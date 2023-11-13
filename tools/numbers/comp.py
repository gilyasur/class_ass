def sumofdigits(num):
    str_number = str(num)
    digit_sum = 0
    for digit_str in str_number:
        digit_sum += int(digit_str)
    return digit_sum

def ispal(num):

    num_str = str(num)
    

    return num_str == num_str[::-1]

