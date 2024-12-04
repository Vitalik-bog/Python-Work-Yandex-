url = input().split('/').pop().split('?').pop().split('&')
key = input()
for uri in url:
    if key in uri:
        res = uri.split('=')
        if res[0] == key:
            print(res[1])
        else:
            print(res[0])