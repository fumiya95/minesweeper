class re_car:
    def __init__ (self,color):
        self.color = color
        print("必ず実行される")
    
    def drive(self):
        print(self.color + "色の車がブゥーーん")

my_car = re_car("Red")#インスタンスか、実体化
print(my_car.color)
my_car.drive()
my_car2 = re_car("Blue")
print(my_car2.color)
my_car2.drive()