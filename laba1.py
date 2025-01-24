file = open('inf.txt','r+')
inf = file.readline()


spi = inf.split()
spi = [int(i) for i in spi]
N = spi[0]
res = spi[-1]
spi = spi[1:-1]
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

if per() == None:
    file.write(' '+ 'No solutions')
else:
    file.write(' '+per())
file.close()
