#!/usr/bin/env python3


def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    points = []
    for [a, b] in ab:
        points.append(b)
        points.append(a - b)

    points.sort()
    points.reverse()

    ans = sum(points[:k])
    print(ans)


if __name__ == "__main__":
    main()
