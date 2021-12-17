def func(a, b, *args):
    print(args)
    return a + b


def kwfunc(a, b, **kwargs):
    print(kwargs)
    return a + b


def func3(a, b):
    print(a ** 2, b ** 2)


def func4(a=1, b=2):
    print(a ** 2, b ** 2)


if __name__ == '__main__':
    a = [1, 2]
    func3(*a)

    d = {
        'a': 3,
        'b': 4,
    }
    func4(**d)

    # n, m = func(1, 2)
    # print(n)
    # print(m)

    # a, b, c = [1, 2, 3]

    # a = [1, 2, 3]
    # b = [4, 5, 6]
    # t = (a, b)
    # print(t)
    # t[0][0] = -1
    # print(t)
    

    # l = [1, 2, 3, 4]
    # l.append(5)
    # l.insert(1, 123)
    # print(l)
    # print(l[0])
    # print('>>> ', l[::-1])

    # s = {1, 2, 3, 4}
    # s.add(6)
    # s.remove(3)
    # print(s)

    # d = {'a': 1, 'b': 2, 'c': 3}
    # d['d'] = 4
    # del d['b']
    # print(d)

    # t = (1, 2, "qwe")
    # print(t)

    # a = [1, 2, 3]
    # b = [a[:], a[:], a[:]]
    # b[0][2] = 333
    # print(b)

    # print(None)
    # print(type(None))
