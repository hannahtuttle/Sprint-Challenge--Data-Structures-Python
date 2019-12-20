from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == self.storage.length:
            self.storage.remove_from_head()

        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        print('test printing here')
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
