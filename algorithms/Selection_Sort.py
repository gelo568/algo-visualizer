NAME = "Selection Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    for index in range(len(data)):
        smallest_index = index

        for current_index in range(index + 1, len(data)):
            steps.append({
                "type": "compare",
                "index1": smallest_index,
                "index2": current_index,
                "array": data.copy(),
            })

            if data[current_index] < data[smallest_index]:
                smallest_index = current_index

        if smallest_index != index:
            data[index], data[smallest_index] = (
                data[smallest_index],
                data[index],
            )
            steps.append({
                "type": "swap",
                "index1": index,
                "index2": smallest_index,
                "array": data.copy(),
            })

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps