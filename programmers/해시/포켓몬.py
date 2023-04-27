def solution(nums):
    numsLength = len(nums)
    settedNums = set(nums)
    if (len(settedNums) < numsLength / 2):
        answer = len(settedNums)
    else:
        answer = numsLength / 2

    return answer