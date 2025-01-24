file = open('inf.txt', 'r+')
inf = file.readline()

N = int(inf[0])
res = int(inf[-1])
spi = inf[1:-1].split()
spi = [int(i) for i in spi]

def per(ind=0, done = 0,var = '',amount = N,result = res):
    '''Функция расстановки + и -'''
    if ind == amount:
        if done == result:
            return var
        return None
    m = per( ind+1, done - spi[ind],var + '-'+ str(spi[ind]),amount = N, result = res)
    if m:
        return m
    sl = per( ind+1, done + spi[ind],var + '+'+ str(spi[ind]),amount = N, result = res)
    if sl:
        return sl
    return None

file.write(' '+per())
file.close()
