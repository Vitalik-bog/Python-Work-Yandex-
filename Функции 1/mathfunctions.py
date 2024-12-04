def line(s, t):
   data = [float(i) for i in t.split(';')]
   s = [float(i) for i in s.split('x')]
   print(data[1] == s[0]*data[0] + s[1])