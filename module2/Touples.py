if __name__ == '__main__':
    t1 = (1, 2, 3, 4, 5, 6)
    print("t1 = ", t1, type(t1))
    print("len(t1) =", len(t1))
    print("t1[0] =", t1[0])
    print("t1[1] =", t1[1])
    print("t1[-1] =", t1[-1])
    print("t1[-2] =", t1[-2])
    print("t1[0:3] =", t1[0:3])
    print()

    t2 = ('a string', 2, 3.14)
    print("t2 =", t2, type(t2))
    print("len(t2) =", len(t2))
    print("t2[0] =", t2[0])
    print("t2[1] =", t2[1])
    print("t2[-1] =", t2[-1])
    print("t2[-2] =", t2[-2])
    print("t2[1:3] =", t2[1:3])
    # t2[0] = 'another string'  # immutable, not working
    print()

    t3 = (9, 5, 4, 2, 7, -1)
    t3sorted = sorted(t3)
    print("t3 =", t3, type(t3))
    print("sorted(t3)", t3sorted, type(t3sorted))
    print()

    t4 = (("s00", "s01"), ("s10", "s11", ("s120", "s121")), "s3")
    print("t4 =", t4)
    print("t4[0][0] =", t4[0][0])
    print("t4[2] =", t4[2])
    # print("t4[0][0] =", t4[0][2]) # error
    print("t4[2][0] =", t4[2][0])  # ok because string
    print("t4[2][1] =", t4[2][1])  # ok because string
    print()

    print("('pop', 'rock')[0] =", ('pop', 'rock')[0])
    print("('pop', 'rock')[1] =", ('pop', 'rock')[1])
    print("('pop', 'rock')[1][1:4:2] =", ('pop', 'rock')[1][1:4:2])

    t51 = (1, 2, 3)
    t52 = (4, 5)
    t5 = t51 + t52
    print("t5 =", t5)
