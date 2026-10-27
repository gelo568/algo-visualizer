NAME = "Quick Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = list(numbers)

    def quick_sort(arr, low, high):
        if low >= high:
            return

        pivot_index = high
        pivot_value = arr[pivot_index]
        smaller_index = low

        for current_index in range(low, high):
            steps.append({
                "type": "compare",
                "index1": current_index,
                "index2": pivot_index,
                "pivot": pivot_index,
                "array": arr.copy()
            })

            if arr[current_index] < pivot_value:
                if smaller_index != current_index:
                    arr[smaller_index], arr[current_index] = (
                        arr[current_index], arr[smaller_index]
                    )
                    steps.append({
                        "type": "swap",
                        "index1": smaller_index,
                        "index2": current_index,
                        "array": arr.copy()
                    })

                smaller_index += 1

        if smaller_index != high:
            arr[smaller_index], arr[high] = arr[high], arr[smaller_index]
            steps.append({
                "type": "swap",
                "index1": smaller_index,
                "index2": high,
                "array": arr.copy()
            })

        quick_sort(arr, low, smaller_index - 1)
        quick_sort(arr, smaller_index + 1, high)

    if len(data) > 1:
        quick_sort(data, 0, len(data) - 1)

    steps.append({
        "type": "finished",
        "array": data.copy()
    })

    return steps