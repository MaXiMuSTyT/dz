users = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]

def santa(users_list):
    dit = {}

    for user in users_list:
        name = user[0]
        if len(user) > 1:
            post = user[1]
        else:
            post = None
        dit[name] = post

    return dit


print(users)