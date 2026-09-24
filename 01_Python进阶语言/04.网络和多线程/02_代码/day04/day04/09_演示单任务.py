"""
案例: 演示单任务, 前边不执行完毕, 后边绝对无法执行.
"""

# 1.定义函数A, 输出10次 hello world
def func_a():
    for i in range(1000000):
        print("hello world")

# 2. 定义函数B, 输出10次 hello python
def func_b():
    for i in range(2):
        print("hello python")


func_a()
print('-' * 23)
func_b()
