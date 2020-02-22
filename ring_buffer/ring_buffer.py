from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # append changes depending on if the list is full or not

        if self.capacity == self.storage.length:
            # override the oldest element (head) with the item
            # self.storage.head
            print("at capacity")
            # i think i need get() for this to work so that I can replace items in the middle
        else:
            self.storage.add_to_tail(item)
            print("\n\nstorage: ", self.storage.length, "\n\n")
            print(self.get())

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head

        while current is not None:
            # add the current value to the list
            list_buffer_contents.append(current.value)
            # update current to the next item in the DLL
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
