class Cat:
    def __init__(self,new_name):
        print("这是一个初始化方法")
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
print(tom.name)
lazt_cat = Cat("大懒猫")
lazt_cat.eat()
