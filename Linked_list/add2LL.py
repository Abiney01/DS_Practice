class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    @staticmethod
    def add_two_LL(head1,head2):
        dummy = Node(0)
        current = dummy
        carry = 0
        while head1 or head2 or carry:
            val1 = head1.data if head1 else 0
            val2 = head2.data if head2 else 0
            total = val1+val2+carry
            carry = total//10
            current.next = Node(total%10)
            current = current.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        return dummy.next
    
    @staticmethod
    def create(list):
        dummy = Node(0)
        current = dummy
        for num in list:
            current.next = Node(num)
            current = current.next
        return dummy.next
    @staticmethod
    def print(result):
        while result:
            print(result.data,end=" " if result.next else "")
            result = result.next
        print()
head1 = Node.create([1,2,3])
head2 = Node.create([4,5,6])
result = Node.add_two_LL(head1,head2)
Node.print(result)