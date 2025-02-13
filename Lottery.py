from random import randint

class Lottery():

    def __init__(self, m, n):
        self.__m = m
        self.__n = n

    @classmethod
    def Verify(cls, m, n):
        return m <= n

    def Generate(self):
        if Lottery.Verify(self.__m, self.__n):
            l = set()
            while len(l) < self.__m:
                i = (randint(1, self.__n))
                if i not in l:
                    l.add(i)
            return l


p = Lottery(4, 20)
p.m = 100
q = Lottery(17, 17)
print(p.Generate())
print(q.Generate())