# 문제 : 
# 세 개의 자연수 A, B, C
# A x B x C 연산 결과 값에 각 숫자 (0~9)가 몇 번씩 쓰였는지?
# 제한 조건 : 
# 1 <= a < 100
# 1 <= b < 1,000,000
# 제안: 
# 곱 결과를 str로 변환 후, 같은 숫자 카운트

import sys

numbers = []

for i in range(3):
    numbers.append(int(sys.stdin.readline().rstrip())) 

number = str(numbers[0] * numbers[1] * numbers[2])

for i in range(10):
    print(number.count(str(int('0')+i)))