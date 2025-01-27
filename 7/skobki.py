def F(length, combination, left, right,combinations = []):
    if len(combination) == 2*length:
        combinations.append(combination)
        return
    if left < length:
        F(length, combination + '(', left + 1, right)
    if right < left:
        F(length, combination + ')', left, right + 1)
    return combinations


print(F(int(input('кол-во пар скобок ')), '', 0, 0))