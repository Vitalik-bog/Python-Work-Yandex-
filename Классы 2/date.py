class AmericanDate:
    
    def __init__(self, year, month, day):
        
        self.year = self.set_year(year)
        self.month = self.set_month(month)
        self.day = self.set_day(day)
        
    def set_year(self, year):
        self.year = year
        return year
    
    def set_month(self, month):
        self.month = month
        return month
    
    def set_day(self, day):
        self.day = day
        return day
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day
    
    def format(self):
        return "{}.{}.{}".format(
            str(self.get_month()).rjust(2, '0'),
            str(self.get_day()).rjust(2, '0'),
            str(self.get_year()))
    
class EuropeanDate:
    
    def __init__(self, year, month, day):
        
        self.year = self.set_year(year)
        self.month = self.set_month(month)
        self.day = self.set_day(day)
        
    def set_year(self, year):
        self.year = year
        return year
    
    def set_month(self, month):
        self.month = month
        return month
    
    def set_day(self, day):
        self.day = day
        return day
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day
    
    def format(self):
        return "{}.{}.{}".format(
            str(self.get_day()).rjust(2, '0'),
            str(self.get_month()).rjust(2, '0'),
            str(self.get_year()))

