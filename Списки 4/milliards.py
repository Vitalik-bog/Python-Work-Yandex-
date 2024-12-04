out = []
newspapers = [i for i in input().split(';')]
accounts = [i.split(',') for i in newspapers]
out = []
[out.append([]) for i in range(len(newspapers))]
for i in range(len(accounts)):
    [out[i].append(accounts[i][j]) for j in range(len(accounts[i])) if int(accounts[i][j]) >= 1000000000]
[accounts[i].append('') for i in range(len(accounts)) if not accounts[i]]
[print(",".join(account)) for account in out]