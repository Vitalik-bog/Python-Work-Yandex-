"""

MDL-почта разработана отъявленным негодяем, раздувающим маленькую задачку в большое приключение!

Функциональные возможности:

1. Регистрация пользователя.
2. Регистрация сервера (происходит автоматически в момент регистрации пользователя).
3. "Управляющий" серверами.
   а. Создание нового сервера.
   б. Получение одного из текущих серверов.
   в. Получение всех серверов.
4. "Управляющий" пользователями.
   а. Создание нового пользователя.
   б. Удаление существующего.
   в. Проверка существования пользователя.
6. Сам объект пользователя.
   а. Функция отправки письма.
   б. Функция получения входящих сообщений.
5. Интерфейс, возможности которого можно увидеть при запуске.
7. P.S. Возможно что-то забыл, писал это уже после реализации.

Copyright, Алексей Медведев, 2018. Запатентовано Весёловским комитетом.

"""



class Error:
    
    def __init__(self, code, message):
        self.code_errors = {1: "Error Server", 2:"Error User", 3:"Mail Error"}
        self.type = self.code_errors[code]
        self.message = message
        self.setSessionError()
        
    def setSessionError(self):
        print()
        print("-"*32)
        print("Внимание, возникла ошибка при работе с почтовым сервисом!")
        print("{}: {}".format(self.type, self.message))
        print("-"*32)        
        print()
        
class Message:
    
    def __init__(self, message):
        self.message = message
        self.setSessionMessage()
        
    def setSessionMessage(self):
        print("-"*32)
        print(self.message)
        print("-"*32, end="\n\n")

class AbstractServer:
    
    def __init__(self):
        self.servers = {}
        
    def getServers(self):
        return self.servers
    
    def add_server(self, server):
        if not server.name in self.servers: 
            self.servers[server.name] = server

            
    def get(self, name):
        if name in self.servers: return self.servers[name]
        else: 
            s = Server(name)
            self.add_server(s)
            return s
            
    def isset_server(self, server_name):
        return True if server_name in self.servers else False
    
system =  AbstractServer()
class Server(AbstractServer):
    
    def __init__(self, name):
        
        self.name = name
        self.users = {}
        system.add_server(self)
        
    def getUsers(self):
        return self.users    
        
    def add_user(self, user):
        if not user.name in self.users: 
            self.users[user.name] = user
            Message("Регистрация прошла успешно!")
        else: Error(2, "Пользователь уже существует!")
        
    def del_user(self, user_name):
        if user_name in self.users: 
            del self.users[user_name]
            Message("Пользователь удалён успешно!")
        else: Error(2, "Пользователь не существует!")
            
    def get(self, name):
        if name in self.users: return self.users[name]
        else: Error(1, "Пользователь не найден!")
        return None    
            
    def isset_user(self, user_name):
        return True if user_name in self.servers else False
    
class Client:
    
    def __init__(self, name, server):
        self.name = name
        self.server = server
        self.messages = []
        try: system.get(server).add_user(self)
        except AttributeError: pass
        
    def newMessage(self, name_user, message):
        self.messages.append((name_user, message))
        
    def readMessages(self):
        if len(self.messages) == 0: return
        Message("Сообщения пользователя {}".format(self.name+"@"+self.server))
        print("{} {}".format("E-mail:", "Message:"))
        
        for name,message in self.messages:
            print("{}: {}".format(name, message))
        print("-"*32)     
    
    def send(self, to, server, who, message):
        try: system.get(server).get(to).newMessage(who, message)
        except AttributeError: pass        
    
def main():
    global system
    print("Мультисерверная MDL-почта приветствует вас! \nПросим вас зарегистрироваться.")
    data = input("Введите данные в формате <user@server.ru>:\n")
    data = (data.split("@")[0], data.split("@")[1])
    server = Server(data[1])
    user = Client(data[0], data[1])
    
    
class Interface:
    
    def __init__(self):
        self.system = system
        
    def main(self):
        print("Мультисерверная MDL-почта приветствует вас!")
        #user, server = self.reg()
        #print(self.system.getServers())
        #print(server.getUsers())
        while True:
            action = self.actions()
            if action == 1: self.reg()
            elif action == 2: self.deluser()
            elif action == 3: self.read()
            elif action == 4: self.mail()
            elif action == 5: self.getServers()
            elif action == 6: self.getUsersOfServer()
            elif action == 7: break
    
    def getServers(self):
        Message("Действующие сервера:")
        data = list(self.system.getServers().keys())
        for server in range(len(data)):
            print(str(server+1)+'. '+data[server])
        print("-"*32)
        
    def getUsersOfServer(self):
        server = self.system.get(input("Имя сервера (без символа <@>)"))
        Message("Действующие пользователи сервера {}:".format(server.name))
        data = list(server.getUsers().keys())
        for user in range(len(data)):
            print(str(user+1)+'. '+data[user])
        print("-"*32)
        
    def reg(self):
        name, server_name = self.__parse()
        server = self.system.get(server_name)
        user = Client(name, server_name)
        return user,server
    
    def deluser(self):
        name, server_name = self.__parse()
        server = self.system.get(server_name)
        server.del_user(name)
    
    def read(self):
        name, server_name = self.__parse()
        server = self.system.get(server_name)
        obj = server.get(name)
        if obj != None: obj.readMessages()
        return
    
    def mail(self):
        to, server_to = self.__parse("Отправка письма => Кому: ")
        fr, server_fr = self.__parse("Отправка письма => От кого: ")
        message = input("Отправка письма => Сообщение: ")
        server_fr = self.system.get(server_fr)
        try: 
            server_fr.get(fr).send(to, server_to, fr+'@'+server_fr.name, message)
            Message("Сообщение успешно отправлено!")
        except AttributeError: Error(3, "Отправка писем данному пользователю невозможна.")
        return       
    
    def actions(self):
        print("Ваши возможные действия: ")
        print("1. Регистрация нового аккаунта.")
        print("2. Удаление аккаунта.")
        print("3. Прочтение писем пользователя.")
        print("4. Отправка письма пользователю.")
        print("5. Вывод всех серверов.")
        print("6. Вывод пользователей сервера.")
        print("7. Выход.")
        return int(input())
    
    def __parse(self, text=False):
        data = input("Введите данные в формате <user@server.ru>:\n") if not text else input(text)
        data = (data.split("@")[0], data.split("@")[1])
        return data[0], data[1]
    
window = Interface()
window.main()