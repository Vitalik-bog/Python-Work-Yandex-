today = int(input())
yesterday = 0
buy = False
sell = False
day = 1
while today != 0:
    yesterday = today
    today = int(input())
    if today > yesterday and buy == False:
        buy = today
    if today < yesterday and buy != False and sell == False:
        sell = today
    yesterday = today
print(buy, sell, sell-buy)

