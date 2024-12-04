allprice = 0;
while(True):
    price = float(input())
    if price > 0:
        if price > 1000:
            allprice += price - (price * 0.05)
        else:
            allprice += price
    else:
        print(allprice)
        break;