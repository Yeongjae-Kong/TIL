def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    students_in_class = n - len(lost_set)
    
    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            students_in_class += 1
            reserve_set.remove(student - 1)
        elif student + 1 in reserve_set:
            students_in_class += 1
            reserve_set.remove(student + 1)
    
    return students_in_class