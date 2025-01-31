if __name__ == '__main__':
    l1 = {1, 2, 3, 4, 5, 6, 2, 3, 6}
    s1 = set(l1)
    print("s1 = ", s1, type(s1))
    print("len(s1) =", len(s1))
    print("1 in s1 =", 1 in s1)
    print("5 in s1 =", 5 in s1)
    print("9 in s1 =", 9 in s1)
    print()

    s2 = {'a string', 2, 3.14}
    print("s2 =", s2, type(s2))
    print()

    s3 = {9, 5, 4, 2, 7, -1}
    print("s3 =", s3, type(s3))
    print()

    print("elements in a set must be hashable while a set is not")
    # s4 = {{"s00", "s01"}, {"s10", "s11", {"s120", "s121"}}, "s3", ("s41", "s42")}
    print("elements in a set must be hashable while a map is not")
    # s4 = {("s00", "s01"), {"s10": "v10", "s11": "v11"}, "s3", ("s41", "s42")}
    s4 = {("s00", "s01"), "s3", ("s41", "s42")}
    print("s4 =", s4)
    print()

    s5 = {"s0", "s1", "s2"}
    s5d = s5
    s5c = set(s5)
    print("s5 =", s5)
    print("set has no extend and mo append methods")
    # s5.extend(["s3", "s4"])
    # print("s5 extended =", s5)
    # s5.append(["s50", "s51"])
    # print("s5 appended =", s5)
    s5.add("s3")
    s5.add("s3")
    print("s5 after add =", s5)
    print("s5d =", s5d)
    print("s5c =", s5c)
    s5.remove("s2")
    print("s5 after delete =", s5)
    print("s5d =", s5d)
    print("s5c =", s5c)
    s5d.remove("s0")
    print("s5 after another delete =", s5)
    print("removing an object that is not in a set will throw an error")
    # s5d.remove("something that never existed")
    print("s5d =", s5d)
    print("s5c =", s5c)
    print()

    s61 = {1, 2, 3, 4, 5, 6, 7, 8}
    s62 = {2, 4, 6, 8, 10, 12}
    s63 = {1, 2, 3}
    print("s61 =", s61)
    print("s62 =", s62)
    print("s63 =", s63)
    print("s61 & s62 =", s61 & s62)
    print("s61.intersection(s62) =", s61.intersection(s62))
    print("s61 | s62 =", s61 | s62)
    print("s61.union(s62) =", s61.union(s62))
    print("s61.difference(s62) =", s61.difference(s62))
    print("s62.difference(s61) =", s62.difference(s61))
    print("s62.issubset(s61) =", s62.issubset(s61))
    print("s61.issuperset(s62) =", s61.issuperset(s62))
    print("s61.issuperset(s63) =", s61.issuperset(s63))

    l7 = [1, 2, 2, 1]
    s7 = {1, 2, 2, 1}
    print("the sum of l7 is:", sum(l7))
    print("the sum of s7 is:", sum(s7))

    s91 = {1, 2, 3}
    s92 = {4, 5}
    print("sets cannot be concatenated")
    # s9 = s91 + s92 # TypeError: unsupported operand type(s) for +: 'set' and 'set'
