# # 배열을 사용한 코드
# def solution(participant, completion):
#     for i in completion:
#         del participant[participant.index(i)]
#     return "".join(participant)
# hash를 사용한 코드
def solution(participant, completion):
    hash = {}
    # hash에 담기
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:    
            hash[i] = 1

    for i in completion:
        if i in hash:
            hash[i] -= 1
            if hash[i] == 0:
                del hash[i]
    
    return "".join(hash)


# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))


## 콜렉션 사용 예시
# from collections import Counter
# string = "hello world"
# counter = Counter(string)
# print(counter)
# print(list(counter)[-1])


## 콜렉션 모듈을 사용한 풀이
# import collections
# def solution(participant, completion):
#     answer = (collections.Counter(participant) - collections.Counter(completion))
#     print(list(answer.keys())[0])
# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))