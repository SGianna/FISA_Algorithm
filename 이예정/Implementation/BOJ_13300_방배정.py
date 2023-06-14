# https://www.acmicpc.net/problem/13300 
#문제 :  1학년부터 6학년까지 학생들이 묵을 방을 배정
# 남학생은 남학생끼리, 여학생은 여학생끼리
# 한 방에는 같은 학년의 학생들을 배정해야 한다.
# 한 방에 한 명만 배정하는 것도 가능
# 제한 조건 : 
# 참가 학생 수 : 정수 N (1 ≤ N ≤ 1,000)
# 한 방에 배정할 수 있는 최대 인원 수 : K(1 < K ≤ 1,000)
# 성별 S 는 0 (여학생), 1 (남학생), 학년 Y(1 ≤ Y ≤ 6)
# 제안: 
#학년을 키로 가지고 성별을 value로 하는 dictionary 
# 인풋이 추가 될때마다 dic 내 value에 문자열 추가 
# 마지막에 학년별 0,1 를 세서 배정 가능한 수로 나누기 


import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

dict = {}
for _ in range(N):
    gender, grade = sys.stdin.readline().rstrip().split()
    
    if grade in dict:
        dict[grade] = dict.get(grade) + gender 
    else :
        dict[grade] = gender

# 방 배정
result = 0
for key in dict:
    boy = dict[key].count('1')
    girl = dict[key].count('0')

    result += int(boy / K)
    if  boy % K != 0:
        result += 1
    
    result += int(girl / K)
    if  girl % K != 0:
        result += 1
        
print(result)