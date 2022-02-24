


# 시행착오▼
# 결국 모양들은 아래와 같은 모양이 단위체가 된다 할 수 있다
# ***
# * *
# ***
# 이런 단위체를 만들 때 마다 저장해서 늘려간다


# num = "**** ****"
# n = int(input())
# for i in range(1,len(num)+1):
#     print(num[i-1],end='')
#     if i % n == 0:
#         print()

# stars = "**** ****"
# array = []
# for i in range(9):
#     array.append(stars)
#     print(array)



# 시행착오▼
# 입력받은 수 만큼 2차원 배열은 만들어 각 인덱스들을
# 판별함수에 넣어 비었다면 = 0, 별이 있다면 = 1
# 하지만 판별한는 과정이 어려웠고 비효율적인 것 같았다
# 
#  # 비었다면 0, 별이 있다면 1을 return
# def isEmpty(i,j):
#     for c in range(m):
#         # 2 * 1 ~ 2 * 1
#         # 2 * 2 ~ 2 * 3
#         # 2 * 5 ~ 2 * 9
#         for C in range(1+((m-1)*3)):
#             if i % (3 ** m) == 2 and j % (3 ** m) == 2:
#                 return 0
#             else:
#                 return 1
#     # if i % 3 == 2 and j % 3 == 2:
#     #     return 0
#     # if (i % 9 == 4 or i % 9 == 5 or i % 9 == 6) and (j % 9 == 4 or j % 9 == 5 or j % 9 == 6):
#     #     return 0    
#     # return 1

# n = int(input())
# temp = n
# m = 0
# while 1:
#     temp /= 3
#     m+=1
#     if temp == 1:
#         break
    
# # 입력된 수 만큼 2차원 배열 생성
# array = [[0] * n for i in range(n)] 

# for i in range(n):
#     for j in range(n):
#         # 리턴값을 배열에 넣기
#         array[i][j] = isEmpty(i+1,j+1) 
#         if array[i][j]:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





