class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def evaluate(equation) -> int:
    ops = {'+', '-', '*', '/'}
    stack = Stack()

    for i in equation:
        if i in ops:
            b = stack.pop()
            a = stack.pop()
            s = a + i + b
            stack.push(str(int(eval(s))))
        else:
            stack.push(i)
    return int(stack.pop())


t1 = ["3", "1", "+", "4", "*"]
t2 = ["4", "13", "5", "/", "+"]
t3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tst = evaluate(t3)
print(tst)
