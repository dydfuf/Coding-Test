def cacheHit(cache, value, time):
    for aCache in cache:
        if aCache[0] == value:
            aCache[1] = time
            break

    return cache


def cacheMiss(cache, cacheSize, value, time):
    # 사용 가능한 캐시가 비어있다면
    if len(cache) < cacheSize:
        cache.append([value, time])
        return cache

    # LRU
    sortedCache = sorted(cache, key=lambda x: x[1])
    sortedCache.pop(0)

    sortedCache.append([value, time])

    return sortedCache


def isInCache(cache, value):
    for aCache in cache:
        if aCache[0] == value:
            return True

    return False


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = list()

    for idx, city in enumerate(cities):
        city = city.lower()

        # cache에 있는지
        if isInCache(cache, city):
            answer += 1
            cache = cacheHit(cache, city, idx)
        else:
            # cache에 없다면
            answer += 5
            cache = cacheMiss(cache, cacheSize, city, idx)

    return answer

def solution2(cacheSize, cities):
    from collections import deque
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
    return answer
if __name__ == '__main__':
    arr_cacheSize = [3, 3, 2, 5, 2, 0]
    arr_cities = [["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
                  ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
                  ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                   "NewYork", "Rome"],
                  ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                   "NewYork", "Rome"],
                  ["Jeju", "Pangyo", "NewYork", "newyork"],
                  ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]

    for cacheSize, cities in zip(arr_cacheSize, arr_cities):
        print(solution2(cacheSize, cities))
