def solution(arr):
    ans = []
    ans.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            ans.append(arr[i+1])
    answer = ans
    return answer