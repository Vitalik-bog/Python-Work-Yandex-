count = int(input())
data = []
for i in range(count):
    advice = input()
    if 'не ' in advice[:3] or 'Не ' in advice[:3]:
        advice = advice[2:]
        while advice[0] == ' ':
            advice = advice[1:]
    data += [advice]
for ad in data:
    print(ad)