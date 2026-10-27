NAME = "Queue"
TYPE = "sort"


class Queue:
    def __init__(self, values=None):
        self.items = []
        if values is not None:
            for value in values:
                self.enqueue(value)

    def enqueue(self, value):
        self.items.append(value)
        return value

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)


def run(numbers):
    steps = []
    queue = Queue()
    data = list(numbers)

    for value in data:
        queue.enqueue(value)
        steps.append({
            "type": "compare",
            "index": len(queue.items) - 1,
            "array": queue.items.copy(),
        })

    while not queue.is_empty():
        queue.dequeue()
        steps.append({
            "type": "swap",
            "index1": 0,
            "index2": max(0, len(queue.items) - 1),
            "array": queue.items.copy(),
        })

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps
