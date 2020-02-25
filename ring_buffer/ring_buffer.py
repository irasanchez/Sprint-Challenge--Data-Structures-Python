from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if below cap
        if self.storage.length < self.capacity:
            # add items at the back
            self.storage.add_to_tail(item)
        else:
            # if at cap or higher
            # check if there is a "current" value, covers first pass
            if self.current is None:
                # if not, remove from the front of the list
                self.storage.remove_from_head()
                # then add the item in place of the removed one
                self.storage.add_to_head(item)
                # reset the "current" to the head
                self.current = self.storage.head
            else:
                # if it's not the first pass
                # check if current is the tail of the storage
                if self.current.next:
                    # if it is not the tail, insert the item in between the current item and the following item
                    self.current.insert_after(item)
                    # update the "current" tracker
                    self.current = self.current.next
                    # delete the item
                    self.current.next.delete()
                else:
                    # if it is the tail though, remove from the front
                    self.storage.remove_from_head()
                    # replace the item there
                    self.storage.add_to_head(item)
                    # update the "current" tracker
                    self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # keep track of current item to be able to loop below
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
