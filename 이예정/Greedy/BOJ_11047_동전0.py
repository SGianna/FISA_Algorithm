# 문제 : 동전 종류 N, 가치의 합 K, 각 동전의 가치 A
# 제한 조건 : 
#   1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000
#   1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수
# 제안: 
# N/2 위치의 동전 가치와 K를 비교
# K = K%N 
# K가 0이 될때까지
#### N 종류가 많지 않으므로 내림차순 정렬된 동전 iterative 검색으로 변경


N, K = map(int, input().split()) #int func, iteratable variables

coins = []

for _ in range(N):
    coins.append(int(input()))

n = N-1
result = 0

while K != 0 :
    if K < coins[n] : 
        n -= 1
    elif K >= coins[n] :
        result += K // coins[n] #파이썬에서 몫 구하기 : //
        K %= coins[n]
        n -= 1
        
print(result)    
        
