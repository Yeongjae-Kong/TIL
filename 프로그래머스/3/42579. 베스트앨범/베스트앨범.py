from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    dic2 = defaultdict(int)
    for idx, play in enumerate(plays):
        dic[genres[idx]].append((idx, play))
        dic2[genres[idx]] += play
    print(dic)
    # dic2를 value 기준으로 정렬
    # 각각 순서대로, max(play)의 idx를 2개씩 출력
    lst2 = sorted(dic2.items(), key=lambda x:x[1], reverse=True)
    print(lst2)
    answer=[]
    for i in lst2:
        temp = sorted(list(dic[i[0]]), key=lambda x:(x[1], -x[0]), reverse=True)
        print(temp)
        if len(temp) >= 2:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])
    # for ans in answer:
    #     ans.sort(key=lambda x:x[0])
    #     ans.sort(key=lambda x:x[1], reverse=True)
    # temp = []
    # for i in range(len(answer)):
    #     temp.append(answer[i][0][0])
    #     temp.append(answer[i][1][0])
    print('ans ', answer)
        
    return answer