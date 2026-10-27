NAME = "Factorial"
TYPE = "sort"


def _factorial(n, steps):
    steps.append({
        "type": "compare",
        "index": n,
        "array": [n],
    })
    if n <= 1:
        return 1
    return n * _factorial(n - 1, steps)


def run(numbers):
    steps = []
    value = int(numbers[0]) if numbers else 0
    value = max(0, value)

    result = _factorial(value, steps)
    steps.append({
        "type": "finished",
        "array": [result],
    })
    return steps
