# <연습문제2>
# 8*8 평면 글자판에서 제시된 길이 만큼의 회문(거꾸로 읽어도 똑같은 문장이나 낱말)의 개수를 구해라

# 4
# CBBCBAAB
# CCCBABCB
# BAAAACAB
# BACCCCAC
# AABCBBAC
# ACAACABC
# BCCBAABC
# ABBBCCAA





N = int(input())
total = 0
txt = [list(input()) for _ in range(8)]
    
for i in range(8):
    for j in range(8-N+1): # 회문을 확인하는 구간의 첫 글자 인덱스

        for k in range(N//2): # 회문의 길이 절반만큼 비교

            if txt[i][j+k] != txt[i][j+N-1-k]:
                break # 비교 글자가 다르면 현재구간 중지

        else: #break없이 걸리지 않고 for문 종료
            total += 1
for i in range(8):
    for j in range(8-N+1): # 회문을 확인하는 구간의 첫 글자 인덱스

        for k in range(N//2): # 회문의 길이 절반만큼 비교

            if txt[j+k][i] != txt[j+N-1-k][i]:
                break # 비교 글자가 다르면 현재구간 중지

        else: #break없이 걸리지 않고 for문 종료
            total += 1
    

print(total)
# 12