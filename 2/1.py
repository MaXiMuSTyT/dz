def lengthofs(s):
    hset = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in hset:
            hset.remove(s[left])
            left += 1
        hset.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

s = input("Введите строку: ")
print(lengthofs(s))