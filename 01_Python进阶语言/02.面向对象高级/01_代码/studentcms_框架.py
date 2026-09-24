"""
该文件用于 完成学生管理系统的 具体业务的操作, 即: 增删改查, 保存学生信息等...
"""

# 导包
from student import Student


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
        pass

    # 5. 定义函数, 实现删除学生信息功能.
    def del_student(self):
        pass

    # 6. 定义函数, 实现修改学生信息功能.
    def update_student(self):
        pass

    # 7. 定义函数, 实现查询单个学生信息功能.
    def search_one_student(self):
        pass

    # 8. 定义函数, 实现查询所有学生信息功能.
    def search_all_student(self):
        pass

    # 9. 定义函数, 实现保存学生信息功能.
    def save_student(self):
        pass

    # 10. 定义函数, 实现加载学生信息.
    def load_student(self):
        pass

    # 11. 定义函数, 把上述的所有业务逻辑跑通.
    def start(self):
        # 11.1
        # 11.2 死循环, 不断的玩儿.
        while True:
            # 11.3
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
