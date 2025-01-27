a = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]

def letters_length(x):
    dit = {}
    for i in x:
        key = (len(i), ''.join(sorted(i)))
        dit.setdefault(key, []).append(i)
    return list(dit.values())
print(letters_length(a))