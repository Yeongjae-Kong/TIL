n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    
    # 문서의 중요도와 원래 인덱스를 함께 저장
    queue = [(val, idx) for idx, val in enumerate(lst)]
    cnt = 0
    
    while queue:
        # 현재 문서가 가장 중요도가 높으면 인쇄
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            cnt += 1
            # 만약 우리가 찾고 있는 문서라면 결과 출력
            if queue[0][1] == b:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            # 중요도가 더 높은 문서가 있으면 뒤로 이동
            queue.append(queue.pop(0))