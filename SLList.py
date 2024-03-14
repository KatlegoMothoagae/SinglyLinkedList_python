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

    def __str__(self):
        lst = ""
        current_node = self.head
        while current_node is not None:
            lst+= str(current_node.data)+" => "
            current_node = current_node.next
        return lst

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

    def reverse(self):
        current_node = self.head
        prev = None
        while current_node is not None:
            buffer = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = buffer

        self.head, self.tail = self.tail, self.head

    def deleteDuplicates_2(self):
        new_lst = SLList()


        seen = set()
        current_node = self.head
        while current_node is not None:
            # print(new_lst.__str__())
            if current_node.data not in seen:
                new_lst.add(current_node.data)
                seen.add(current_node.data)
            current_node = current_node.next
        self.head = new_lst.head
        return new_lst

    def deleteDuplicates(self):

        current_node = self.head
        check = current_node.data
        while current_node is not None and current_node.next is not None:
                if current_node.next.data == check:
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next
                    check = current_node.data
                    print(f"check: {check}")





# Definition for singly-linked list.

# class Solution:
#     def deleteDuplicates(self, head):ListNode(1, ListNode(1, ListNode(2, ListNode(3))))
#         current_node = head
#         while current_node is not None:
#             if current_node.val == current_node.next.val:
#                 current_node.next = current_node.next.next
#         return head

if __name__ == "__main__":
    head = SLList()
    head.add(1)
    head.add(1)
    head.add(1)
    head.add(1)
    head.add(1)
    head.add(1)
    head.add(2)
    head.add(2)
    head.add(1)
    head.add(1)
    head.add(1)

    head.deleteDuplicates()
    print(head)

