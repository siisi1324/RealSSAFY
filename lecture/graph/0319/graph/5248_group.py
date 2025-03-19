def initialize_groups(member_count):
    # 각 멤버를 자신을 대표자로 초기화
    group_leader = [i for i in range(member_count + 1)]
    return group_leader


def find_leader(member):
    if group_leader[member] == member:
        return member
    # 경로 압축을 수행하여 대표자를 바로 설정
    group_leader[member] = find_leader(group_leader[member])
    return group_leader[member]


def merge_groups(member_a, member_b):
    leader_a = find_leader(member_a)
    leader_b = find_leader(member_b)

    if leader_a == leader_b:
        return  # 이미 같은 그룹

    # 대표자가 작은 번호를 우선으로 설정
    if leader_a < leader_b:
        group_leader[leader_b] = leader_a
    else:
        group_leader[leader_a] = leader_b


# 테스트 케이스 개수
num_tests = int(input())
for test_case in range(1, num_tests + 1):
    num_members, num_pairs = map(int, input().split())
    pair_data = list(map(int, input().split()))  # 멤버 간의 연결 정보
    group_leader = initialize_groups(num_members)

    # 입력받은 데이터로 그룹 병합
    for idx in range(0, len(pair_data), 2):
        merge_groups(pair_data[idx], pair_data[idx + 1])

    # 고유한 그룹 개수 세기
    unique_groups = 0
    for member in range(1, num_members + 1):  # 1번부터 시작 (0번 인덱스 사용 X)
        if find_leader(member) == member:
            unique_groups += 1

    print(f"#{test_case} {unique_groups}")