from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            if self.current == self.storage.head:
                # print('checking current value',self.current.value)
                self.current = self.storage.head.next
                # print('checking value after next',self.current.value)
                self.storage.remove_from_head()    
                self.storage.add_to_head(item)
            elif self.current != self.storage.head and self.current != self.storage.tail:
                self.current.value = item
                self.current = self.current.next
            elif self.current == self.storage.tail:
                self.current = self.storage.head
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                



        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        print('test printing here')
        # list_buffer_contents.append(self.current)
        # TODO: Your code here
        current_node = self.storage.head
        while current_node is not None:
            print(current_node.value)
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
      

        return list_buffer_contents

# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
