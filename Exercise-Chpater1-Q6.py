# Q6 Answer template

def solution(n):
    
    for i in range(n+1):
        if i * i == n:
            answer = (i+1) * (i+1)
            break
        answer = -1
    return answer

n = int(input())
print(solution(n))