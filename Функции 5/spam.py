def mail(name, date, email, address='Пенза'):
    print('To: ', email)
    print('Здравствуйте,', name, '!')
    print('Были бы рады видеть вас на встрече начинающих программистов в', address+',', 'которая пройдет', date+'.')
mail('Павел', '01.01.2019', 'pavel@mail.ru', 'Яндекс')
mail('Кирилл', '04.09.2018', 'kiril@mail.ru')