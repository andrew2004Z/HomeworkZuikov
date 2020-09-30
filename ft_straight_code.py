def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_straight_code(x):
    if x > 0:
        n = ''
        while x > 0:
            y = f'{x % 2}'
            n = y + n
            x = int(x / 2)
        while ft_len(n) != 8:
            n = '0' + n
        return n
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
        return n