"""
案例: 演示封装之私有属性.

封装简介:
    概述:
        属于面向对象的三大特征之一, 就是隐藏对象的属性和实现细节, 仅对外提供公共的访问方式.
    怎么封装?
        我们学的 函数, 类 都是封装的体现.
    好处:
        1. 提高代码的安全性.        由 私有化 来保证
        2. 提高代码的复用性.        由 函数 来保证
    弊端:
        代码量增加了. 因为私有内容外界想访问, 必须提供公共的访问方式, 代码量就增加了.

私有格式:
    __属性名
    __函数名()
"""
# 故事5: 小明把技术给徒孙的时候, 不希望把自己的私房钱给徒孙, 代码模拟.
# 1. 定义师傅类Master

# 2. 定义学校类School

# 3. 定义徒弟类

class Prentice:
    # 3.1 属性
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        # 私房钱.
        self.__money = 20000

    # 3.2 方法
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    # 3.3 针对私有的属性, 提供公共的访问方式.
    def get_money(self):         # 获取 ， 公共接口，让你可以看得到
        return self.__money

    def set_money(self, money):  # 设置 ， 让你可以设置
        self.__money = money

# 4. 定义徒孙类
class TuSun(Prentice):
    pass

# 5. 测试.
if __name__ == '__main__':
    # 属性 = print
    # 函数 = 调用ts
    ts = TuSun()
    print(ts.kongfu)
    ts.make_cake()
    print('-' * 34)

    # print(ts.__money)     # 报错, 父类私有成员, 子类无法访问.

    ts.set_money(100)       # 设置函数的值
    print(ts.get_money())   # 通过父类提供的公共的访问方式, 访问父类的私有成员.
    
