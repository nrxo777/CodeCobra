def sum_all(*args):
    arguments = sum(args)
    # ********** Also can use as: **********
    # for i in args:
    #     print(i * 2)
    return arguments

print(sum_all(1,2,3,4,5))