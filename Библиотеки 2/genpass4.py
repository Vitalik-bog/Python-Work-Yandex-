from random import choice

def generate_password(m):
    letters_lower, letter_upper, nums = 'abcdefghijkmnpqrstuvwxyz', 'ABCDEFGHJKLMNPQRSTUVWXYZ', '23456789'
    symbols = letters_lower + letter_upper + nums
    password, data = '', ''
    data += choice(letters_lower) + choice(letter_upper) + choice(nums)
    password += data
    while len(password) < m:
        s = choice(symbols)
        while s in password: s = choice(symbols)
        password+=s
        symbols = symbols.replace(s, '')
    return password

def main(n, m):
    res = []
    while len(res) < n:
        pas = generate_password(m)
        res.append(pas)
    return res

