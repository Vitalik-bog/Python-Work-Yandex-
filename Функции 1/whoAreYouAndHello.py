def whoAreYouAndHello():
    name = input()
    while ' ' in name or name[0].upper() != name[0] or name[1:].lower() != name[1:] or name.isalpha() == False:
        name = input()
    print('Привет,', name + '!')
            
            
        
        