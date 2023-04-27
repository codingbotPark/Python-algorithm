# def solution1(data,d,k):
#     for i in range(len(data) - 1):
#         if (abs(data[i] - data[i+1]) <= d) and k > 0 and i != 0:
#             data[i] = ''
#             k -= 1
#     return list(filter(None,data))

# print(solution1([2,4,7,1,2,4,6],3,3))

def solution2(data, d, k):
    pointer = 0
    for i in range(1,len(data) -1):
        print(data)
        if (abs(data[pointer] - data[i]) <= d) and k > 0:
            data[i] = '' 
            k -= 1
        else:
            pointer = i
            print("move pointer",pointer)

    return list(filter(None,data)) 

print(solution2([2,4,7,1,2,4,2,2,2,2,2,6],3,3))

def solution22(data, d, k):
    while len(data) >= 2 or k > 0:
        if abs(data[0] - data[1]) <= d:
            del data[1]
            k -= 1
        else:
            break
    print(data)
# print(solution22([2,4,7,1,2,4,6],3,3))


## ------------------------




## ------------------------

# def solution3(data,d,k):
