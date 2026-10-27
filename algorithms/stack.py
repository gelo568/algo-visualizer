NAME = "Stack"
TYPE = "sort"


class Stack:
    def __init__(self, values=None):
        self.items = []

        if values is not None:
            for value in values:
                self.push(value)

    def push(self, value):
        self.items.append(value)
        return value

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)


def run(numbers):
    steps = []
    stack = Stack()
    data = list(numbers)

    for value in data:
        stack.push(value)
        steps.append({
            "type": "compare",
            "index": len(stack.items) - 1,
            "array": stack.items.copy(),
        })

    while not stack.is_empty():
        stack.pop()
        steps.append({
            "type": "swap",
            "index1": max(0, len(stack.items) - 1),
            "index2": max(0, len(stack.items)),
            "array": stack.items.copy(),
        })

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps