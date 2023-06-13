t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    ans = str(a**b)
    print(ans[-1])