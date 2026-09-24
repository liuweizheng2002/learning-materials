"""

学生管理系统文件

"""

from student import Student  # 导入包
import time

# 一.创建学生管理系统类
class StudentCMS(object):
    # （1）创建魔法方法，初始化属性信息
    def __init__(self):
        # 创建一个空列表，用于存储学生信息
        self.stu_list = []
        # 创建一个列表，用于存储学生信息(测试用）
        # self.stu_list = [
        #     Student('张三', '男', 18, '13800000000', '不好好学, 天天想上'),
        #     Student('李四', '女', 19, '13800000001', '好不容学, 天天向下'),
        #     Student('王五', '男', 20, '13800000002', '天天学习, 好好向上'),
        #     Student('赵六', '女', 21, '13800000003', '好习好学, 天向天上'),
        # ]

    # 1.定义函数，实现打印，管理系统的界面
    @staticmethod
    def show_view():
        print('*' * 23)
        print('学生管理系统V2.0版')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('*' * 23)
        print()

    # 2.定义函数，实现添加学生信息功能
    def add_student(self):
        # 1.提示用户录入学生信息
        name = input('请输入学生的姓名:')
        gender = input('请输入学生的性别:')
        age = int(input('请输入学生的年龄:'))
        phone = input('请输入学生的电话号:')
        desc = input('请输入学生的描述信息:')
        # 2.创建学生对象，并把学生信息封装到列表中
        stu = Student(name, gender, age, phone, desc)
        # 3.把学生对象添加到列表中
        self.stu_list.append(stu)
        # 4.提示用户添加学生信息成功
        print(f'添加{stu.name}的学生信息成功\n')

    # 3.定义函数，实现删除学生信息功能
    def del_student(self):
        del_name = input('请输入要删除学生的姓名:')
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f'删除{stu.name}的学生信息成功!\n')
                # 输出删除学生信息成功后的列表
                break
        else:
            print(f'没有找到{del_name}的学生信息。\n')

    # 4.定义函数，实现修改学生信息功能
    def update_student(self):
        upd_name = input('请输入要修改学生的姓名:')
        for stu in self.stu_list:
            if stu.name == upd_name:
                stu.age = int(input('请输入修改后学生的年龄:'))
                stu.gender = input('请输入修改后学生的性别:')
                stu.phone = input('请输入修改后学生的电话号:')
                stu.desc = input('请输入修改后学生的描述信息:')

                print(f'修改{stu.name}的学生信息成功!\n')
                break
        else:
            print(f'没有找到{upd_name}的学生信息。\n')


    # 5.定义函数，实现查询单个学生信息功能
    def search_one_student(self):
        search_name = input('请输入要查找学生的姓名:')
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu, end='\n\n')
                break
        else:
            print(f'没有找到{search_name}的学生信息。\n')

    # 6.定义函数，实现查询所有学生信息功能
    def search_all_student(self):
        # 判断列表是否为空
        if self.stu_list == []:
            print(f'暂时没有学生信息\n')
        else:
            for stu in self.stu_list:
                print(stu)
            print()

    # 7.定义函数，实现保存学生信息功能
    def save_student(self):
        # 拓展功能，__dict__功能，把学生信息保存到文件中
        # 1.文件关联学生信息文件
        with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
            # 2.把学生信息转成字典形式，写入stu_dict空字典中
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            # 3.把学生信息转成字符串形式，并用write写入文件中
            dest_f.write(str(stu_dict))

    # 8.定义函数，实现加载学生信息
    def load_student(self):
        # 加入try...except...语句，如果文件不存在，则创建文件
        try:
            with open('./stu_data.txt', 'r', encoding='utf-8') as src_f:
                # 1.把文件中的字符串形式的学生信息转成字典形式
                stu_dict = src_f.read()
                # 2.把字典形式的学生信息转成列表形式
                stu_list = eval(stu_dict)
                # 3.如果列表为空，则把列表转成空列表
                if len(stu_dict) == 0:
                    # 把列表转成空列表
                    stu_list = []
                # 4.把列表形式的学生信息转成学生对象，并赋值给self.stu_list]
                self.stu_list = [Student(**stu) for stu in stu_list]

        except:
            with open('./stu_data.txt', 'w', encoding='utf-8') as src_f:
                pass

    # 9.定义函数，把上述的所有业务逻辑跑通
    def start(self):
        # 1.加载学生信息
        self.load_student()
        # 2.加载学生信息死循环
        while True:
            # 1.添加休眠时间
            time.sleep(1)
            # 2.打印学生管理系统的界面
            StudentCMS.show_view()
            # 3提示用户录入要操作的编号，并接受
            input_num = input('请输入您要操作的编号:')
            # 4.根据用户输入的编号做不同的操作
            if input_num == '1':
                # print('添加学生信息\n')
                self.add_student()
            elif input_num == '2':
                # print('删除学生信息\n')
                self.del_student()
            elif input_num == '3':
                # print('修改学生信息\n')
                self.update_student()
            elif input_num == '4':
                # print('查询单个学生信息\n')
                self.search_one_student()
            elif input_num == '5':
                # print('查询所有学生信息\n')
                self.search_all_student()
            elif input_num == '6':
                self.save_student()
                print('保存学生信息成功！\n')
            elif input_num == '0':
                # 退出系统，做二次效验
                result = input('您确定要退出吗?(Y/N) -> ')
                if result.lower() == 'y':
                    # 字符串lower（）-> 用户输入的是大写的Y，小写的y，都可以转成小写形式
                    # 在退出前保存学生信息到文件
                    self.save_student()
                    print('已退出系统,下次再见。\n')
                    break
                else:
                    print('您已取消退出\n')
                    continue
            else:
                print('您的输入有误，请重新输入!\n')
                continue


# 二.测试
if __name__ == '__main__':
    # 1.创建学生管理系统的对象
    cms = StudentCMS()
    # 2.调用学生管理系统对象的start()函数，启动学生管理系统,
    cms.start()
