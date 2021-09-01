# 선수과목
# https://www.acmicpc.net/problem/14567


def solution() :
    n, m = map(int, input().split())

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)

        indegree[b] += 1




solution()
