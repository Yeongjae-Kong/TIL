def solution(array, commands):
    ans = []
    for arr in commands:
        i = arr[0]-1
        j = arr[1]-1
        k = arr[2]-1
        print(i, j, k)
        tmp = array[i:j+1]
        tmp.sort()
        ans.append(tmp[k])
    return ans