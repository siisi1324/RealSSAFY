N = int(input())

arr = list(range(1, N+1))



















































# N = int(input())
# for i in range(1, N+1):
#     I = str(i)
#     for j in I:
#         if j in ['3', '6', '9']:
#             print(f'-', end='')
#         else:
#             print(f'{j}', end=' ')
#
# # ===============================================
# 남의 것...
#
# n = int(input())
#
# arr = list(range(1, n + 1))
# # 그러게..리스트로 만들면 되는건데 바뷰..
# for i in arr:
#     cnt = 0
#     for j in str(i):
#         if j == '3':
#             cnt += 1
#         if j == '6':
#             cnt += 1
#         if j == '9':
#             cnt += 1
#     # 갯수만 따로 카운킹해서
#     if cnt > 0:
#         print('-' * cnt, end=" ")
#     # 이런식으로 하니까 띄우기 문제도 없어지고..
#     else:
#         print(i, end=" ")
#     # 좋네요...