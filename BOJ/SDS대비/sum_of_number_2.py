M, N = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = 0
result = 0

while start <= end <= len(data):
    temp = sum(data[start:end])
    if temp == N:
        result += 1
    if temp <= N:
        end += 1
        continue
    elif temp > N and start < end:
        start += 1
        continue
    else:
        start += 1
        end += 1

print(result)
