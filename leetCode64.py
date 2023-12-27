class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        len_x = len(grid)
        len_y = len(grid[0])
        tag = [[float("inf") for i in range(len_y)] for k in range(len_x)]
        tag[0][0] = grid[0][0]

        for i in range(len_x):
            for j in range(len_y):
                nb = self.neighbor(i, j, len_x - 1, len_y - 1)
                if nb:
                    for x, y in nb:
                        tag[x][y] = min(tag[x][y], tag[i][j] + grid[x][y])

        return tag[len_x - 1][len_y - 1]

    def neighbor(self, curX, curY, maxX, maxY) -> list:
        ans = list()
        x = curX + 1 if curX < maxX else None
        y = curY + 1 if curY < maxY else None
        if x:
            ans.append((x, curY))
        if y:
            ans.append((curX, y))
        return ans
