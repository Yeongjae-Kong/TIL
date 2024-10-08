def solution(diffs, times, limit):
    answer = 0
    # diff[i]보다 level이 크거나 같으면 timesum += time[i]
    # else: timesum += (time[i-1]+time[i])*(diffs[i]-level) + time[i]
    # if timesum > limit : break
    #
    # level = max(diffs) // 2
    # i = 1
    # if timesum > limit: 1. if level // (i), < 100: -1씩 하고 return.  
    #   2. level = level // (1+i)
    # if timesum < limit:
    #   1. if level * i < 100: +1씩 하고 return.
    #   2. i = i/2, level = level * (1+i), i = i/2. 
    level = max(diffs) // 2
    prev_timesum = 0
    prev_level = 0
    w = max(diffs)//2

    while True:
        timesum = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                timesum += times[i]
            else:
                timesum += (times[i-1]+times[i]) * (diffs[i]-level) + times[i]

        if prev_timesum <= limit < timesum:
            if abs(level-prev_level) == 1:
                if prev_level >= 1:
                    answer = prev_level
                else:
                    answer = 1
                return answer
        if timesum <= limit < prev_timesum:
            if abs(level-prev_level) == 1:
                if level >= 1:
                    answer = level
                else:
                    answer = 1
                return answer
        
        prev_level = level
        prev_timesum = timesum

        if w > 1:
            w = w // 2

        if timesum > limit:
            level += w
        else: # timesum <= limit
            level -= w
    return answer