def solution(name):
    n = len(name)
    move = n - 1
    answer = 0
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        move = min(move, 2 * i + n - next_i, i + 2 * (n - next_i))
    
    return answer + move