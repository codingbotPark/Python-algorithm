from xml.etree.ElementTree import C14NWriterTarget


a,b,c = map(int,input().split())
A = a + b
B = a % c
C = b % c
D = a * b
print(A%c)
print((B + C) % c)
print(D % c)
print((B * C)%c)