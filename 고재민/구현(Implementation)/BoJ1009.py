n = int(input())
num = 0
for i in range(n):
    a, b = map(int, input().split())
    a = a % 10
    if a == 1 and a == 5 and a == 6:
        print(a[-1])
    elif a == 4 and a == 9:
        ans = b%2
        num = str(a ** ans)
        print(num[-1])
    elif a == 0:
        print(10)
    else:
        ans = b%4
        num = str(a ** ans)
        print(num[-1])
#
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     aa = a % 10
#     if aa == 0:
#         print(10)
#     elif aa in [1,5,6]:
#         print(aa)
#     elif aa in [4,9]:
#         bb = b%2
#         if bb == 0:
#             print(aa*aa%10)
#         else:
#             print(aa)
#     else:
#         bb = b%4
#         if bb == 0:
#             print(aa**4%10)
#         else:
#             print(aa**bb%10)