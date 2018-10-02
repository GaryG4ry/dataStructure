class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):  # 判断链表是否为空
        return (self.length == 0)

    def append(self, dataOrNode):  # 向链表尾部假如一个新的节点
        # 判断加入的是不是个节点
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:  # 如果头结点不存在
            self.head = item
            self.length += 1
        else:  # 如果头结点存在，就一直向下找，知道找到此时链表的最后一个节点，再将next指向新加入的值
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():  # 判断链表是否为空，空的话没必要删除
            print('error:the linklist is empty!')
            return

        if index < 0 or index >= self.length:  # 判断输入的索引是否合法
            print('error:index out of range!')
            return

        if index == 0:  # 判断是否要删除头结点
            self.head = self.head._next
            self.length -= 1
            return
        # 开始找到index的位置，然后删除操作，也就是把索引的前一个节点指向索引的后一个节点    不需要判断是否是最后一个节点
        # 不仅要找到当前的索引指向的节点 还要找到此索引节点的上一个节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            prev._next = node._next
            self.length -= 1

    def insert(self, index, dataOrNode):
        if self.isEmpty():  # 判断为空
            print('error,empty LinkList!')
            return

        if index < 0 or index >= self.length:  # 判断输入的索引是否合法
            print('error:index out of range!')
            return
        # 判断要插入的是不是个节点的类型 不是的话 将其变成节点类型
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        # 判断插入是否为头结点 如果是 就将其的next指向头结点 并将其指定为头结点
        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return
        # 跟删除一样的操作
        j = 0
        prev = self.head
        node = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index > self.length:
            print('error,index out of range!')
            return

        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        if j == index:
            node.data = data

    def getItem(self, index):
        if self.isEmpty() or index < 0 or index > self.length:
            print('error,index out of range!')
            return

        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    def getIndex(self, data):
        if self.isEmpty():
            print('error:empty list!')
            return

        j = 0
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print('not found!')

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ''
            node = node._next
        return nlist

    def __getitem__(self, item):
        if self.isEmpty():
            return
        return self.getItem(item)

    def __setitem__(self, key, value):
        if self.isEmpty():
            return
        return self.update(key, value)

    def __len__(self):
        return self.length
