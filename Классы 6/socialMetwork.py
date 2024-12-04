class User:
    
    def __init__(self, name):
        
        self.name = name
        
    def send_message(self, user, message):
        return
    
    def post(self, message):
        return
    
    def info(self):
        return ""
    
    def describe(self):
        print(info())
        
        
class Person(User):
    
    def __init__(self, name, birthday):
        
        self.name = name
        self.birthday = birthday
        
    def info(self):
        return "Дата рождения: {}".format(self.birthday)
    
    
    def subscribe(self, user):
        return
    
class Community(User):
    
    def __init__(self, name, description):
        
        self.name = name
        self.description = description
        
    def info(self):
        return  "Описание: {}".format(self.description)