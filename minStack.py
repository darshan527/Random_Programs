class Stack:
    def __init__(self) -> None:
        self.items = []
        self.minItem = []

    def push(self, num: int) -> int:
        """
        Inserts a item at the top of a Stack.
        """
        self.items.append(num)
        if len(self.minItem) == 0:
            self.minItem.append(num)
        else:
            if num <= self.minPeek():
                self.minItem.append(num)
            else:
                self.minItem.append(self.minPeek())

    def pop(self) -> None:
        """
        Pop top item of the stack.
        """
        print(self.items.pop())
        self.minItem.pop()

    def display(self):
        """
        Prints all the items of the stack 
        along with the min item at each stage.
        """
        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i], self.minItem[i])

    def peek(self) -> int:
        """
        Returns the top item of the Stack
        """
        return self.items[-1]

    def minPeek(self) -> int:
        """
        Returns the minimum element of the Stack.
        """
        return self.minItem[-1]


#Driver Code
if __name__ == "__main__":
    stack = Stack()
    l = [1, 2, 3, 4, -9, 5]
    for i in l:
        stack.push(i)
    stack.display()
    stack.pop()
    stack.pop()
    print(stack.minPeek())
    print(stack.peek())