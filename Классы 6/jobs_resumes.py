class Profile:
    
    def __init__(self, profession):
        
        self.profession = profession
        
    def info(self):
        return ""
    
    def describe(self):
        print(self.info())
        
class Vacancy(Profile):
    
    def __init__(self, profession, money):
        
        self.profession = profession
        self.money = money
        
    def info(self):
        
        return "Предлагаемая зарплата: {}".format(self.money)
        
class Resume(Profile):
    
    def __init__(self, profession, time):
        
        self.profession = profession
        self.time = time
        
    def info(self):
        return "Стаж работы: {}".format(self.time)