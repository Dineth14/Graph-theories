"""
Dynamic 5x5 labyrinth shortest path using BFS algorithm.
"""
from collections import deque
from typing import List, Set, Tuple

# bridge rotation logic
def bridge_rotates(time: int, position: Tuple[int, int], rows: int, cols: int) -> bool:
    perimeter = 2 * (rows + cols) - 4
    step = time % perimeter
    x, y = position

    if x == 0:
        return step < cols
    elif y == cols - 1:
        return step < cols + (rows - 1)
    elif x == rows - 1:
        return step < cols + (rows - 1) + (cols - 1)
    elif y == 0:
        return step < perimeter

    return False

# Find shortest path in labyrinth accounting changing bridges
def labyrinth_shortest_path(grid: List[List[str]]) -> Tuple[int, List[Tuple[int, int]]]:
    rows, cols = len(grid), len(grid[0])
    start = end = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'T':
                end = (r, c)

    if not start or not end:
        return -1, []
    
    # Initialize BFS
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]#right, down, left, up
    queue = deque([(start[0], start[1], 0, [(start[0], start[1])])])
    visited: Set[Tuple[int, int, int]] = set()#set of (x, y, time%2)
    visited.add((start[0], start[1], 0))

    while queue:
        x, y, time, path = queue.popleft()

        if (x, y) == end:
            return time, path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            ntime = time + 1

            if 0 <= nx < rows and 0 <= ny < cols:
                cell = grid[nx][ny]
                if cell == '#':
                    continue
                if cell == 'B' and not bridge_rotates(ntime, (nx, ny), rows, cols):
                    continue

                state = (nx, ny, ntime % 2)
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, ntime, path + [(nx, ny)]))

    return -1, []

#input
if __name__ == "__main__":

#test grid
   test_grid = [
        ['.', 'S', '#', 'B', '.'],
        ['#', '.', '#', '#', '.'],
        ['.', '.', 'B', '.', '.'],
        ['.', '#', '#', '#', 'T'],
        ['.', '.', '.', 'B', '.']
    ]
#input grid

grid: List[List[str]] = [[''] * 5 for _ in range(5)]
print("Enter the 5x5 grid row by row (use S, T, #, B, .):")
for r in range(5):
    for c in range(5):
        grid[r][c] = input().strip().split()[0]

length, path = labyrinth_shortest_path(grid)
if length != -1:
    print(f"Shortest path length: {length}")
    print(f"Path: {path}")
else:
    print("No path found.")















