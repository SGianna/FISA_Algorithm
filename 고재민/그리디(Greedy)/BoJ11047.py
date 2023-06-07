import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
cnt = 0
for _ in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))

for i in reversed(range(N)):
    cnt += K//coin[i]
    K = K%coin[i]

print(cnt)
