class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val = image[sr][sc]
        def dfs(image, r, c, visit):
            row, col = len(image), len(image[0])
            if min(r,c) < 0 or r == row or c == col or (r,c) in visit or image[r][c] != val:
                return

            visit.add((r,c))
            image[r][c] = color
            dfs(image, r+1, c, visit)
            dfs(image, r-1, c, visit)
            dfs(image, r, c+1, visit)
            dfs(image, r, c-1, visit)

            visit.remove((r,c))

            return
        dfs(image, sr, sc, set())
        return image

