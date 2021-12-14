# mahmoud G Batran
def swap_case(s):
    m = []
    for string in s:
        if string.isupper():
            m.append(string.lower())
        else:
            m.append(string.upper())
        r = "".join(m)

    return r


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


