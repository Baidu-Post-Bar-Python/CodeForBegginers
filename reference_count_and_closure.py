class Garbage:
    id = 0

    def __init__(self):
        Garbage.id += 1
        self.id = Garbage.id
        print(f'{str(self)}正在被创建')

    def __del__(self):
        print(f'{str(self)}正在被销毁')

    def __str__(self):
        return f'<{self.id} 号对象>'


def outer():
    g = Garbage()

    def inner():
        print(f'inner 引用了外部的 {str(g)}')
    return inner    # inner 的闭包引用了g，在inner被销毁前引用计数不会变为0


def no_reference():
    g = Garbage()
    print(f"局部变量g会在函数调用结束后被销毁，导致函数调用结束后{str(g)}的引用计数减为0而被销毁")


print("例1", "*" * 30)
no_reference()
print("例2", "*" * 30)
outer()
# 没有东西去引用返回的inner函数，
# 因此其引用计数为0，
# 因此这个返回的函数将被销毁，
# 其闭包也随之被销毁，
# 导致闭包内的局部变量g也被销毁，
# 最终导致局部创建的Garbage对象被销毁
print("例3", "*" * 30)
print("赋值会增加返回的inner函数的引用计数")
inner1 = outer()
print("因此返回的函数暂时不会被销毁")
inner1()
print("例4", "*" * 30)
inner2 = outer()
inner2()
print("手动删除变量，也会导致引用计数减少")
del inner2
print("删除了inner2之后，程序该结束了，所有全局变量都将被销毁")
print("因此最终inner1的闭包内的g（对应的是<3 号对象>）也会被销毁")
