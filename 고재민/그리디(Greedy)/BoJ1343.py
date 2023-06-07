# import sys
#
# poly = sys.stdin.readline()
# polyA = 'AAAA'
# polyB = 'BB'
# cnt = 0
# ans = []
# print(poly)
# for i in range(len(poly)):
#     if poly[i] == 'X':
#         cnt += 1
#     elif poly[i] == '.':
#         if cnt % 4 == 0:
#             ans.append(polyA*(cnt//4))
#             cnt -= 4*(cnt//4)
#             if cnt == 1:
#                 print(-1)
#                 break
#         elif cnt % 2 == 0:
#             ans.append(polyB*(cnt//2))
#             cnt -= 2*(cnt//2)
#         ans.append('.')
#     elif cnt == 4:
#         ans.append(polyA)
#     elif
#
poly = input()
poly = poly.replace("XXXX","AAAA")
poly = poly.replace("XX","BB")

if 'X' in poly:
    print(-1)
else:
    print(poly)