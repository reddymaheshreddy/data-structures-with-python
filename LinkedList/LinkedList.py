class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        itr = self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+'--->'
            itr=itr.next
        print(llstr)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)
    def insert_values(self,data_list):
        self.head = None
        for ele in data_list:
            self.insert_at_end(ele)
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_begining (data)
            return
        count = 0
        itr =self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr=itr.next
            count += 1
    def insert_after_value(self,data_after,data_to_insert):
        itr=self.head
        
        while itr:
            if itr.data==data_after:
                
                itr.next=Node(data_to_insert,itr.next)
                return
            itr=itr.next
        return


    def remove_by_value(self,data):
        itr=self.head
        if self.head is None:
            return
        if itr.data == data:
            if itr.next is not None:
                self.head=Node(itr.next.data,itr.next.next)
                return
            else:
                itr=Node(None,None)
                return
        while itr:
            if itr.next is not None and itr.next.data==data:
                if itr.next.next is not None:
                    itr.next=Node(itr.next.next.data,itr.next.next.next)
                    return
                else:
                    itr.next=Node(None,None)
                    return
            itr=itr.next
              
if __name__=="__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
