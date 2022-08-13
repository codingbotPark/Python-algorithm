# print(a.find("a")) # 문자열 중 특정 문자가 나오는 첫번째 위치
# print(a.rfind("a")) # 문자열 중 특정 문자가 나오는 마지막번재 위치

str = input()
num = str.count("c=")
num += str.count("c-")
num += str.count("dz=") 
num += str.count("d-") 
num += str.count("lj") 
num += str.count("nj") 
num += str.count("s=") 
num += str.count("z=")
num += (len(str) - (2 * num))
print(num)
