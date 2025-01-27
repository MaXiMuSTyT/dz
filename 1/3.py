def zigzag(s, amountofrows):
    if amountofrows == 1 or amountofrows >= len(s):
        return s

    rows = [''] * amountofrows
    ind = 0
    step = 1

    for i in s:
        rows[ind] += i
        if ind == 0:
            step = 1
        elif ind == amountofrows - 1:
            step = -1
        ind += step

    return ''.join(rows)


print(zigzag(input('строка '), int(input('кол-во строк '))))
