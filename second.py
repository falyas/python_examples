class Change:
    def __init__(self,count=0):
        self.__count=count
c1=Change(5)
c2=Change(5)
print(c1)
print(c2)
print(id(c1)==id(c2))

s1="good"
s2="good"
print(s1)
print(s2)
print(id(s1)==id(s2))
