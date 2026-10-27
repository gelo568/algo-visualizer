NAME = "Linear Search"
TYPE = "search"


def run(numbers, target):
    steps = []
    data = numbers.copy()

    for index, value in enumerate(data):
        steps.append({
            "type": "compare",
            "index": index,
            "array": data.copy()
        })

        if value == target:
            steps.append({
                "type": "found",
                "index": index,
                "array": data.copy()
            })
            return steps

    steps.append({
        "type": "not_found",
        "array": data.copy()
    })

    return steps