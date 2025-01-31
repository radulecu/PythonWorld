if __name__ == "__main__":
    r = range(3)
    print("r", "=", r, type(r))
    l = list(r)
    s = set(r)
    t = tuple(r)

    print("looping through range")
    for i in r:
        print(i)
    print()

    print("looping through list")
    for i in l:
        print(i)
    print()

    print("looping through set")
    for i in s:
        print(i)
    print()

    print("looping through tuple")
    for i in t:
        print(i)
    print()

    r = range(9, 13)
    print("r", "=", r, type(r))

    print("looping through range")
    for i in r:
        print(i)
    print()

    r = range(-2, 3)
    print("r", "=", r, type(r))

    print("looping through range")
    for i in r:
        print(i)
    print()

    print("range(15,10)", "=", range(15, 10))
    print("list(range(15, 10))", "=", list(range(15, 10)))
    print()

    colors = ["red", "green", "blue", "orange", "yellow"]
    print("colors", "=", colors)
    for i in range(len(colors)):
        colors[i] = "white"
    print("colors", "=", colors)
    print()

    colors = ["red", "green", "blue", "orange", "yellow"]
    print("colors", "=", colors)
    for i in range(len(colors)):
        del (colors[-1])
    print("colors", "=", colors)
    print()

    colors = ["red", "green", "blue", "orange", "yellow"]
    print("colors", "=", colors)
    print("enumerate(colors)", "=", enumerate(colors), type(enumerate(colors)))
    for i, color in enumerate(colors):
        print(i, "->", color)
    print("i is still visible outside the loop but may be undefined if input is empty", i)
    print()

    numbers = [1, 5, -2, 7, -99]
    i = 0
    while numbers[i] > 0:
        print("still a positive number", ":", numbers[i])
        last_number = i
        i += 1
    print("last_number visible outside loop but may get undefined if input is empty", last_number)
    print()

    even = []
    for i in range(10):
        if i % 2 == 1:
            continue
        even.append(i)
    print("even", "=", even)
    print()

    first_even = []
    for i in (2, 6, 4, 5, 8, 7):
        if i % 2 == 1:
            break
        first_even.append(i)
    print("first_even", "=", first_even)
    print()
