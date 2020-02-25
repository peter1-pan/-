#! /usr/bin/env python3
# -*- coding:utf-8 -*-


class SingleNode(object):
    '''单链表的节点'''
    def __init__(self,item):
        # _item 存放数据元素
        self.item = item
        # _next 下一个节点的标识
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self,node=None):
        self.__head = node    # __head私有属性，node(节点)初始化-> None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        #cur游标，用来移动遍历节点
        cur = self.__head
        # count 计数
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.__head
        while cur != None:
            print (cur.item,end=' ')
            cur = cur.next
        print ("")  # 遍历换行

    def add(self,item):
        '''头部添加元素'''
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        '''尾部添加元素'''
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将__head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pop,item):
        '''指定位置添加元素'''
        if pop <= 0:   # 若指定位置pos为第一个元素之前，则执行头插入
            self.add(item)
        elif pop > (self.length()-1):   # 若指定位置超过链表尾部，则执行尾部插入
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pop-1):
                count += 1
                pre = pre.next
            node = SingleNode(item) 
            node.next = pre.next     # 先将新节点node的next指向插入位置的节点
            pre.next = node          # 再将插入位置的前一个节点指向新节点



    def remove(self,item):
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def serarch(self,item):
        '''链表查找节点是否存在，并返回True或False'''
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    # print(ll.is_empty())
    # print(ll.length())

    ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())  

    ll.append(2)
    ll.append(3)
    ll.append(4)
    # ll.add(8)
    # ll.insert(2,9)
    # ll.insert(-2,2)
    # ll.insert(15,10)
    # ll.travel()
    ll.remove(3)
    ll.travel()