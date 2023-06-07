n = int(input())
ans = []
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(1,n+1):
    ans.append((rope[i-1])*i)

print(max(ans))