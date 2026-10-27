NAME = "Fibonacci"
TYPE = "sort"


def _fibonacci(n, steps):
    steps.append({
        "type": "compare",
        "index": n,
        "array": [n],
    })
    if n <= 1:
        return n
    return _fibonacci(n - 1, steps) + _fibonacci(n - 2, steps)


def run(numbers):
    steps = []
    value = int(numbers[0]) if numbers else 0
    value = max(0, value)

    result = _fibonacci(value, steps)
    steps.append({
        "type": "finished",
        "array": [result],
    })
    return steps
