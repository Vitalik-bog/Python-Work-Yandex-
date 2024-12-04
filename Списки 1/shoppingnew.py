count = int(input())
products = []
products_count = []
for i in range(count):
    products.append(input())
    products_count.append(int(input()))
for j in range(len(products)-1, -1, -1):
    print(products[j], products_count[j])