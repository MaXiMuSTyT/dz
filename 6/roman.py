def roman(s):
    romannum = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    number = 0
    for i in range(len(s)):
        if i < len(s) - 1 and romannum[s[i]] < romannum[s[i + 1]]:
            number -= romannum[s[i]]
        else:
            number += romannum[s[i]]

    return number


print(roman(input('число, записанное римскими цифрами: ')))