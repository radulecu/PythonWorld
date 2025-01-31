if __name__ == '__main__':
    a = 6
    print("a == 6 =", a == 6)
    print("a == 7 =", a == 7)
    print("a != 6 =", a != 6)
    print("a != 7 =", a != 7)
    print("a >= 5 =", a >= 5)
    print("a >= 7 =", a >= 7)
    print("a >= 6 =", a >= 6)
    print("a > 6 =", a > 6)

    if a == 6:
        print("a is 6")
    else:
        print("a is not 6")

    if (a == 7):
        print("a is 7")
    else:
        print("a is not 7")

    if a < 6:
        print("a is lower than 6")
    elif a > 6:
        print("a is greater than 6")
    else:
        print("a is 6")

    if a < 7:
        print("a is lower than 7")
    elif a > 7:
        print("a is greater than 7")
    else:
        print("a is 7")

    if a < 5:
        print("a is lower than 5")
    elif a > 5:
        print("a is greater than 5")
    else:
        print("a is 5")

    print("not True =", not True)
    print("not True =", not True)
    print("True or False =", True or False)
    print("True and False =", True and False)

    print("'str'=='str' =", 'str' == 'str')
    print("'str'=='string' =", 'str' == 'string')
    print("'B' > 'A' =", 'B' > 'A')
    print("'BA' > 'AB' =", 'BA' > 'AB')

    print("5 == None", "=", 5 == None)
    print("None == None", "=", None == None)
