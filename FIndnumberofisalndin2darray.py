# this problem comes in Google online face to face interview on 2020 may
# given 2d matrix find the number of island in matrix where 1 count as island and = count as sea
# you can only count island in vertical and horizontal direction no croos join allowed


def numIsiland(graph):
    if graph is None:
        return 0
    row = len(graph)
    col = len(graph[0])
    island = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                dfs(graph, row, col, i, j)
                island += 1
    return island


def dfs(graph, row, col, x, y):
    if graph[x][y] == 0:
        return
    graph[x][y] = 0
    if x != 0:
        dfs(graph, row, col, x-1, y)
    if x != row - 1:
        dfs(graph, row, col, x+1, y)
    if y != 0:
        dfs(graph, row, col, x, y-1)
    if y != col-1:
        dfs(graph, row, col, x, y+1)


# test case
#graph = graph=[[1, 0, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
result = numIsiland(graph=[[1, 0, 0, 0, 0], [1, 0, 1, 0, 0], [
                    1, 1, 1, 0, 0], [0, 0, 0, 0, 0]])
print(result)
