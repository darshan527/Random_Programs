class Node(object):
    """
    Create a Node for Linked List.
    """
    def __init__(self, value) -> None:
        """
        Takes Value.
        """
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None
        else:
            tmp = self.head.value
            self.head = self.head.next
            self.num_elements -= 1
            return tmp


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    print(stack.size())