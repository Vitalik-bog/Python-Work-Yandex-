def eratosthenes(n):
    numbers = [i for i in range(2, n+1)]
    resend = ['']
    deleted = []
    p = numbers[0]
    while resend.count(resend[-1]) < len(numbers):
        for i in numbers:
            if i % p == 0 and i != p:
                deleted += [str(numbers.pop(numbers.index(i)))]
        for i in numbers:
            if i > p:
                p = i
                break
        resend += [p]
    print(' '.join(deleted))