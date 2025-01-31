if __name__ == '__main__':
    d1 = {'int': 12, 'float': 3.141592, "boolean": True, 'string': 'my string', 'touple': (1, 5, 9), 'list': [2, 6, 4]}
    print("d1 =", d1)
    keys = d1.keys()
    values = d1.values()
    keys2 = list(d1.keys())
    values2 = list(d1.values())
    print("d1.keys =", keys, type(keys))
    print("d1.values =", values, type(d1.values))
    print("d1.keys2 =", keys2, type(keys))
    print("d1.values2 =", values2, type(d1.values))
    print("d1['int'] =", d1['int'])
    print("d1.get('int') =", d1.get('int'))
    print("d1['float'] =", d1['float'])
    print("d1.get('float') =", d1.get('float'))
    print("d1['boolean'] =", d1['boolean'])
    print("d1.get('boolean') =", d1.get('boolean'))
    print("d1['string'] =", d1['string'])
    print("d1.get('string') =", d1.get('string'))
    print("d1['touple'] =", d1['touple'])
    print("d1.get('touple') =", d1.get('touple'))
    print("d1['list'] =", d1['list'])
    print("d1.get('list') =", d1.get('list'))
    print("d1['something'] fails with error cause nothing does not exist")
    # print("d1['something'] =", d1['something'])
    print("d1.get('something') =", d1.get('something'))
    d1['something'] = 'new value'
    print("d1['something'] after add=", d1['something'])
    print("d1.get('something') =", d1.get('something'))
    print("d1.keys =", keys, type(keys))
    print("d1.values =", values, type(d1.values))
    print("d1.keys2 =", keys2, type(keys))
    print("d1.values2 =", values2, type(d1.values))
    del (d1['something'])
    print("d1.get('something') =", d1.get('something'))
    print("'something' in d1 =", 'something' in d1)
    print("'string' in d1 =", 'string' in d1)
    print("d1.keys =", keys, type(keys))
    print("d1.values =", values, type(d1.values))
    print("d1.keys2 =", keys2, type(keys))
    print("d1.values2 =", values2, type(d1.values))
    print()

    d2 = {(1, 2, 3): (4, 5, 6)}
    # d2fail = {(1, 2, 3): (4, 5, 6), [7, 8, 9]: [10, 11, 12]}  # list is unhashable[10, 11, 12]}
    print("d2 =", d2)
    print("d2.get((1,2,3)) =", d2.get((1, 2, 3)))
    print()

    release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                         "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                         "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                         "Saturday Night Fever": "1977", "Rumours": "1977"}
    print("release_year_dict =", release_year_dict)
    print("release_year_dict['Thriller'] =", release_year_dict['Thriller'])
    print("release_year_dict['The Bodyguard'] =", release_year_dict['The Bodyguard'])
    print("release_year_dict.keys() =", release_year_dict.keys())
    print("release_year_dict.values() =", release_year_dict.values())
    release_year_dict['Graduation'] = '2007'
    print("release_year_dict afeter add =", release_year_dict)
    del (release_year_dict['Thriller'])
    del (release_year_dict['Graduation'])
    print("release_year_dict after delete=", release_year_dict)
