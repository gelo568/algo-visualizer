NAME = "Graph"
TYPE = "sort"


def run(numbers):
    steps = []
    adjacency = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2],
    }
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        steps.append({
            "type": "compare",
            "index": node,
            "array": sorted(visited),
        })

        for neighbor in adjacency.get(node, []):
            if neighbor not in visited:
                steps.append({
                    "type": "swap",
                    "index1": node,
                    "index2": neighbor,
                    "array": sorted(visited),
                })
                dfs(neighbor)

    start = int(numbers[0]) if numbers else 0
    start = start % 4
    dfs(start)

    steps.append({
        "type": "finished",
        "array": sorted(visited),
    })

    return steps
