T = int(input())

for x in range(T):
    test = list(map(int,input().split()))
    N = test[0]
    M = test[1]
    array = [[0 for a in range(N)] for b in range(N)]
    imsi = [[0 for c in range(N-M+1)] for d in range(N-M+1)]
    maxarray = [0 for t in range(N-M+1)]

    for i in range(N):
        array[i] = list(map(int,input().split()))

    for q in range(N-M+1):
        for w in range(N-M+1):
            for row in range(M):
                for column in range(M):
                    imsi[q][w] += array[q+column][w+row]

    for p in range(N-M+1):
        maxarray[p] = max(imsi[p])

    maxvalue = max(maxarray)
    print(f"#{x+1} {maxvalue}")
