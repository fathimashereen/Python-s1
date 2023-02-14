class A:
    def __init__(self):
        self.fruits=[]
        self.vegetables=[]
        print("enter 3 fruits")
        for i in range(3):
            a=input()
            self.fruits.append(a)
        print("enter 3 vegetables")
        for i in range(3):
            b=input()
            self.vegetables.append(b)
    def display(self):
        print("list of fruits:",self.fruits)
        print("list of vegetables:",self.vegetables)



obj1=A()
obj1.display()
