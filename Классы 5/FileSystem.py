class Directory:
    
    def __init__(self, name, parent):
        
        self.name = name
        self.parent = parent if parent else self
        self.dirs = {}
        self.files = {}
        
    def __iadd__(self, dir_obj):
        self.dirs[dir_obj.name] = dir_obj
        return self
        
        
    def addfile(self, file_obj):
        self.dirs[file_obj.name] = file_obj
        
    
    def getAllDirs(self):
        for dir in self.dirs.keys():
            print("-", dir)
            
    def getAllFiles(self):
        for file in self.files.keys():
            print("-", file)    
            
    
class File:
    
    def __init__(self, name, text):
        
        self.name = name
        self.text = text

    
    def read(self):
        return self.text
    
class Interface:
    
    def __init__(self):
        
        self.current = Directory("/", False)
        self.url = "/"
        
    
    def createDirectory(self, name):
        self.current.dirs[name] = Directory(name, self.current)
        
    def createFile(self, name, text):
        obj = File(name, "")
        obj.text = text
        self.current.files[name] = obj
        
    def readFile(self, name):
        print()
        print("-"*16)
        print("Содержимое файла", name)
        print("-"*16)
        print(self.current.files[name].read())
        print("-"*16)
        print()
        
    def changeDir(self, name="", toBack=False):
        if toBack: 
            self.url = self.url.replace(self.current.name+"/", "")
            self.current = self.current.parent
            return
        else: 
            self.current = self.current.dirs[name] if name in self.current.dirs else self.current
            self.url += self.current.name+"/"
        
        
    def actions(self):
        
        def getStructure(self, title, arr, data):
            if len(arr) == 0: return
            print("-"*16+"\n{}: \n".format(title))
            data()
            print("-"*16)
            
        while True:
            print("Текущее положение:", self.url)
            getStructure(self, "Дирректории", self.current.dirs.keys(), self.current.getAllDirs)
            getStructure(self, "Файлы", self.current.files.keys(), self.current.getAllFiles)
            print("\nДействие:\n")
            print("1. Создать дирректорию:")
            print("2. Перейти в дочернюю дирректорию:")
            print("3. Перейти в родительскую дирректорию:")
            print("4. Создать файл:")
            print("5. Прочесть файл:")
            print("6. Выход:")
            action = int(input())
            if action == 1: self.createDirectory(input("Имя дирректории: "))
            elif action == 2: self.changeDir(input("Имя дирректории: "))
            elif action == 3: self.changeDir("", toBack=True)
            elif action == 4: self.createFile(input("Имя файла: "), input("Текст файла: "))
            elif action == 5: self.readFile(input("Имя файла: "))
            elif action == 6: return
            

ui = Interface()
ui.actions()
    