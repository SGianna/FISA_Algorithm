# 문제 : k 로프를 이용하여 중량 w를 들어올릴때 최대중량
# 제한 조건 : 
# N(1 ≤ N ≤ 100,000)개의 로프
# 로프가 버틸 수 있는 최대 중량 < 10,000, 자연수

# 제안: 
#   사용 로프가 1개 일때, max(로프 중량)
#   사용 로프가 N개 일때, max(오름차순(로프 중량)*N)

n = int(input())

list1 = []
for i in range(n):
    list1.append(int(input()))

list1.sort(reverse=True)
for i in range(n):
    list1[i] = list1[i]*(i+1)

print(max(list1))