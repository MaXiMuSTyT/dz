def paths(a, b, st, col):
    if st >= a or col >= b:
        return 0
    if st == a - 1 and col == b - 1:
        return 1
    return paths(a, b, st + 1, col) +paths(a, b, st, col + 1)




print(paths(int(input('длина ')),int(input('ширина ')),0,0))