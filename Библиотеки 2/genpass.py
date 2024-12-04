from random import choice
symbols = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789'

def generate_password(m):
    password = ''
    while len(password) < m: password+=choice(list(symbols))
    return password

def main(n, m):
    res = []
    while len(res) < n:
        pas = generate_password(m)
        while pas in res: pas = generate_password(m)
        res.append(pas)
    return res
