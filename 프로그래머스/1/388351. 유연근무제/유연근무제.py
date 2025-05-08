def solution(schedules, timelogs, startday):
    answer = len(schedules)
    # abs(6-startday), 7-startday는 제외
    for i in range(len(timelogs)):
        for j in range(7):
            if (startday + j - 1) % 7 + 1 in (6, 7):
                continue
            else:
                # 평일검사
                if timelogs[i][j] > 1110:
                    answer -= 1
                    break
                a = str(timelogs[i][j])
                if a[-2] == '0':
                    a = str(int(a[:-2])-1)+'5'+a[-1]
                    if int(a) > schedules[i]:
                        answer -= 1
                        break
                else: 
                    if timelogs[i][j]-10 > schedules[i]:
                        answer -= 1
                        break
    return answer