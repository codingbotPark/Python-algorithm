



# # 빼는 데 2초가 걸리기 때문에 추가를 다 해주고 하는게 좋을 것 같다
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