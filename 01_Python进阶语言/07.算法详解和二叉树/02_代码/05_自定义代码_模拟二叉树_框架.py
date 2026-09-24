"""
案例: 自定义代码, 模拟二叉树.

树结构解释:
    概述:
        它属于数据结构的一种, 属于 非线性结构(N个前驱, N个后继)
    特点:
        1. 有且只能有1个根节点.
        2. 每个节点都可以有1个父节点 及 任意个子节点, 根节点除外(没有父节点).
        3. 没有子节点的节点, 称之为: 叶子节点.
    常用分类:
        无序树:
        有序树:
        二叉树:
            完全二叉树: 最后一层不满, 其它都是满的.
            满二叉树: 都是满的.
            非完全二叉树: 中间有断的.
            平衡二叉树: 任意节点的两个子树的高度差不超过1

        我们用的最多的就是: 二叉树
    存储:
        顺序存储: 既要存储数据, 又要存储节点的关系.
        链式存储: 采用节点(item, lchild, rchild)的方式, 形成链表来存储

抽取方法的快捷键: ctrl + alt + M
"""

# 1. 定义Node类, 表示二叉树的节点.
class Node:
    # 初始化属性
    def __init__(self, item):
        self.item = item        # 元素域, 即: 节点存储的数据.
        self.lchild = None      # 左子节点
        self.rchild = None      # 右子节点


# 2. 自定义BinaryTree类, 表示二叉树
class BinaryTree:
    # 2.1 初始化属性.
    def __init__(self, node=None):
        self.root = node        # 根节点, 类似于: 链表的 self.head 头结点

    # 2.2 定义add函数, 表示: 添加节点
    def add(self, item):
        pass

    # 2.3 定义breadth()函数, 表示: 广度优先遍历(逐层遍历, 一层一层遍历)
    def breadth(self):
        pass

    # 2.4 定义preorder()函数, 表示: 深度优先之先序遍历(根左右)
    def preorder(self):
        pass

    # 2.5 定义inorder()函数, 表示: 深度优先之中序遍历(左根右)
    def inorder(self):
        pass

    # 2.6 定义postorder()函数, 表示: 深度优先之后序遍历(左右根)
    def postorder(self):
        pass

# 3. 编写测试函数, 用于测试对应的功能.
# 3.1 定义函数 dm01_测试节点和二叉树()
def dm01_测试节点和二叉树():
    # 1. 创建节点
    node1 = Node('A')
    # 2. 打印节点的 元素域, 左子树, 右子树.
    print(node1.item)  # A
    print(node1.lchild)  # None
    print(node1.rchild)  # None
    print('-' * 23)
    # 3. 测试二叉树.
    # bt = BinaryTree()       # 空的
    # print(bt.root)          # None
    bt = BinaryTree(node1)
    print(bt.root)  # 根节点(的地址)
    print(bt.root.item)  # 根节点的元素域 -> A


# 4.在main函数中具体测试
if __name__ == '__main__':
    dm01_测试节点和二叉树()