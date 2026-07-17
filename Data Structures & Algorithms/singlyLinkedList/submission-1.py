class ListNode :
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        # self.tail = head.next       

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i+=1
        return -1

        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        if not curr or not curr.next:
            return False
        curr.next = curr.next.next
        return True
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        ll = []
        while curr:
            ll.append(curr.val)
            curr = curr.next
        return ll

        
