n = int(input())
parts = []
for i in range(n):
    parts.append(input())
count = int(input())
echo = []
for j in range(count):
    echo.append(int(input())-1)
for x in range(len(echo)):
    print(parts[echo[x]])