## 배열을 사용한 풀이
# def solution(phone_book):
#     answer = True
    
#     print(phone_book)

#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]) and i != j:
#                 answer = False
#     return answer

def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range((len(phone_book))-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False

    return answer

print(solution(["119", "97674223", "1195524421"]))