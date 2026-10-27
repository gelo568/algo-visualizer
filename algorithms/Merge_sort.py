NAME = "Merge Sort"
TYPE = "sort"


def _merge_sort_steps(data, left, right):
    steps = []

    if left >= right:
        return steps

    middle = (left + right) // 2
    steps.extend(_merge_sort_steps(data, left, middle))
    steps.extend(_merge_sort_steps(data, middle + 1, right))

    left_part = data[left:middle + 1]
    right_part = data[middle + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        steps.append({
            "type": "compare",
            "index1": left + i,
            "index2": middle + 1 + j,
            "array": data.copy()
        })

        if left_part[i] <= right_part[j]:
            value = left_part[i]
            i += 1
        else:
            value = right_part[j]
            j += 1

        data[k] = value
        steps.append({
            "type": "swap",
            "index1": k,
            "index2": k,
            "array": data.copy()
        })
        k += 1

    while i < len(left_part):
        data[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        data[k] = right_part[j]
        j += 1
        k += 1

    return steps


def run(numbers):
    steps = []
    data = numbers.copy()
    steps.extend(_merge_sort_steps(data, 0, len(data) - 1))
    steps.append({
        "type": "finished",
        "array": data.copy()
    })
    return steps