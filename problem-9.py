def count_substring(string, sub_string):
    l_str = len(string)
    s_sstr = len(sub_string)
    count = 0
    for x in range(l_str):
        if string[x:x+s_sstr] == sub_string:
            count += 1
    return count

print(count_substring('marufmaruf','mar'))