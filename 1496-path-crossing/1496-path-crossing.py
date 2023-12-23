class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x = 0
        y = 0

        for i in path:
            x += 1 if i == "E" else (-1 if i == "W" else 0)
            y += 1 if i == "N" else (-1 if i == "S" else 0)

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False