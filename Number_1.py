stroki = []
with open('input.txt', 'r') as file:
    for i in file:
        stroki.append(i)


def digit(file):
    d = []
    for i in file:
        a = []
        for j in i:
            if j.isdigit():
                a.append(j)
        if len(a) > 1:
            d.append(int(''.join(a[:len(a):len(a) - 1])))
        else:
            for i in a:
                d.append(int(i * 2))

    return sum(d)


print(digit(stroki))
