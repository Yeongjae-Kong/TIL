from collections import deque

def solution(s):
    ans = 0
    if len(s) % 2 == 0:
        for _ in range(len(s)):
            q = deque()
            s = s[1:]+s[0]
            q.append(s[0])
            for i in range(1, len(s)):
                if len(q) != 0:
                    tmp = q.pop()
                else:
                    q.append(s[i])
                    continue
                if (tmp, s[i]) in (('(',')'), ('{','}'), ('[',']')): 
                    continue
                else:
                    q.append(tmp)
                    q.append(s[i])
            if len(q) == 0:
                ans+=1
    else:
        return 0
    return ans