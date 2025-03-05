def solution(expression):
    # + - * 세가지, 경우의 수 최대 6 -> 직접 구현?
    # 길이 100 이하
    
    def minus(temp):
        ans = []
        for e in temp:
            nums = list(map(int, e.split("-")))  # 문자열 리스트를 정수 리스트로 변환
            result = nums[0]  # 첫 번째 숫자
            for num in nums[1:]:  # 두 번째 숫자부터 차례로 뺀다
                result -= num
            ans.append(result)
        return ans

    def plus(temp):
        ans = []
        for e in temp:
            nums = list(map(int, e.split("+")))  # 문자열 리스트를 정수 리스트로 변환
            result = sum(nums)  # 모든 숫자의 합
            ans.append(result)
        return ans

    def multiple(temp):
        ans = []
        for e in temp:
            nums = list(map(int, e.split("*")))  # 문자열 리스트를 정수 리스트로 변환
            result = 1
            for num in nums:
                result *= num
            ans.append(result)
        return ans

    
    # --------
    
    def multipleminus(temp):
        temp = temp.split("+")
        ans = []
        for e in temp:
            temp = e.split("*")
            temp = minus(temp)
            multiple=1
            for num in temp:
                multiple *= int(num)
            ans.append(multiple)
        ansnum = 0
        for num in ans:
            ansnum += int(num)
        return ansnum
    
    def multipleplus(temp):
        temp = temp.split("-")
        ans = []
        for e in temp:
            temp = e.split("*")
            temp = plus(temp)
            multiple=1
            for num in temp:
                multiple *= int(num)
            ans.append(multiple)
        ansnum = int(ans[0]) * 2
        for num in ans:
            ansnum -= int(num)
        return ansnum
    
    
    def plusminus(temp):
        temp = temp.split("*")
        ans = []
        for e in temp:
            temp = e.split("+")
            temp = minus(temp)
            plus = 0
            for num in temp:
                plus += int(num)
            ans.append(plus)
        ansnum = 1
        for num in ans:
            ansnum *= int(num)
        return ansnum
    
    def plusmultiple(temp):
        temp = temp.split("-")
        ans = []
        for e in temp:
            temp = e.split("+")
            temp = multiple(temp)
            plus = 0
            for num in temp:
                plus += int(num)
            ans.append(plus)
        ansnum = ans[0] * 2
        for num in ans:
            ansnum -= int(num)
        return ansnum
    
    def minusplus(temp):
        temp = temp.split("*")
        ans = []
        for e in temp:
            temp = e.split("-")
            temp = plus(temp)
            minus = temp[0] * 2
            for num in temp:
                minus -= int(num)
            ans.append(minus)
        ansnum = 1
        for num in ans:
            ansnum *= int(num)
        return ansnum
    
    def minusmultiple(temp):
        temp = temp.split("+")
        ans = []
        for e in temp:
            temp = e.split("-")
            temp = multiple(temp)
            minus = temp[0] * 2
            for num in temp:
                minus -= int(num)
            ans.append(minus)
        ansnum = 0
        for num in ans:
            ansnum += int(num)
        return ansnum
    
    answer = []
    answer.append(abs(plusminus(expression)))
    answer.append(abs(plusmultiple(expression)))
    answer.append(abs(minusplus(expression)))
    answer.append(abs(minusmultiple(expression)))
    answer.append(abs(multipleplus(expression)))
    answer.append(abs(multipleminus(expression)))
    
    ans = max(answer)
    return ans