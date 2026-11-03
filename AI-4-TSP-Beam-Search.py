
# Distance between cities
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Calculate total distance
def cost(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance[path[i]][path[i + 1]]
    total += distance[path[-1]][path[0]]
    return total

# Generate neighboring paths
def neighbors(path):
    result = []
    for i in range(1, len(path)):
        new_path = path[:]
        new_path[0], new_path[i] = new_path[i], new_path[0]
        result.append(new_path)
    return result

# Local Beam Search
def beam_search(k):
    beam = [[0, 1, 2, 3]]

    for _ in range(5):
        candidates = []

        for path in beam:
            candidates.extend(neighbors(path))

        candidates.sort(key=cost)
        beam = candidates[:k]

    return min(beam, key=cost)

# Run the algorithm
best_path = beam_search(2)

print("Best Path:", best_path)
print("Minimum Distance:", cost(best_path))
