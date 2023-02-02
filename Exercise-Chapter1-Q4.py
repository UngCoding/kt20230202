# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = int(data[0])
print(data[0], end='')
for i in range(len(data)-1):
    if(result * int(data[i+1]) >= result + int(data[i+1])):
        result *=  int(data[i+1])
        print( " X " + data[i+1], end = '')
    else:
        result += int(data[i+1])
        print(" + " + data[i+1], end = '')

print(" = " + str(result))