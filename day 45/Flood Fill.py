class Solution(object):
    def floodFill(self, image, sr, sc, color):
        row = len(image)
        col = len(image[0])
        original = image[sr][sc]

        if original == color:
            return image

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col:
                return

            if image[r][c] != original:
                return

            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image