def dfs(graph, idx, visited):
    visited[idx] = True
    for i in range(len(graph[idx])):
        if graph[idx][i] == 1 and not visited[i+1]:
            dfs(graph,i+1,visited)
    return visited

def solution(n, computers):
    answer = 1
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    computers.insert(0,0)

    pointer = 1

    while True:
        visited = dfs(computers,pointer,visited)
        if False in visited:
            answer += 1
            pointer = visited.index(False)
        else:
            break

    return answer

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))