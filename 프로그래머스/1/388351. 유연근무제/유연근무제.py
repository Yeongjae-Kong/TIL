def add_10_minutes(time):
    hour = time // 100
    minute = time % 100
    minute += 10
    if minute >= 60:
        hour += 1
        minute -= 60
    return hour * 100 + minute

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        hope_time = schedules[i]
        success = True
        for j in range(7):
            day = (startday + j - 1) % 7 + 1  # 1~7 사이 요일로 변환
            if day in (6, 7):  # 토요일, 일요일 제외
                continue
            if timelogs[i][j] > add_10_minutes(hope_time):
                success = False
                break
        if success:
            answer += 1
    return answer
