def countFood(days):
    global dailyFood 
    out = 0
    for i in days:
        out += dailyFood[i-1]
    print(out)
    