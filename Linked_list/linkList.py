class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Linked_List:
    def __init__(self,start=None):
        self.start = start
    def isEmpty(self):
        return self.start == None 
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n
    def insert_at_last(self,data):
        n = Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
    def print_items(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
        print()
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def delete_item(self,data):
        if self.start == None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item ==  data:
                self.start = temp.next
            else:
                while temp is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self,start):
        self.current = start
    def  __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# my_list = Linked_List()
# my_list.insert_at_start(4)
# my_list.insert_at_last(5)
# my_list.insert_at_last(6)
# my_list.insert_after(my_list.search(4),7)
# # my_list.print_items()
# my_list.delete_item(4)
# # my_list.print_items()
# for x in my_list:
#     print(x,end=" ")



