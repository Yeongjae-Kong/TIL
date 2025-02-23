def solution(phone_book):
    phone_book.sort()  # 사전순 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):  # 앞 번호가 뒷 번호의 접두어인지 확인
            return False
    return True