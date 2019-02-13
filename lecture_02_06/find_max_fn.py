def find_max(things):
    m = things[0]

    for t in things:
        if t > m:
            m = t

    return m


def find_max_str_len(things):
    m = things[0]

    for t in things:
        if len(str(t)) > len(str(m)):
            m = t

    return m


def find_max_len(things):
    m = things[0]

    for t in things:
        if len(t) > len(m):
            m = t

    return m


if __name__ == '__main__':
    print(find_max([1, 3, 17, -104]))
    print(find_max_str_len([1, 3, 17, -104]))
    print(find_max_len([1, 3, 17, -104]))
    print(find_max_len([[1, 3, 17, -104], [], [1, 2, 3, 4, 5]]))
    print(find_max_len(['short', 'looooooooooong', 'short again']))


