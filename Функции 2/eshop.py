items = []
receipt = 0
def addItem(itemName, itemCost):
    items.append([itemName, itemCost])
    
def printReceipt():
    global items, receipt
    if len(items) > 0:
        receipt += 1
        print('Чек ', receipt, '. Всего предметов: ', len(items), sep='')
        price = 0
        for product in items:
            print(product[0], '-', product[1])
            price += product[1]
        print('Итого:', price)
        print('-----')
        items = []
