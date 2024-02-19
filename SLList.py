class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class _SLListIterator:
    def __init__(self, head):
        self._current_node = head

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_node is None:
            raise StopIteration
        else:
            data = self._current_node.data
            self._current_node = self._current_node.next
            return data


class SLList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return _SLListIterator(self.head)

    def __contains__(self, item):
        current_node = self.head
        while current_node is not None and current_node.data != item:
            current_node = current_node.next
        return current_node is not None

    def add(self, data):
        node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, target_data):
        prev_node = None
        current_node = self.head
        while current_node is not None and current_node.data != target_data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is not None:
            self.size -= 1
            if current_node is self.head:
                self.head = current_node.next
            else:
                prev_node.next = current_node.next
            if current_node is self.tail:
                self.tail = prev_node

