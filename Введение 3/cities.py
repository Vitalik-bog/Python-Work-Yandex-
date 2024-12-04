city_1 = input()
city_2 = input()

while(city_2[0] == city_1[-1]):
    city_1 = city_2
    city_2 = input()    
print(city_2)
    