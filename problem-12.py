def wrap(string, max_width):
    lenth = len(string)
    i = 0
    l = []
    while (i<lenth):
        l.append(string[i:i + max_width])
        i = i + max_width

    return '\n'.join(l)

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4))


