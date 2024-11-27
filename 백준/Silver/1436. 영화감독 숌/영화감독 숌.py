def find_end_number(N):
    count = 0
    number = 666
    
    while count < N:
        if '666' in str(number):
            count += 1
        
        if count == N:
            return number
        
        number += 1

# 입력 받기
N = int(input())

# 결과 출력
print(find_end_number(N))