import time

# 動物類別


class Animal:
    pass
# 鳥類類別


class Bird(Animal):
    # 飛行方法
    def fly(self):
        print("fly")
# 鴨子類別


class Duck(Bird):
    pass


duck = Duck()
duck.fly()


class Date:
    """方法一：使用类方法"""
    # Primary constructor

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)  # Primary
b = Date.today()  # Alternate
