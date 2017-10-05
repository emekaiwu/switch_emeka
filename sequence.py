def fib(start,count):
    fib_list = []
    for index in range(count):
        if index== 0:
            fib_list.append(start)
        elif index == 1:
            fib_list.append(start)
        else:
            fib_list.append(fib_list[index-1] + fib_list[index-2])
    return fib_list
print(fib(4,20))
