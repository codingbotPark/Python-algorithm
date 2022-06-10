# if문에서 생각을 잘못했어서 부등호를 반대로, 내용을 반대로해서 맞춤


from collections import deque

# 입력받은 수 만큼 큐에 수를 넣어준다
command = input().split(" ")

arr = deque(range(1,int(command[0])+1))

targetNum = map(int,input().split())

# 주어진 수의 순서대로 빼야하기 때문에 targetNum의 수를
# 순서대로 만족시키면 되는데, 앞, 뒤의 수중 적은 방법을 사용해야한다

# 큐의 길이와, index함수를 사용하여 위치를 알아내서 계산!
counter = 0
for i in targetNum:
    if (len(arr) // 2) < (arr.index(i)):# 그냥 오른쪽 뒤로 이동
        while (not i == arr[0]):
            arr.appendleft(arr.pop())
            counter+=1
        arr.popleft()

    else: # 반대로 이동

        while(not(i == arr[0])): # 배열의 첫 번째가 targetNum이 아닐 때 까지
            arr.append(arr.popleft())
            counter+=1
        arr.popleft()
print(counter)