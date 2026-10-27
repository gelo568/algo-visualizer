NAME = "Linked List"
TYPE = "sort"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return node

    def delete(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return True
            current = current.next

        return False

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def __len__(self):
        return len(self.to_list())


def run(numbers):
    steps = []
    linked = LinkedList()
    data = list(numbers)

    for value in data:
        linked.insert(value)
        steps.append({
            "type": "compare",
            "index": len(linked.to_list()) - 1,
            "array": linked.to_list(),
        })

    if data:
        linked.delete(data[0])
        steps.append({
            "type": "swap",
            "index1": 0,
            "index2": max(0, len(linked.to_list()) - 1),
            "array": linked.to_list(),
        })

    steps.append({
        "type": "finished",
        "array": linked.to_list(),
    })

    return steps
