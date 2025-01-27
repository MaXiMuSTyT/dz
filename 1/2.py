num = input()
def f(num):
    if ((int(num) < 0) and (int(num) >= -128)) and (int('-' + num[-1] + num[1:-1]) >= -128):
        if len(num) == 4:
            if (num[-1] == '0') and (num[2] == '0'):
                print('-' + num[1])
            else:
                print('-' + num[-1] + num[2] + num[1])
        else:
            if num[-1] == '0':
                print('-' + num[1:-1])
            else:
                print('-' + num[-1] + num[1:-1])
    elif ((int(num) > 0) and (int(num) <= 128)) and (int(num[-1] + num[:-1]) <= 128):
        if len(num) == 3:
            if (num[-1] == '0') and (num[1] == '0'):
                print(num[0])
        else:
            if len(num) == 2:
                if num[1] == '0':
                    print(num[0])
                else:
                    print(num[-1] + num[:-1])
    else:
        print('No solution')

f(num)