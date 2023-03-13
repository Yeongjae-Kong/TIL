
# Separate Chaining과 Open Addressing에 관한 고찰 (with Java & Python)


삭제 연산을 수행할 때, 해시 함수의 리턴값이 같은 Key가 여러개 있는 경우

Chaining 기법은 연결 리스트의 삭제 방법과 동일하게 포인터가 다음 노드를 가르키도록 변경합니다.

하지만 Open Addressing 기법에서 데이터를 삭제하게 되는 경우, 해당 버킷의 공간이 비게 됩니다.

이때 삽입 및 탐색 과정에서 삭제로 인해 비어진 공간을 보고 값이 저장되지 않았다고 판단할 수 있습니다.

이렇게 되면 그 이후 Index에 저장된 pair를 찾을 수 없게 됩니다.

<br/>

Linear Probing을 예로 들면, n+1 Index의 (key, value)를 삭제했을 때, n+1 index의 bucket이 비게 되고 추후 탐색을 수행할 때 빈 공간을 만나면 더이상 탐색을 지속하지 않아 n+2 Index의 (key, value)를 찾을 수 없게 될 수 있습니다.

이러한 문제는 삭제한 공간에 Null과 같은 임의의 값을 저장하여 그 값을 만날 경우 탐색을 계속하게 함으로써 해결할 수 있습니다.

<br/>

하지만, 그렇게 되면 쓰지 않는 bucket 공간을 Null이 차지하는 메모리 누수가 발생하게 되어 비효율적입니다.

C와 같은 Low-level 언어가 아니면 자동적으로 garbage collection이 수행되어 도달 가능성이 없는 객체를 메모리에서 삭제하게 되지만, 이또한 비용이 발생합니다.

<br/>

추가적으로 Chaining의 경우 작동 원리의 특성 상 LF가 증가하여도 성능 저하가 linear하지만 Open Addressing은 LF가 증가함에 따라 성능이 비약적으로 떨어지게 됩니다. (아래 표 참고)

<br/>




이러한 이유들로 인해 Java의 HashMap에서는 Open Addressing이 아닌 Separate Chaining 방법을 사용하고 있습니다.

Java는 Robust한 언어라 불리기에 메모리 관리의 안전성과 견고성에 초점을 둡니다.  

따라서 Separate Chaning 기법이 Linked-list의 메소드에 synchronized 키워드를 선언하여 동기적으로 구현하기 비교적 쉽기 때문에, 자바의 멀티 쓰레드 환경에 맞는 thread-safe한 기법인 Separate Chaining을 선택한 것으로 보입니다.

<br/>

반면 파이썬의 경우에는 HashTable로 구현한 Dict 클래스에서 충돌이 발생할 때 Open Addressing 방법을 사용합니다.

기본적으로 싱글스레드로 동작하고, 간결하고 빠른 개발속도를 추구하는 파이썬의 특성에 기인한 것으로 보입니다.

위에서 Java의 HashMap 등의 자료구조는 LF를 75%로 한다고 언급했는데, Python의 dict 자료형의 경우 LF를 66%로 제한하고, 이 이상으로 데이터가 차면 더 큰 크기의 해시 테이블을 새로 생성한 뒤 기존 데이터를 새로운 해시 테이블로 옮기는 과정을 수행합니다. 이렇게 옮기는 과정을 제외하면, 위의 표에서 볼 수 있듯이 탐색 속도는 0.66의 Load Factor 아래에서 Chaining보다 더욱 빠른 성능을 낼 수 있습니다.

<br/>

또한 파이썬의 Dict는 Open Addressing 중에서도 Pertubation Shift Probing이라는 고유의 방법을 사용합니다.

<br/>

위와 같은 수식을 통해 더 효율적으로 해시 충돌을 해결하였습니다.

python github 공식문서에서 더욱 디테일한 내용을 찾을 수 있습니다.

https://github.com/python/cpython/blob/v3.9.1/Objects/dictobject.c#L133
