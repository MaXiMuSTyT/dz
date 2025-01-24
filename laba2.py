file = open('input.txt', 'r+')
a = file.readline()
output = open('output.txt','w')
output.truncate(0)
def inf(a):
    '''Вспомогательная функция для преобразовния информации'''
    s = a.split()
    d = [int(i) for i in s]
    return d

stars_cor = []
solutions = []
placed_positions = []
coordinates = []
inf = inf(a)
N = inf[0]
L = inf[1]
K = inf[-1]
field = [['0'] * N for i in range(N)]
b = 0

for i in range(K):
    p = file.readline().split()
    coordinates = [int(i) for i in p]
    x = coordinates[1]
    y = coordinates[0]
    field[x][y] = '#'
    placed_positions.append((x, y))


def is_under_attack(field, x, y ,N):
    '''Функция проверки точки на поле'''
    king_horse = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    for movex, movey in king_horse:
        if (x + movex) >= 0 and (x + movex) < N and (y + movey) >= 0 and (y + movey) < N and field[x + movex][y + movey] == '#' :
                return True

    return False

def place_stars(field,N):
    '''Функция расстановки * на поле'''
    king_horse = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    for x,y in placed_positions:
        for movex, movey in king_horse:
            if (x + movex) >= 0 and (x + movex) < N and (y + movey) >= 0 and (y + movey) < N  :
                field[x + movex][y + movey] = '*'
                stars_cor.append((x+movex,y+movey))
    return

def stars_delete(field):
    '''Функция удаления * на поле'''
    for x,y in stars_cor:
        field[y][x] = 0
    stars_cor.clear()
    return


def place_figures(field, placed, L, solutions, N,m, l):
    '''Функция расстановки фигур на поле и нахождения всех решений'''
    if placed == L:
        solutions.append(placed_positions.copy())
        return
    for x in range(m,N):
        for y in range(l if x == m else 0, N):
            if field[x][y] == '0' and not is_under_attack(field, x, y, N):
                field[x][y] = '#'
                placed_positions.append((x, y))
                # place_stars(field,N)
                # # for row in field:
                # #     print(*row, sep=', ')
                # stars_delete(field)
                place_figures(field, placed + 1, L, solutions, N,x,y)
                field[x][y] = '0'
                placed_positions.pop()
            l = 0


place_figures(field, b, L, solutions, N,0,0)


for i in solutions:
    output.write(str(i) + '\n')
place_stars(field,N)
# вывод поля
for row in field:
    print(*row,sep =', ')
print('кол-во решений:',len(solutions))

file.close()
output.close()


