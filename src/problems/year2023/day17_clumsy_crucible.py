from collections import defaultdict
from heapq import heappop, heappush
from math import inf


def clumsy_crucible(cities: list[list[int]]):
    return dijkstra(grid=cities, min_consecutive=1, max_consecutive=3), dijkstra(
        grid=cities, min_consecutive=4, max_consecutive=10
    )


def dijkstra(grid: list[list[int]], min_consecutive: int, max_consecutive: int) -> int:
    distances = defaultdict(lambda: inf)
    heap = [(0, (0, 0, (0, 1))), (0, (0, 0, (1, 0)))]

    while heap:
        cost, (idx_row, idx_column, node) = heappop(heap)

        # Reached end of grid
        if (idx_row, idx_column) == (len(grid) - 1, len(grid[0]) - 1):
            return cost

        if cost > distances[idx_row, idx_column, node]:
            continue

        di, dj = node
        for ndi, ndj in ((-dj, di), (dj, -di)):
            node_cost = cost
            for depth in range(1, max_consecutive + 1):
                ni, nj = idx_row + ndi * depth, idx_column + ndj * depth
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    node_cost += grid[ni][nj]
                    if depth < min_consecutive:
                        continue
                    k = (ni, nj, (ndi, ndj))
                    if node_cost < distances[k]:
                        distances[k] = node_cost
                        heappush(heap, (node_cost, k))
    return -1
