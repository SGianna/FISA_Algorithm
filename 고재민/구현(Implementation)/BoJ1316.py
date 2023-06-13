N = int(input())
cnt = 0

for i in range(N):
    word = input()
    ans = True
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                ans = False
                break
    if ans:
        cnt += 1
print(cnt)
