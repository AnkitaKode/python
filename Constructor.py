class Point:
    def __init__(self,x,y):    #Constructor classs
        self.x=x
        self.y=y
    def move(self):
        print("Move")
    def go(self):
        print("Go")


num=Point(10,20)
print(num.y)