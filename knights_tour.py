"""
knight's tour problem
the knight's tour problem is a classic problem in graph theory and combinatorial optimization.
the objective is to find a sequence of moves of a knight on a chessboard such that the knight visits every square exactly once.

functions:
- knights_tour(n: int, start_x: int = 0, start_y: int = 0) -> Optional[List[Tuple[int, int]]]
knights_tour: Find a knight's tour on an n x n chessboard starting from (start_x, start_y).

"""

from typing import List, Tuple, Optional

def is_valid_move(x: int, y: int, n: int, visited: List[List[bool]]) -> bool:
    return 0 <= x < n and 0 <= y < n and not visited[x][y]

def knights_tour(n: int, start_x: int = 0, start_y: int = 0) -> Optional[List[Tuple[int, int]]]:
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    def count_onward_moves(x: int, y: int, visited: List[List[bool]]) -> int:
        count = 0
        for dx, dy in moves:
            if is_valid_move(x + dx, y + dy, n, visited):
                count += 1
        return count

    def backtrack(x: int, y: int, move_count: int, path: List[Tuple[int, int]], visited: List[List[bool]]) -> bool:
        if move_count == n * n:
            return True

        next_moves = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, n, visited):
                onward_moves = count_onward_moves(nx, ny, visited)
                next_moves.append((onward_moves, nx, ny))

        next_moves.sort()  # Sort by number of onward moves (Warnsdorf's rule)

        for _, nx, ny in next_moves:
            visited[nx][ny] = True
            path.append((nx, ny))
            if backtrack(nx, ny, move_count + 1, path, visited):
                return True
            visited[nx][ny] = False
            path.pop()

        return False

    visited = [[False] * n for _ in range(n)]
    visited[start_x][start_y] = True
    path = [(start_x, start_y)]

    if backtrack(start_x, start_y, 1, path, visited):
        return path
    else:
        return None
    
# Example usage:
if __name__ == "__main__":
    n = 5
    tour = knights_tour(n)
    if tour:
        print("Knight's Tour found:")
        board = [[0] * n for _ in range(n)]
        for move_number, (x, y) in enumerate(tour, start=1):
            board[x][y] = move_number
        for row in board:
            print(' '.join(f"{cell:2}" for cell in row))
    else:
        print("No Knight's Tour found.")