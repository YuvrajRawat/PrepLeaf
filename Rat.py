import copy
import random

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

def find_path(maze, start, end):
    def dfs(x, y):
        visited[x][y] = True

        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 1 and not visited[nx][ny]:
                path.append((nx, ny))
                if dfs(nx, ny):
                    return True
                path.pop()

        return False

    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    path = [start]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if dfs(*start):
        return path
    else:
        return None

def generate_maze(n):
    maze = [[random.choice([0, 1]) for _ in range(n)] for _ in range(n)]
    maze[0][0] = 1
    maze[n - 1][n - 1] = 1
    return maze

def main():
    n = int(input("Enter the size of the maze (n x n): "))
    maze = generate_maze(n)
    start = (0, 0)
    end = (n - 1, n - 1)

    print("\nGenerated Maze:")
    print_maze(maze)

    while True:
        print("\n1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the game")

        choice = int(input("Enter the choice (1/2/3): "))

        if choice == 1:
            solution = find_path(copy.deepcopy(maze), start, end)
            if solution:
                for x, y in solution:
                    maze[x][y] = "+"
                print("\nSolution Path:")
                print_maze(maze)
            else:
                print("\nNo path exists.")
        elif choice == 2:
            maze = generate_maze(n)
            print("\nGenerated Maze:")
            print_maze(maze)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
