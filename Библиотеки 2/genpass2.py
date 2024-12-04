from random import choice
symbols = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789'

def generate_password(m):
    password = ''
    while len(password) < m:
        s = choice(list(symbols))
        while s in password: s = choice(list(symbols))
        password+=s
    return password

def main(n, m):
    res = []
    while len(res) < n:
        pas = generate_password(m)
        while pas in res: pas = generate_password(m)
        res.append(pas)
    return res
