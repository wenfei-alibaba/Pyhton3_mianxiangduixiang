class Cat:
    def __init__(self):
        print("这是一个初始化方法")
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat()
print(tom.name)
