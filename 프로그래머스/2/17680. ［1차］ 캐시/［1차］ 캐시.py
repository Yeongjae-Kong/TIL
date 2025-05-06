from collections import deque

def solution(cacheSize, cities):
    # 캐시에 없을 때
    # 캐시에 있을 때
    # 캐시에 없고 캐시가 꽉찼을 때
    # 캐시에 있고 캐시가 꽉찼을 때
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    cache = deque()
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        if len(cache) < cacheSize:
            if city not in cache:
                cache.append(city)
                answer += 5
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1
        elif len(cache) == cacheSize:
            if city not in cache:
                cache.popleft()
                cache.append(city)
                answer += 5
            else: # 캐시에 존재
                cache.remove(city)
                cache.append(city)
                answer += 1
    return answer