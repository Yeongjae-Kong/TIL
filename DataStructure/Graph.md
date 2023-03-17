# Graph란?

<br/>

그래프란 정점(Vertex)와 간선(Edge)을 모아놓은 자료구조입니다.

그래프는 사이클이 가능하고, 방향 그래프와 무방향 그래프가 모두 존재합니다.

이러한 점에서 그래프가 트리 구조의 상위 집합 개념이라 볼 수 있습니다.

<img src="https://blog.kakaocdn.net/dn/ceAVKK/btr4aL5e79e/pQwu4lc93RY3DbCYKFEMkk/img.png"/>

무방향 그래프에서 하나의 정점에 인접한 정점의 수를 차수(degree)라고 하며,

간선에 의해 직접 연결된 정점을 인접 정점(adjacent vertex)라고 합니다.

이러한 정점들을 지나는 경로가 같은 간선을 지나지 않을 때, 단순 경로(simple path)라고 합니다.(0 > 1 > 2 > 3)

<br/>

그래프는 방향 그래프/무방향 그래프 외에도 간선에 가중치를 넣어 정점 이동 시 비용을 부과하는 가중치 그래프,

모든 정점에 경로가 존재하는 연결 그래프와 특정 정점에 경로가 존재하지 않는 비연결 그래프,

모든 정점이 연결되어 있으면서 트리의 속성을 만족하는 신장트리(Spanning Tree)와 신장트리의 가중치 합이 최소인 최소신장트리(MST) 등이 있습니다.

MST는 Greedy Algorithm인 kruskal Algorithm으로 구현할 수 있습니다.

<br/>

# Graph의 구현

<br/>

그래프는 인접행렬과 인접리스트 두 방식으로 구현할 수 있습니다.


- 인접행렬


Vertex가 Edge로 직접 연결되어있으면 1, 그렇지 않으면 0인 2차원 배열을 통해 그래프를 구현합니다.

<img src="https://blog.kakaocdn.net/dn/LakX6/btr4gEGu4Wu/KO5sBCYPDFutGKreVfgTgK/img.png"/>

- 인접그래프