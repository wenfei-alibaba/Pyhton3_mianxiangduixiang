class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()
# 可以使用 .属性名 利用赋值语句进行赋值
tom.name = "Tom"
tom.eat()
tom.drink()
print(tom)
# 创建第二个猫对象
lazy_tom = Cat()
lazy_tom.name="大懒猫"
lazy_tom.eat()
lazy_tom.drink()
print(lazy_tom)
