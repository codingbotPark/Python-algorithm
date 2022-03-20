
case = int(input())
value = []
nums = [[0] * 2 for i in range(case)]
for i in range(case):
    nums[i][0],nums[i][1] = map(int,input().split())
    value.append(nums[i][0]+nums[i][1])
value.sort()
for i in range(case):
    for j in range(case):
        if value[i]  == nums[j][0] + nums[j][1]:
            print(nums[j][0],nums[j][1])
            print(nums)
            break
    