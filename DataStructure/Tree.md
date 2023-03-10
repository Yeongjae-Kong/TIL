# Tree란?

Tree란 노드와 브랜치를 이용하는 비선형의 자료구조로, 계층적인 구조를 표현하는데 사용됩니다.

예로 컴퓨터에서의 디렉토리 경로도 Tree 구조를 가지고 있습니다.

<br/>


# Tree 구조

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FR2RwY%2Fbtr2rDJcvxq%2FSysgFCtqf7yk1UPWP9kvgK%2Fimg.png"/>

위 그림의 A, B 등을 각각 노드라 칭하고, 상위 계층의 노드가 없는 A 노드를 루트 노드라 합니다.

A-B / B-E와 같이 수직 관계를 가지는 노드를 각각 부모 노드, 자식 노드라 하며

같은 부모를 가지는 B-C / E-F 등을 형제 노드라 부릅니다.

각 노드를 연결하는 선을 브랜치(혹은 엣지)라고 부릅니다.

Tree에서 노드 Depth는 루트에서 해당 노드까지 거치는 edge의 수를 의미합니다.

노드 Level은 특정 Depth를 가지는 집합 (Level 1 = {B, C})을 의미합니다.

노드 Degree는 자식 노드의 개수를 의미하며

이와 별개로 트리 Degree는 노드 중 가장 큰 Degree를 의미합니다. 

<br/>

트리는 vertex와 edge의 집합으로 구성된 그래프 자료구조의 일종이라 볼 수 있는데,

그래프 중에서도 서로 다른 두 노드를 연결하는 길이 하나뿐인, 그래프의 하위 집합이라 할 수 있습니다.

<br/>

트리 구조는 사이클이 존재할 수 없는데, 자식 노드에서 다른 노드를 거쳐 부모 노드로 순회할 수 없다는 뜻입니다.

또한 Edge가 자기 자신을 향하는 Self loop이 존재해선 안됩니다.

<br/>

# Tree의 종류

Tree의 종류로는 기본적으로 이진트리(Binary Tree)와 완전 이진트리(Completely Binary Tree),

포화 이진트리(Perfect Binary Tree), 이진 검색트리(Binary Search Tree) 등이 있습니다.

이진트리는 각 노드가 최대 2개의 자식을 갖는 트리를 의미합니다.

완전 이진트리는 노드가 왼쪽에서 오른쪽으로 채워지며,

마지막 레벨을 제외한 모든 레벨이 완전히 채워져 있는 트리를 의미합니다.

포화 이진트리는 모든 레벨의 노드가 2개의 자식으로 꽉 차있는 트리를 의미합니다.

<br/>

이진 검색트리는 이진 트리의 속성을 가지면서 아래 네가지 속성을 가져야 합니다.

<br/>

1. 이진 탐색 트리의 노드에 저장된 키는 유일합니다.

2. 부모의 키가 왼쪽 자식 노드의 키보다 커야 합니다.

3. 부모의 키가 오른쪽 자식 노드의 키보다 작아야 합니다.

4. 자식 노드의 서브트리 또한 이진 탐색 트리여야 합니다.

<br/>

따라서 이진 검색트리는 아래와 같은 구조를 가지게 됩니다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbbo2Aj%2Fbtr2vUqPuex%2Ftg5SokTaukQg5q1rgDJgok%2Fimg.png"/>


이러한 속성을 가지는 이유는 이진 검색트리가 탐색의 효율성을 높이기 위해 고안되었기 때문입니다.


심화적으로 Red-Black Tree나 B+ Tree, B- Tree 등이 있지만 차후 서술하도록 하겠습니다.

<br/>

# Tree의 순회

트리에는 각 노드를 체계적으로 탐색하기 위해 고안된 순회 방법이 있습니다.

<br/>

- 중위 순회 (inorder)

왼쪽 서브 트리 > 루트 노드 > 오른쪽 서브 트리 순서로 탐색이 이루어집니다.

루트 노드를 기준으로 왼쪽 서브 트리를 따라 계속 내려가다, 왼쪽 자식 노드를 가지고 있지 않은 노드부터 재귀적으로 탐색을 시작합니다.

이때, 서브 트리의 왼쪽 노드를 거친 뒤 부모 노드를 거친 후 오른쪽 자식 노드를 탐색하는데,

이또한 재귀적으로 오른쪽 자식 노드의 서브트리를 중위 순회로 탐색해야 합니다. 

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FceUNh9%2Fbtr2vosajCc%2FfVguCAZkgZLRB3XHrnVzJ1%2Fimg.png"/>

해당 트리를 중위 순회 시 A > B > C > D > E > F > G > H > I 로 출력하게 됩니다.

<br/>

- 전위 순회 (preorder)

루트노드 > 왼쪽 서브트리 > 오른쪽 서브트리 순서로 탐색이 이루어집니다.

중위 순회의 방식과 마찬가지로 재귀적으로 이루어집니다.

<br/>

- 후위 순회 (postorder)

왼쪽 서브트리 > 오른쪽 서브트리 > 루트노드 순서로 탐색이 이루어집니다.

중위 순회의 방식과 마찬가지로 재귀적으로 이루어집니다.

<br/>

# Tree의 활용

Tree 자료구조는 왜 필요할까요?

만약 데이터가 정렬되어있지 않다면 필요한 데이터를 찾을 때 값을 모두 스캔해야 합니다.

하지만 Tree와 같이 정렬되어 있다면 데이터를 효율적으로 찾을 수 있습니다.

즉, 데이터를 탐색하는데 더욱 포커싱된 자료구조라고 볼 수 있습니다.

오라클에서도 이같은 인덱싱 기법으로 데이터를 찾고 있습니다.


또한 Tree는 자료구조의 한 종류인 Heap을 구현하는 방법 중 하나로도 쓰일 수 있습니다.


<br/>
 

# Tree의 예제

https://www.acmicpc.net/problem/1068

자식 노드의 개수가 0인 노드를 리프 노드라 합니다.

해당 문제는 트리에서 특정 노드를 지웠을 때 리프 노드의 개수를 출력하는 문제입니다.

이 경우 DFS라 불리는 깊이 우선 탐색을 통해 노드를 전수조사하여 해결할 수 있습니다.


```python
# 백준 1068 트리
n = int(input())
tree = list(map(int, input().split()))
delete = int(input())

def check(delete):
    tree[delete] = 'x'
    for i in range(len(tree)):
        if delete == tree[i]:
            check(i) # 재귀적인 DFS 방식으로 delete의 자식 노드들을 x로 치환
check(delete)

cnt = 0
for i in range(n):
    if tree[i] != 'x' and i not in tree: # x가 아니고, i가 부모 노드가 아닐 때 = 리프
        cnt += 1

print(cnt)
```

check 함수를 통해 처음 input받은 delete index의 노드부터 재귀적으로 탐색하여 x표시 하였고,

반복문으로 x가 아님과 동시에 tree에 들어있는 부모가 아닐 때 카운트를 하도록 했습니다.