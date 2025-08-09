N, K = map(int, input().split())
arr = list(map(int, input().split()))

freq = {}
i = 0
maxlen = 0

for j in range(N):
    if arr[j] in freq:
        freq[arr[j]] += 1
    else:
        freq[arr[j]] = 1

    while len(freq) > K:
        freq[arr[i]] -= 1
        if freq[arr[i]] == 0:
            del freq[arr[i]]
        i += 1

    maxlen = max(maxlen, j - i + 1)

print(maxlen)
