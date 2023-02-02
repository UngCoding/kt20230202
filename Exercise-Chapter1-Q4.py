# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = int(data[0])
for i in range(len(data)-1):
    if(result * int(data[i+1]) >= result + int(data[i+1])):
        result *=  int(data[i+1])
    else:
        result = result + int(data[i+1])


print(result)