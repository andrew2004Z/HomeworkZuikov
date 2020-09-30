def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_reverse_code(x):
    ch = x
    if x > 0:
        n = ''
        while x > 0:
            y = f'{x % 2}'
            n = y + n
            x = int(x / 2)
        while ft_len(n) != 8:
            n = '0' + n
    else:
        x = x * -1
        n = ''
        while x > 0:
            y = f'{x % 2}'
            n = y + n
            x = int(x / 2)
        while ft_len(n) != 7:
            n = '0' + n
        n = '1' + n
    a = '1'
    if ch > 0:
        return n
    else:
        for i in n[1:]:
            if i == '0':
                a = a + '1'
            else:
                a = a + '0'
        return a