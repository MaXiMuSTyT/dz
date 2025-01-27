s = input('строка ')
li = s.split()
def f(s,li):
    li.reverse()
    for i in range(len(li)):
        if i == 0:
            li[i] = li[i].capitalize()
        else:
            li[i] = li[i].lower()

    return li

print(' '.join(f(s,li)))