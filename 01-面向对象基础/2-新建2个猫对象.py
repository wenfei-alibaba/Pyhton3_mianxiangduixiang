class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫爱喝水")
#创建猫对象
tom = Cat()
tom.eat()
tom.drink()
print(tom)
lazy_tom=Cat()
lazy_tom.eat()
lazy_tom.drink()
lazy_tom2=lazy_tom
print(lazy_tom2)