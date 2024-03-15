def count_stars(image):
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or image[x][y] == '-':
            return
        image[x][y] = '-'
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                dfs(x + dx, y + dy)

    count = 0
    for i in range(m):
        for j in range(n):
            if image[i][j] == '#':
                dfs(i, j)
                count += 1
    return count


def main():
    case = 1
    while True:
        try:
            m, n = map(int, input().split())
            image = [list(input()) for _ in range(m)]
            stars = count_stars(image)
            print(f"Case {case}: {stars}")
            case += 1
        except EOFError:
            break


if __name__ == "__main__":
    main()
