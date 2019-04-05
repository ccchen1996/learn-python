def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数应该都是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is the maximun.')
    else:
        print(y, 'is the maximun.')

print_max(3, 5)
print(print_max.__doc__)
help(print_max)
