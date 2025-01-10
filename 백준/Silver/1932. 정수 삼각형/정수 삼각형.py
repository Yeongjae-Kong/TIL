n = int(input())

lst = []

for i in range(n):
    tmp = list(map(int, input().split()))  # 입력받은 줄을 리스트로 변환
    lst.append(tmp)  # 리스트에 추가
    
def max_path_sum(triangle):
    # 삼각형의 길이를 구합니다.
    n = len(triangle)

    for i in range(n - 2, -1, -1):  # 마지막 전 줄부터 시작
        for j in range(len(triangle[i])):
            # 현재 위치의 최대 합은 그 아래층 인접한 두 값 중 큰 값을 더한 값
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # 최종적으로 triangle[0][0]에 최대 합이 저장됩니다.
    return triangle[0][0]

# 결과 출력
print(max_path_sum(lst))  # 출력: 18
