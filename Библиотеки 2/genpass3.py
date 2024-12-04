from random import choice

def generate_password(m):
    letters_lower, letter_upper, nums = 'abcdefghjkmnpqrstuvwxyz', 'ABCDEFGHJKMNPQRSTUVWXYZ', '23456789'
    password, data = '', ''
    data += choice(list(letters_lower)) + choice(list(letter_upper)) + choice(list(nums))
    password += data
    while len(password) < m: password+=choice(list(letters_lower + letter_upper + nums))
    return password

def main(n, m):
    res = []
    while len(res) < n:
        pas = generate_password(m)
        while pas in res: pas = generate_password(m)
        res.append(pas)
    return res
