# Splay tree란?
 
</br>
Splay tree는 이진검색트리(Binary Search Tree)의 한 종류로, 다른 BST(AVL tree, R-B tree 등)보다 구현이 쉽고, 연산을 amortized O(logn)의 시간복잡도로 수행할 수 있습니다. amortized O notation은 일반적으로 사용되는 big-O notation과 달리, 시간 복잡도를 실행 시간의 상한 점근이 아닌, 최악의 경우에 대한 해당 연산의 평균 시간복잡도를 나타냅니다. 따라서 최악의 경우에서 연산 시간복잡도가 O(logn)임을 보장한다는 의미라고 생각하시면 됩니다.

Splay tree는 삽입, 삭제, 검색의 연산을 수행한 뒤, splay를 통해 최근에 접근한 노드를 루트에 위치시켜 트리를 재구성합니다. 즉, 자주 탐색하는 키를 가진 노드를 루트에 가깝게 위치하도록 구성하여 연산의 효율성을 높인 트리입니다.

</br>

# Splay tree의 원리
 </br>

Splay tree는 연산이 발생한 후 Splay라는 rotate 연산을 통해 트리의 균형을 맞춥니다.

삽입 시에는 새로 삽입한 노드, 검색 시에는 해당 노드를 splay합니다. 삭제시에는 삭제한 노드의 양쪽 subtree가 분리되므로, 분리된 left subtree의 rightmost element(가장 큰 원소)를 찾은 뒤 이것의 right child로 right subtree를 붙인 뒤 rightmost element를 루트 노드로 splay하여 두 subtree를 연결합니다.

 </br>

Splay는 아래의 세 경우가 있습니다. x를 대상 노드, p를 부모 노드, g를 부모의 부모 노드라 칭하겠습니다.
 
 </br>

1. x가 p만 가지고 있을 때 zig step

2. x와 p가 둘다 왼쪽 혹은 오른쪽 자식 노드일 경우 zig-zig step

3. x와 p가 서로 다른 방향으로 자식 노드일경우 zig-zag step

 </br>

각 step은 AVL tree의 rotate연산과 같습니다. 단, zig-zig step에서는 single rotation이 가운데 노드가 아닌 가장 하위의 자식 노드부터 rotation이 시작된다는 점만 다릅니다.

rotate 연산은 BST의 일종인 AVL tree를 설명한 아래 글에서 확인하실 수 있습니다.

https://yeongjaekong.tistory.com/35

 </br>

# Splay tree의 활용
 
</br>

따라서 Splay tree는 최근에 접근한 노드를 루트로 옮기는 특성을 잘 활용할 수 있는 분야에서 사용됩니다.

아래와 같은 예시가 있습니다.

 </br>

- 캐시 관리: 최근에 접근한 데이터에 빠르게 액세스할 수 있음.

- 네트워크 라우팅: IP 라우팅 테이블에서 자주 사용되는 항목에 대해 빠르게 업데이트하고 관리하는데 사용될 수 있음.

- 자동 완성 및 검색 엔진: 가장 일치하는 항목을 빠르게 찾을 수 있음.