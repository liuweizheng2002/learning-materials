"""

学生文件

"""


class Student:  # 定义学生类
    def __init__(self, name, gender, age, phone, desc):
        """
        该魔法方法用于初始化 属性信息
        :param name:    姓名
        :param gender:  性别
        :param age:     年龄
        :param phone:   电话号
        :param desc:    描述信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        """
        该魔法方法用于 打印 学生信息
        :return:
        """
        return (f'姓名: {self.name}, 性别: {self.gender}, 年龄: {self.age},'
                f' 电话号: {self.phone}, 描述信息: {self.desc}')



if __name__ == '__main__':
    s1 = Student('张三', '男', 18,
                '13800000000', '好好学习, 天天向上')
    print(s1)
