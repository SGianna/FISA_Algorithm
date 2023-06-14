# 입력 단어에서 다음 인덱스의 단어와 중복된다면 False

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
