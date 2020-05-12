# https://leetcode.com/problems/flood-fill/
# Solved Date: 20.05.12.

import collections


class Solution:
    def flood_fill(self, image, sr, sc, newColor):
        visit = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        queue = collections.deque()
        queue.append((sr, sc, image[sr][sc]))
        visit[sr][sc] = True
        image[sr][sc] = newColor
        while queue:
            y, x, color = queue.popleft()
            for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < len(image) and 0 <= new_x < len(image[0]):
                    if not visit[new_y][new_x] and image[new_y][new_x] == color:
                        visit[new_y][new_x] = True
                        image[new_y][new_x] = newColor
                        queue.append((new_y, new_x, color))
        return image


def main():
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution.flood_fill(image, 1, 1, 2))


if __name__ == '__main__':
    main()
