from collections import deque

def solution(begin, target, words):
    def checkfunc(a, b):
        cnt = 0
        for i in range(len(a)): # 글자 수는 다 같음
            if a[i] == b[i]:
                cnt += 1
        if cnt == len(a)-1:
            return 1
        return 0
                    
    # hit에서 가능한 모든 (단어, 단계)를 q에 넣는다. 계산한 단어는 visited 처리한다.
    # while q로 반복
    # target이 완성되면 return
    answer = 0
    visited = [0]*len(words)
    q = deque()
    q.append((begin, 0))
    while q:
        temp, level = q.popleft()
        if temp == target:
            return level
        for i in range(len(words)):
            if visited[i] == 0:
                if checkfunc(temp, words[i]) == 1:
                    q.append((words[i], level+1))
                    visited[i] = 1
                    print(words[i], level+1)
    return 0