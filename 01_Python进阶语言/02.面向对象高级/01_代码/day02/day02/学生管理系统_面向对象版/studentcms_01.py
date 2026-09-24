"""
该文件用于 完成学生管理系统的 具体业务的操作, 即: 增删改查, 保存学生信息等...
"""

# 导包
from student import Student
import time

# 1. 创建学生管理系统类.
class StudentCMS(object):
    # 2. 通过魔法方法init, 初始化属性信息.
    def __init__(self):
        # 创建一个空列表, 用于存储学生信息.
        self.stu_list = []      # [学生对象, 学生对象, 学生对象] -> [Student(...), Student(...)...]

    # 3. 定义函数, 实现打印 管理系统的界面.
    def show_view(self):
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


    # 4. 定义函数, 实现添加学生信息功能.
    def add_student(self):
        name = input('请输入学生姓名：')
        gender = input('请输入学生性别：')
        age = int(input('请输入学生年龄：'))
        phone = input('请输入学生电话：')
        desc = input('请输入学生描述信息：')
        stu = Student(name, gender, age, phone, desc)
        self.stu_list.append(stu)
        print(f'添加 {name} 学生信息成功!\n')

    # 5. 定义函数, 实现删除学生信息功能.
    def del_student(self):
        del_name = input('请输入要删除的学生姓名:')
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f'学员 {del_name} 信息删除成功!\n')
                break
            else:
                print('查无此人, 请检查后重新删除!\n')

    # 6. 定义函数, 实现修改学生信息功能.
    def update_student(self):
        upd_name = input('请输入要修改的学生姓名:')

        for stu in self.stu_list:
            if stu.name == upd_name:
                stu.gender = input('请录入修改后的性别: ')
                stu.age = int(input('请录入修改后的年龄: '))
                stu.phone = input('请录入修改后的电话: ')
                stu.desc = input('请录入修改后的描述信息: ')

                print(f'学员 {upd_name} 信息修改成功!\n')
                break
            else:
                print('查无此人, 请检查后重新操作!\n')

    # 7. 定义函数, 实现查询单个学生信息功能.
    def search_one_student(self):
        search_name = input('请输入要查找的学生姓名:')

        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu, end='\n\n')
                break
            else:
                print('查无此人, 请检查后重新操作!\n')

    # 8. 定义函数, 实现查询所有学生信息功能.
    def search_all_student(self):
        if len(self.stu_list) == 0:
            print('暂无学生信息, 请添加后查询! \n')
        else:
            for stu in self.stu_list:
                print(stu)


    # 9. 定义函数, 实现保存学生信息功能.
    def save_student(self):
        with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            dest_f.write(str(stu_dict))

    # 10. 定义函数, 实现加载学生信息.
    def load_student(self):
        try:
            with open('./stu_data.txt','r',encoding='utf-8')as src_f:
                stu_data = src_f.read()
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                    stu_list = []
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
                stu_dict = [stu.__dict__ for stu in self.stu_list]
                dest_f.write(str(stu_dict))

    # 11. 定义函数, 把上述的所有业务逻辑跑通.
    def start(self):
        # 11.1
        self.load_student()
        # 11.2 死循环, 不断的玩儿.
        while True:
            # 11.3
            time.sleep(1)
            # 11.4 打印 学生管理系统的界面.
            self.show_view()
            # 11.5 提示用户录入要操作的编号, 并接收.
            input_num = input('请输入您要操作的编号:')
            # 11.6 根据用户输入的编号, 做不同的操作.
            if input_num == '1':
                # 添加学生信息
                print('添加学生信息\n')
                self.add_student()
            elif input_num == '2':
                # 删除学生信息
                print('删除学生信息\n')
                self.del_student()
            elif input_num == '3':
                # 修改学生信息
                print('修改学生信息\n')
                self.update_student()
            elif input_num == '4':
                # 查询单个学生信息
                print('查询单个学生信息\n')
                self.search_one_student()
            elif input_num == '5':
                # 查询所有学生信息
                print('查询所有学生信息\n')
                self.search_all_student()
            elif input_num == '6':
                # 保存学生信息
                print('保存学生信息\n')
                self.save_student()
            elif input_num == '0':
                # 退出系统, 做二次校验.
                result = input('您确定要退出吗? (Y/N) -> ')
                if result.lower() == 'y':       # 字符串的lower() -> 把字母转成小写形式.
                    print('谢谢您的使用, 期待下次再会!')
                    break
            else:
                # 输入错误
                print('录入有误, 请重新录入!\n')



# 12. 在main中测试.
if __name__ == '__main__':
    # 12.1 创建学生管理系统对象.
    cms = StudentCMS()
    # 12.2 调用学生管理系统对象的start()函数, 启动学生管理系统.
    cms.start()
