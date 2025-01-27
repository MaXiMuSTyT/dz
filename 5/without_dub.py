N = int(input('кол-во элементов '))
f = [input(str(i +1)+' ') for i in range(N)]
def uniq(smth):
    uniq_smth = list(set(smth))
    subsets = []

    def add(start, h):
        if h:
            subsets.append(set(h))

        for i in range(start, len(uniq_smth)):
            add(i + 1, h + [uniq_smth[i]])

    add(0, [])
    return subsets

print('Подмножества для' ,str(f) +':',uniq(f),"\n" + 'кол-во подмножеств:', len(uniq(f)))