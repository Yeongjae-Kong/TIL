from itertools import combinations

def calculate_team_power(team, S):
    power = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            power += S[team[i]][team[j]] + S[team[j]][team[i]]
    return power

def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    
    members = list(range(N))
    min_difference = float('inf')
    
    # 모든 조합을 시도
    for start_team in combinations(members, N // 2):
        link_team = [m for m in members if m not in start_team]
        
        start_power = calculate_team_power(start_team, S)
        link_power = calculate_team_power(link_team, S)
        
        difference = abs(start_power - link_power)
        min_difference = min(min_difference, difference)
    
    print(min_difference)

main()
