# Q1 Answer template

def solution(a, b):
    n = max(a,b)
    for i in range(a*b, max(a,b) - 1, -1):
        if(i%a == 0 and i%b == 0 ):
            answer = i
    return answer

a,b = map(int, input().split())

c = solution(a,b)
print(c)