"""
案例: 自定义代码模拟链表

链表介绍:
    概述:
        它属于数据结构之 线性结构的一种, 每个节点都只能有 1个前驱 和 1个后继节点.
    作用:
        用于优化顺序表的弊端(如果没有足够的连续的内存空间, 会导致扩容失败)
        链表扩容时, 有地儿就行, 连不连续无所谓.
    组成:
        由 节点 组成, 其中节点由 元素域(数值域) 和 链接域(地址域)组成.
    分类:
        根据 节点类型不同, 链表主要分为:
        单向链表: 节点由1个数值域 和 1个地址域组成, 前边节点的地址域存储的是后续节点的地址, 最后1个节点的地址域为 None
        单向循环链表:
        双向链表:
        双向循环链表:
        详见今日随堂图片.

自定义代码模拟链表, 思路分析:
    1. 自定义SingleNode类, 表示 节点类.
        属性:
            item   数值域(元素域)
            next   地址域(链接域)

    2. 自定义SingleLinkedList类, 表示: 链表
        属性:
            head  表示头结点, 指向第1个节点.
        行为:
            is_empty(self) 链表是否为空
            length(self) 链表长度
            travel(self. ) 遍历整个链表
            add(self, item) 链表头部添加元素
            append(self, item) 链表尾部添加元素
            insert(self, pos, item) 指定位置添加元素
            remove(self, item) 删除节点
            search(self, item) 查找节点是否存在

    3. 测试.
"""

# 1. 自定义SingleNode类, 表示 节点类.
class SingleNode:
    # 初始化属性
    def __init__(self, item):
        self.item = item        # 元素域(数值域)
        self.next = None        # 链接域(地址域)


# 2. 自定义SingleLinkedList类, 表示: 链表
class SingleLinkedList:
    # 1. 初始化属性.
    def __init__(self, node=None):
        self.head = node      # 链表的 头结点, 指向第1个节点.

    # 2. is_empty(self) 链表是否为空
    def is_empty(self):
        pass

    # 3. length(self) 链表长度
    def length(self):
        pass

    # 4. travel(self. ) 遍历整个链表
    def travel(self):
        pass

    # 5. add(self, item) 链表头部添加元素
    def add(self, item):
        pass

    # 6. append(self, item) 链表尾部添加元素
    def append(self, item):
        pass

    # 7. insert(self, pos, item) 指定位置添加元素
    def insert(self, pos, item):
        pass

    # 8. remove(self, item) 删除节点
    def remove(self, item):
        pass

    # 9. search(self, item) 查找节点是否存在
    def search(self, item):
        pass


# 3. 在main中测试
if __name__ == '__main__':
    # 3.1 测试节点类.
    node1 = SingleNode(10)
    # 3.2 打印当前节点的 元素域(数值域) 和 链接域(地址域)
    print(f'元素域(数值域): {node1.item}')    # 10
    print(f'链接域(地址域): {node1.next}')    # None
    print(f'node1对象: {node1}')            # 地址值, 可以重写 str魔法方法改为打印属性值.
    print(f'node1的类型: {type(node1)}')
    print('-' * 23)

    # 3.2 测试链表类.
    # my_linkedlist = SingleLinkedList()
    my_linkedlist = SingleLinkedList(node1)
    print(f'头结点为: {my_linkedlist.head}')
    print(f'头结点的元素域: {my_linkedlist.head.item}')    # 10
    print(f'头结点的地址域: {my_linkedlist.head.next}')    # None