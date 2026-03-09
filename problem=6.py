def split_and_join(line):

    l = len(line)
    new_str = ''
    for x in range(l):
        if line[x] == ' ':
            new_str += '-'
        else:
            new_str += line[x]
    print(new_str)


s = 'a r t'
split_and_join(s)


