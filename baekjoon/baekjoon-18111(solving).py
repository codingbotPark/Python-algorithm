# 현재 상황, 상황에 더 좋은 판단을 한다
# 1. 블록 없애기
# 2. 블록 쌓아서 평평하게 하기


# ----------------------------------
# 1. 기본 주어지는 블록 쌓고
# 2. 다 없애기
# 3. 남은 블록을 x * y 값과 비교
def checkAllSame(blocks):
    a = set(blocks)
    if (len(a) == 1):
        return True
    return False

y,x,blockNum = map(int,input().split())
blocks = []
time = 0

for i in range(y):
    for j in list(map(int,input().split())):
        blocks.append(j)


# 기본으로 주어지는 블록 쌓기
for i in range(blockNum):
    if(checkAllSame(blocks)):
        blockNum -= (i+1)
        exit()
    blocks[blocks.index(min(blocks))]+=1
    time+=1

print(blocks,time,blockNum)

# 나머지 모든 블록이 같아질 때 까지 블록 다 없애기
minestBlock = min(blocks)
for i in range(len(blocks)):
    temp = (blocks[i] - minestBlock)
    time += temp * 2
    blockNum += temp
    blocks[i] = minestBlock

print(blocks,time,blockNum)

    

# 남은 블록으로 최적화시키기
temp = blockNum // (x * y)
time -= temp * (x * y) * 2
for i in range(temp):
    for j in range(len(blocks)):
        blocks[j] += 1


print(blocks,time,blockNum)




# # ---------
# 블록을 제거하는 데에는 2초,
# 블록을 추가하는 데에는 1초가 걸리기 때문에
# # 평평해지려면 x * y 로 나누어 떨어지면 된다
# # 즉 x * y로 합이 나누어 떨어지게 만든다
# y,x,inven = map(int,input().split())
# arr = []
# for i in range(y):
#     arr += list(map(int,input().split()))

# avg = sum(arr) // (x * y)
# # 반대로 정렬해서
# # 인벤토리에 블록을 먼저 +한다
# arr.sort(reverse=True) 

# for i in range(len(arr)):
#     if arr[i] > avg:
# # 다 했을 때 이벤토리가 부족해서 평평하게 못했을 경우를 대비해 준다


# # 이렇게 하면 1초를 넘길거 같다


# # ---------
# # 최대한 블록을 쌓고(B가 최대) 나머지는 지워야 한다
# # 지운 블록을 다시 쌓을 수 있다
# y,x,inven = map(int,input().split())
# arr = []
# for i in range(y):
#     arr += list(map(int,input().split()))
    
    
# minN = min(arr)
# arr = list(map(lambda x:x - minN,arr))
# print(arr)