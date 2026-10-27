NAME = "Hash Table"
TYPE = "sort"


class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))
        return index

    def search(self, key):
        index = self._hash(key)
        for item_key, item_value in self.table[index]:
            if item_key == key:
                return index, item_value
        return None, None

    def delete(self, key):
        index = self._hash(key)
        for i, (item_key, _) in enumerate(self.table[index]):
            if item_key == key:
                del self.table[index][i]
                return True
        return False

    def to_list(self):
        values = []
        for bucket in self.table:
            for _, value in bucket:
                values.append(value)
        return values


def run(numbers, target=None):
    steps = []
    data = list(numbers)
    table = HashTable(max(8, len(data) * 2))

    for value in data:
        index = table.insert(value, value)
        steps.append({
            "type": "compare",
            "index": index,
            "array": table.to_list(),
        })

    if target is not None:
        index, value = table.search(target)
        if index is not None:
            steps.append({
                "type": "found",
                "index": index,
                "array": table.to_list(),
            })
        else:
            steps.append({
                "type": "not_found",
                "array": table.to_list(),
            })
    elif data:
        key = data[-1]
        table.delete(key)
        steps.append({
            "type": "swap",
            "index1": table._hash(key),
            "index2": table._hash(key),
            "array": table.to_list(),
        })

    steps.append({
        "type": "finished",
        "array": table.to_list(),
    })

    return steps
