# Q0 Answer template
import math

def solution(a, b):
    n = min(a,b)
    for i in range(n):
        if(a%(i+1) == 0 and b%(i+1) ==0):
            answer = i+1
    return answer

a,b = map(int, input().split())

c = solution(a,b)
print(c)


# Q1 Answer template

def solution(a, b):
    answer = -1
    return answer

c = solution(a,b)
print(c)