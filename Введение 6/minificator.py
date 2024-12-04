import re

count = int(input())
line, temp = '', ''
for i in range(count):
    line = input()
    if re.search(r'\s+$', line):
        line = re.sub(r'\s+$', '', line)
    if re.search(r'\S+\s+.*$', line):
        if not re.search(r'^.*\'.*\s+', line):
            if re.search(r'^\s+', line):
                temp = re.match(r'\s+', line).group(0)
            line = line[len(temp):]
            line = re.sub(r'\s+', ' ', line)
            line = temp+line
        else:
            quotes = []
            for i in range(len(line)):
                if (line[i] == "'" and line[i-1] != "\\") or (line[i] == "'" and line[i-1] == "\\" and line[i-2] == "\\"):
                    if len(quotes) < 2:
                        quotes.append(i)
            quotes_part = line[quotes[0]:quotes[1]+1]
            if re.match(r'\s+', line):
                temp = re.match(r'\s+', line).group(0)
            else:
                temp = ''
            before_quote = re.sub(r'\s+', ' ', line[:quotes[0]])
            after_quote = re.sub(r'\s+', ' ', line[quotes[1]+1:])
            if re.search(r'#.*$', after_quote):
                after_quote = re.sub(r'#.*$', '', after_quote)
            line = temp[1:] + before_quote + quotes_part + after_quote
        if re.search(r'^\s*#', line):
            line = ''
        if re.search(r'.+#.*$', line):
            if not re.search(r".*'.*#.*'.*$", line):
                line = re.sub(r'#.*$', '', line)
                line = re.sub(r'\s+$', ' ', line)
    print(line)
        