# 删除结点
def remove(self, item):
    # 游标
    cur = self.head
    # 辅助游标(指向前一个结点的游标)
    pre = None

    while cur is not None:
        # 找到要删除的结点
        if cur.item == item:
            # 若删除是头结点
            if cur == self.head:
                self.head = cur.next
            else:
                pre.next = cur.next
            return
        # 没有找到要删除的元素
        else:
            pre = cur
            cur = cur.next
