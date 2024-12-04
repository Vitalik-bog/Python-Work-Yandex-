class Message:
    
    messages = {
        5 : "Доклад уже существует!",
        50 : "Конфликт во времени с другим докладом!",
        404 : "Доклад не найден",
        1 : "Доклад успешно добавлен!",
        10 : "Доклад успешно удалён!",
        
    }
        
    def create(code):
        print()
        print("-"*32)
        print(Message.messages[code])
        print("-"*32)
        print()
    
    

class Conference:
    
    def __init__(self, name):
        
        self.name = name
        self.reports = {}
        
    def __iadd__(self, obj):
        
        def isIntersectionTime(self, newobj):
            for obj in self.reports.values():
                if set(range(obj.initTime(), obj.initTime(withlong=True))).intersection(set(range(newobj.initTime(), newobj.initTime(withlong=True)))): return True
            return False
        
        if obj.name in self.reports: Message.create(5); return self
        if isIntersectionTime(self, obj): Message.create(50);  return self
        
        self.reports[obj.name] = obj
        Message.create(1)
        return self
    
    def __isub__(self, name):
        if name in self.reports: 
            del self.reports[name]
            Message.create(10)
        else: Message.create(404)
        return self
        
    
    def __call__(self):
        self.printRow("Все доклады", sorted(self.reports.values(), key=lambda report: report.initTime()))
            
    def printRow(self, title, data):
        print(title)
        print("-"*32)
        for report in data:
            print(report.time_start, report.name, report.time, sep=" | ")
            print("-"*32)
            
    def theLongest(self):
        self.printRow("Самый продолжительный доклад", [sorted(self.reports.values(), key=lambda report: -report.time)[0]])
            
        
class Report:
    
    def __init__(self, name, time_start, time):
        
        self.name = name
        self.time_start = time_start
        self.time = int(time)
        
    def initTime(self, withlong=False):
        time = [int(i) for i in self.time_start.split(":")]
        return time[0]*60 + time[1] if not withlong else time[0]*60 + time[1] + self.time
    
class Inteface:
    
    def __init__(self):
        
        self.system = Conference(input("Название конференции: "))
        
    def addReport(self, name, time_start, time):
        self.system += Report(name, time_start, time)
        
    def delReport(self, name):
        self.system -= name
        
    def statistic(self):
        self.system.theLongest()
        
    def actions(self):
        print("Добро пожаловать на конференцию '{}'".format(self.system.name))
        while True:
            print("1. Все доклады")
            print("2. Создать доклад")
            print("3. Удалить доклад")
            print("4. Статистика")
            print("5. Выход")
            action = int(input())
            if action == 1 and self.system: self.system()
            elif action == 2: self.addReport(input("Имя доклада: "), input("Время старта <чч:мм>: "), input("Продолжительность: <м> "))
            elif action == 3: self.delReport(input("Имя доклада: "))
            elif action == 4: self.statistic()
            elif action == 5: return
        
user = Inteface().actions()