n = int(input('количество банков: '))
inf = []
sums = []
for i in range(n):
    inf.append((input('название банка: '), int(input('сумма: ')), i+1))
def banks(h = 0):
    for name, summ, num in inf:
        for name_next, summ_next, num_next in inf:
            if abs(num - num_next) > 1:
                sums.append(((summ + summ_next), (name, num), (name_next, num_next)))
    for summa, first, second in sums:
        h = max(summa, h)
    for summa, first, second in sums:
        if summa == h:
            print([summa, first, second])
            break
        else:
            continue

banks()