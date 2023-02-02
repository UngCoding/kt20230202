# Q5 Answer Template
score = input()
mid = len(str(score))//2

left, right = 0, 0
for i in range(mid):
    left += int(score[i])

for i in range(mid, len(score)):
    right += int(score[i])
    
if right == left:
    print("LUCKY")
else:
    print("READY")