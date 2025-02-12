# <cs지식정도로만 이해>

# [보이어-무어 알고리즘]
# 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
# 보이어-무어 알고리즘은 패턴에 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 
# 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이만큼이 된다. 
# 일반적으로 시간복잡도 : O(n), 최악의 경우 : O(mn)



# [문자열 매칭 알고리즘 비교]

#  찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n
#  고지식한 패턴 검색 알고리즘: 수행시간 `O(mn)`
#  카프-라빈 알고리즘: 수행시간 `Θ(n)`
#  KMP 알고리즘: 수행시간 `Θ(n)`



# [빅 O,  Ω(오메가), Θ(세타) 표기법의 차이]

# ### 1. **Big-O 표기법 (O, 빅오)**

# **최악(Worst-case) 성능을 보장하는 상한(Bound)**
# 알고리즘이 수행하는 **최대 연산량**을 나타냄
# 입력 크기가 증가할 때 **얼마나 빠르게 증가할 수 있는지**를 나타냄

# 버블 정렬의 최악 시간 복잡도: **O(n²)** → 최악의 경우에도 최대 `n²`번 연산을 수행한다는 의미.
# 이진 탐색의 시간 복잡도: **O(log n)** → 최악의 경우에도 최대 `log n`번만 탐색한다는 의미.


# ### 2. **오메가 표기법 (Ω, 오메가)**

# **최소(Best-case) 성능을 보장하는 하한(Bound)**
# 알고리즘이 수행하는 **최소 연산량**을 나타냄
# 이보다 적은 연산량으로는 수행될 수 없음

# 삽입 정렬의 최선 시간 복잡도: **Ω(n)** → 입력이 이미 정렬되어 있다면 최소 `n`번의 연산만으로 끝날 수 있음.
# 선형 탐색의 최선 시간 복잡도: **Ω(1)** → 첫 번째 요소에서 찾을 수도 있음.

### 3. **세타 표기법 (Θ, 세타)**

# **상한(Bound)과 하한(Bound)이 같은 경우를 의미**
# 즉, 최악과 최선이 동일한 경우라면 **정확한 성장 속도**를 나타냄
# **O(빅오)와 Ω(오메가)이 같을 때 → Θ(세타)로 표현 가능**

# **퀵 정렬의 평균 시간 복잡도: Θ(n log n)** → 최악(O(n²))일 수도 있지만, 평균적으로 Θ(n log n) 시간 안에 동작함.
# **이진 탐색의 시간 복잡도: Θ(log n)** → 항상 `log n`번의 비교 연산을 수행하므로 최악과 최선이 동일함.