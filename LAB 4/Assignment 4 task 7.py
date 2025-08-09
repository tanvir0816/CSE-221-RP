N, M, K = map(int, input().split())
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]
board = [[False] * (M + 1) for _ in range(N + 1)]
knights = []
for _ in range(K):
    x, y = map(int, input().split())
    knights.append((x, y))
    board[x][y] = True
found = False
for x, y in knights:
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= M and board[nx][ny]:
            print("YES")
            found = True
            break
    if found:
        break
if not found:
    print("NO")
