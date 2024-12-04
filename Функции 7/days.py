import itertools
year_leap,  year_usually, day = (31,29,31,30,31,30,31,31,30,31,30,31), (31,28,31,30,31,30,31,31,30,31,30,31), int(input())-1
days_leap, days_usually = [], []

for i in range(len(year_leap)):    days_leap = itertools.chain(days_leap, itertools.product(range(1, year_leap[i] + 1), [i + 1]))
for i in range(len(year_usually)): days_usually = itertools.chain(days_usually, itertools.product(range(1, year_usually[i] + 1), [i + 1]))

days_leap, days_usually = list(days_leap), list(days_usually)
days = [str(d) for d in list(itertools.islice(itertools.cycle(itertools.chain(days_leap, days_usually, days_usually, days_usually)), 6000))]
time = [days[day], days[999], days[1999], days[2999], days[3999], days[4999]]
time = [''.join(list(number)) for number in time]
[print(t[1:-1].replace(',', '')) for t in time]