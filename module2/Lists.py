if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6]
    print("l1 = ", l1, type(l1))
    print("len(l1) =", len(l1))
    print("l1[0] =", l1[0])
    print("l1[1] =", l1[1])
    print("l1[-1] =", l1[-1])
    print("l1[-2] =", l1[-2])
    print("l1[0:3] =", l1[0:3])
    print()

    l2 = ['a string', 2, 3.14]
    print("l2 =", l2, type(l2))
    print("len(l2) =", len(l2))
    print("l2[0] =", l2[0])
    print("l2[1] =", l2[1])
    print("l2[-1] =", l2[-1])
    print("l2[-2] =", l2[-2])
    print("l2[1:3] =", l2[1:3])
    l2[0] = 'another string'  # not immutable, working
    print("l2 =", l2, type(l2))
    print()

    l3 = [9, 5, 4, 2, 7, -1]
    l3sorted = sorted(l3)
    print("l3 =", l3, type(l3))
    print("sorted(l3)", l3sorted, type(l3sorted))
    print()

    l4 = [["s00", "s01"], ["s10", "s11", ["s120", "s121"]], "s3", ("s41", "s42")]
    print("l4 =", l4)
    print("l4[0][0] =", l4[0][0])
    print("l4[2] =", l4[2])
    # print("l4[0][0] =", l4[0][2]) # error
    print("l4[2][0] =", l4[2][0])  # ok because string
    print("l4[2][1] =", l4[2][1])  # ok because string
    print()

    print("('pop', 'rock')[0] =", ('pop', 'rock')[0])
    print("('pop', 'rock')[1] =", ('pop', 'rock')[1])
    print("('pop', 'rock')[1][1:4:2] =", ('pop', 'rock')[1][1:4:2])

    l5 = ["s0", "s1", "s2"]
    l5d = l5
    l5c = l5[:]
    l5c2 = list(l5)
    print("l5 =", l5)
    l5.extend(["s3", "s4"])
    print("l5 extended =", l5)
    l5.append(["s50", "s51"])
    print("l5 apended =", l5)
    l5[0] = "new s0"
    l5[5][0] = "new s50"
    print("l5 modified =", l5)
    print("l5d =", l5d)
    del (l5[3])
    print("l5 after delete =", l5)
    print("l5d =", l5d)
    del (l5[0:2])
    print("l5 after another delete =", l5)
    print("you can't remove an object that does not exist in the list")
    # del (l5[9])
    print("l5d =", l5d)
    print("l5c =", l5c)
    print("l5c2 =", l5c2)
    print()

    s1 = "This is a string; it should be converted to a list."
    print("s1 =", s1)
    l6 = s1.split()
    print("l6 split form s1 =", l6)
    print()

    s2 = "A, B, C, D"
    print("s2 =", s2)
    l7 = s2.split(", ")
    l8 = s2.split(",")
    print("l7 split by ', ' from s2 =", l7)
    print("l8 split by ',' from s2 =", l8)

    l91 = [1, 2, 3]
    l92 = [4, 5]
    l9 = l91 + l92
    print("l9 =", l9)
    print("l91 =", l91)
    print("l92 =", l92)
    print()

    l10 = [1, 2, 2, 3, 3, 3, 4]
    print("l10 =", l10)
    del (l10[2])
    print("l10 after deletion of second element =", l10)
    print("2 in l10 0", 2 in l10)
    print("3 in l10 0", 3 in l10)
    print("9 in l10 0", 9 in l10)

