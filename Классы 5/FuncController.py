class FunctionController:
    
    def __init__(self, number):
        self.functions = {"x":self.x, "sqrt_fun":self.sqrt_fun}
        self.results = []
        self.num = {}
        for _ in range(number): self.interpretate(input().split())
        for arr in self.results:
            print(*arr)
    
    def interpretate(self, data):
        
        operations = {"+": lambda x, y: x + y,
                      "-": lambda x, y: x - y,
                      "*": lambda x, y: x * y,
                      "/": lambda x, y: x / y}
        
        def trytonumber(x):
            try: return float(x)
            except ValueError: return None
            
        
        if data[0] == "define":
            name = data[1]
            arg1 = self.functions[data[2]] if trytonumber(data[2]) == None else trytonumber(data[2])
            arg2 = self.functions[data[4]]
            operation = operations[data[3]]
            if (type(arg1) == float or type(arg1) == int):
                self.num[name] = arg1
                arg1 = lambda x: self.num[name]
            func = lambda x: operation(arg1(x), arg2(x))
            self.functions[name] = func
            
        elif data[0] == "calculate":
            numbers = [float(i) for i in data[2:]]
            self.results += [list(map(lambda x: str(int(x)) if int(x) == float(x) else str(x), [self.functions[data[1]](n) for n in numbers]))]
            
    
    def x(self, x):
        return x
    
    def sqrt_fun(self, x):
        from math import sqrt
        return sqrt(x)

            
fc = FunctionController(int(input()))