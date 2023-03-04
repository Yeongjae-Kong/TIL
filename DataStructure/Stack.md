# Stack이란?


Stack은 데이터를 차곡차곡 쌓아 놓은 형태의 자료구조로, 가장 마지막에 삽입된 데이터가 가장 먼저 삭제됩니다.
이러한 구조를 후입선출, 즉 LIFO(Last In First Out)이라 합니다.

Stack의 연산은 크게 push(item), pop()으로 이루어집니다.

즉 pop()을 실행하면 마지막으로 push로 넣은 item이 나옵니다.

그 외에도 Peek(), isFull(), isEmpty() 등의 함수가 있습니다.

Peek() 마지막으로 push한 item을 빼지않고 출력만 해주는 함수이고,

isFull()은 stack overflow를 방지하기 위해 stack이 꽉 찼는지 확인할 때 쓰는 함수입니다.

isEmpty()는 반대로 스택이 비어있는지 확인할 수 있고, boolean을 반환합니다. 

-----------------------------

# Stack의 활용


- Stack은 재귀함수가 필요할 때 스택 자료구조를 통해 구현할 수 있습니다.

- 웹 브라우저의 뒤로가기 버튼 또한 스택의 원리를 통해 구현할 수 있습니다.

- 그 외에도 프로그램의 실행 취소, C/C++의 main() 함수에서 사용되는 지역변수와 함수를 관리하는데 사용됩니다.

----------------------------

# Stack의 예제


Stack의 예제로 백준 9012번 문제를 풀어보겠습니다. 

https://www.acmicpc.net/problem/9012

괄호 문자열()의 짝이 맞는지를 확인하는 문제입니다.

해당 문제의 핵심 아이디어는 Stack의 원리와 동일한 것을 깨우쳐야 합니다.

' ( ' 괄호의 경우 스택에 push를 해주고,

' ) ' 괄호로 짝이 맞아지면 스택에 pop을 하여, 마지막 Stack이 empty가 되면 짝이 맞고,

그렇지 않으면 짝이 맞지 않은 것입니다.

해당 문제에서는 짝이 맞는지 여부를 YES, NO로 출력하라고 명시되어있기에, 그렇게 코딩해보겠습니다.

``` python
import sys
n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # not break
        if len(stack) == 0: # 스택이 비어있으면 YES
            print("YES")
        else: # 스택이 안비어있으면 NO
            print("NO")
```


상단의 sys.stdin.readline()의 경우 input() 대신에 사용하는 것으로,

input()은 입력 값이 여러개일 경우 개행 문자로 나누어 여러 버퍼에 저장하지만,

sys.stdin.readline()의 경우 하나의 버퍼에 저장하기 때문에 입력이 많을 경우에 실행 속도에 이점이 있습니다.



해당 코드의 경우 stack과 동일한 원리로 ' ( ' 가 나올 때마다 Stack에 넣고, ' ) ' 가 나올 때마다 Stack에서 pop하는 원리를 활용하여 반복문을 통해 괄호 문자열의 짝이 맞는지 여부를 확인할 수 있습니다!