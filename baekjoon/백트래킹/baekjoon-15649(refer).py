# https://intrepidgeeks.com/tutorial/bojun-15649-n-and-m-1-python-with-back-tracking
# 백트래킹이란 조건이 만족하는 모든 경우의 수를 찾는 것이다
# 그래서 DFS(깊이 우선 탐색), BFS(너비 우선 탐색), Best First Search등이 있고
# 이 코드에서는 DFS를 사용했다
# 
# m으로 자리수를 정해놓고 각 자리에 들어가는 수는 중복되지 않는다
# => ((1, 2), (1, 3), (1, 4)) => (1, 1)은 불가능 하다.
# 
# 자리 수가 두 개인 경우는 이중 반복문을 통해 풀 수 있지만,
# m이 커질수록 반복문을 계속 중첩시킬 순 없다
# => 요기서 내가 가장 힘들게 생각했고, 힘들었던 것 같다
# 
# 그래서 백트래킹을 사용해야 하고 
# 조건은 이미 방문한 경우라면 제외시키면 된다
# 

n,m = map(int,input().split())
s = [] # 출력을 위한 숫자가 쌓일 스택
visited = [False] * (n+1) # ???

def dfs():
    # 출력 될 수에 따라 조건을 걸어준다
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

dfs()


# n 과 m을 입력받는데,
# m개의 두 수는 각각 n까지의 값들을 가질 수 있고
# 중복이 안 된다
# 
# 이 때의 경우의 수를 구한다
# 4, 2가 들어오면 [][] 의 중복이 되지 않는 경우의 수를 구하면 된다
# 즉, (4 * 4) - (4 * 1) = 12
# 즉, (n * n) - (n * (m - 1))
# 
# 3, 1가 들어오면 [], 3 - 0 = 3
# 
# 4, 4가 들어오면 (4 * 4 * 4 * 4) - (4 * 3) = 256 - 12 = 

# import sys
# a,b = map(int,sys.stdin.readline().split())
# for x in range(1,a+1):
#     for y in range(1,a+1):
#         for z in range()
#     print()

# import sys
# a,b = map(int,sys.stdin.readline().split())
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         for m in range(b):
#             print(i,j)
#         print()