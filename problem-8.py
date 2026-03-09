def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    result = ''.join(l)
    print(result)

    return

st = 'abcd'
ch = 'r'
mutate_string(st,2,ch)