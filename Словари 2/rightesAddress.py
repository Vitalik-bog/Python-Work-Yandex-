def ActionFolderFile(valids, address):
    ok = False
    if address in valids: ok = True
    temp = []
    for data in address.split('/'):
        temp.append(data)
        if '/'.join(temp)+'/' in valids or '/'.join(temp) in valids: ok = True; break
    if ok: return 'YES'
    else: return 'NO'
valid, results = [input() for _ in range(int(input()))], []
[results.append(ActionFolderFile(valid, input())) for _ in range(int(input()))]
[print(res) for res in results]