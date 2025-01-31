import re

if __name__ == '__main__':
    name = "Michael Jackson"
    name2 = 'Ghita Cartita'
    print("name =", name)
    print("name2 =", name2)
    print("name[0] =", name[0])
    print("name[1] =", name[1])
    print("name[2] =", name[2])
    print("name[-0] =", name[-0])
    print("name[-1] =", name[-1])
    print("name[-2] =", name[-2])
    print("name[0:2] =", name[0:2])
    print("name[0:4] + name[8:12] =", name[0:4] + name[8:12])
    print("name[2:7] =", name[2:7])
    print("name[0:7] =", name[0:7])
    print("name[::2] =", name[::2])
    print("name[0:7:2] =", name[0:7:2])

    print("len(name)", len(name))

    print(name + " is the best!")
    print("3 * s1", 3 * name)
    statement = name
    statement = statement + " is the best!"
    print("statement =", statement)

    # name[0] = 2 # Not allowed, immutable

    print(r"Michael Jackson \n is the best! ->", "Michael Jackson \n is the best!")
    print(r"Michael Jackson \t is the best! ->", "Michael Jackson \t is the best!")
    print(r"Michael Jackson \\n is the best! ->", "Michael Jackson \\n is the best!")

    print("statement.upper() =", statement.upper())
    print("statement.lower() =", statement.lower())
    print("statement.replace('Michael', 'Janet') =", statement.replace('Michael', 'Janet'))
    print("statement.find('el') =", statement.find('el'))
    print("statement.find('El') =", statement.find('El'))
    print("statement.find('Jackson') =", statement.find('Jackson'))
    print("statement.split() =", statement.split())

    print("re.search('Jac.son') =", re.search('Jac.son', name))

    phone = "1234567890"
    phones = "1234567890, 5678901234, 256 8901234567"
    text = "Hello World!"
    print(r"re.findall(r'\d{10}', phone) =", re.findall(r'\d{10}', phone))
    print(r"re.findall(r'\d{10}', phones) =", re.findall(r'\d{10}', phones))

    print(r"re.findall(r'\bcat\b','This is my cat.') =", re.findall(r'\bcat\b', 'This is my cat.'))
    print(r"re.findall(r'\bat\b', 'This is my cat.') =", re.findall(r'\bat\b', 'This is my cat.'))
    print(r"re.findall(r'\Ba\B', 'This is my cat.')') =", re.findall(r'\Ba\B', 'This is my cat.'))

    print(r"re.split(' ', statement) =", re.split(' ', statement))
    print(r"re.split(r'\s', statement) =", re.split(r'\s', statement))

    print(r"re.sub('best', 'king of pop', statement) =", re.sub('best', 'king of pop', statement))
    print(r"re.sub('BEST', 'king of pop', statement, flags=re.IGNORECASE) =",
          re.sub('BEST', 'king of pop', statement, flags=re.IGNORECASE))

    q = "This is the first line \n\
    This is the second line \n\
    This is the third line"
    print("Multi line string: ", q)

    print("re.findall('cat','My cat is looking for its cat friend') =",
          re.findall('cat', 'My cat is looking for its cat friend.'))

    print("re.sub('cat','dog', 'My cat is looking for its cat friend') =",
          re.sub('cat', 'dog', 'My cat is looking for its cat friend.'))

    print("hello Mike".find("Mike")
          )
