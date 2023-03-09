# Queue란?

Queue란 한쪽 끝에서 삽입이 이루어지고 반댓쪽 끝에서 삭제가 이루어지는 형태의 자료구조로,

가장 마지막에 들어온 데이터가 가장 늦게 삭제됩니다.

이러한 구조를 선입선출, FIFO(First In First Out)이라 합니다.

Queue는 enQueue(item)와 deQueue()로 데이터의 삽입 및 삭제가 가능합니다.

<br/>


처음 요소를 front, 마지막 요소를 rear라 칭하며

Qpeek()을 통해 front 요소를 삭제하지 않은 채로 return 할 수 있습니다.

Array나 Linkedlist를 통해 Queue를 구현할 수 있습니다.

<br/>

# Queue의 종류

Queue의 종류로는 선형 Queue와 원형 Queue가 있습니다.

위에서 설명한 것이 일반적으로 말하는 선형 Queue입니다.

하지만 선형 Queue는 문제가 하나 있습니다.

deQueue 실행 시 앞단에 데이터가 빠져나간 빈 공간이 생겨 메모리 낭비가 발생할 수 있습니다.

이러한 메모리 낭비를 해결하려하자니 front 이후의 데이터를 모두 하나씩 당겨와야 하니 속도가 저하됩니다.

이를 보안하기 위해 원형 Queue가 등장하였습니다.
<br/>


원형 Queue의 포인터 증가방식은 rear+1%arraysize를 따릅니다.

원형 Queue의 원리를 모듈러 연산(나머지 연산)으로써 적용시켰습니다.

즉 deQueue 실행 시 생긴 앞단의 빈 공간을, 포인터가 배열의 첫 인덱스를 다시 지정할 수 있게 된 것입니다. 
<br/>


위의 선형 Queue를 둥글게 말았다고 생각을 해봅시다.

이때 front == rear = index 0 으로 시작합니다.

front == rear일 때 배열이 공백상태이므로 deQueue는 실행할 수 없습니다.

(rear+1)%arraysize == front라면 rear 포인터가 arraysize를 꽉채우고 front와 같아진 것이기에

배열이 포화상태인 것으로 볼 수 있습니다. 이때 enQueue는 실행할 수 없습니다.

<br/>

원형 Queue에서 array를 모두 채운 뒤 deQueue를 실행하면 앞의 데이터가 빠질 것이고,

enQueue를 실행하면 그 메모리를 가리키는 포인터가 모듈러 연산에 의해 첫 인덱스로 돌아올 것입니다.

이러한 원리를 통해 선형 Queue의 메모리 낭비 문제를 해결할 수 있게 되었습니다.

<br/>

# Queue의 활용

- OS의 task scheduling에서, 워커 쓰레드가 Queue로 넘어온 프로세스를 FIFO의 방식으로 처리하고 제거합니다.

- 네트워크 패킷 처리에서 들어오는 패킷을 관리하는데 사용됩니다.

- BFS(넓이 우선 탐색)에 사용됩니다.

<br/>

# Queue의 예제

Queue의 예제로 백준 12873번을 풀어보겠습니다.

<br/>
https://www.acmicpc.net/problem/12873
<br/>

해당 문제는 원으로 둘러쌓인 원형 Queue라 생각할 수 있습니다.

i번째의 세제곱 index가 제거되긴하나, 모듈러 연산을 통해 제거해줄 수 있습니다.

```python
n = int(input())

queue = [0]*n
for i in range(n):
    queue[i] = i+1 # 1,2,3...n의 Queue 생성

if n == 1: # input length가 1이면 1출력
    print(queue.pop())
else:
    queue.pop(0) # 첫번째는 항상 제거됨
    order = 0
    for i in range(1, n-1):
        pop_index = ((i+1)**3-1)%len(queue) # 2번째 요소부터 계산
        order = order+pop_index # n단계가 끝났을 때 그다음 순서부터 계산하기 위함
        if order >= len(queue):
            order-=len(queue) # order가 queue의 크기를 넘어갔을 때 다시 index 0부터 순환
        queue.pop(order)
    print(queue.pop())
```

이 문제에서 중요한 것은 t단계가 끝나면 queue가 처음이 아닌 데이터가 빠진 그다음 index부터 계산되어진다는 점입니다.

저는 이를 order라는 변수를 만들어 계산에 사용함으로써 가능하게 하였습니다.

또한 order가 len(queue)보다 커지면 순환 queue와 동일하게 다시 0번째 index부터 시작하게끔 코딩했습니다.
