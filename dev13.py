def filter_last_digit(num_list):
    integer = 0
    for i in num_list:
        integer += i%10
    return integer
print(filter_last_digit([23, 67, 100]))
