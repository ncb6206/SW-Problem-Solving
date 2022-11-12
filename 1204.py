T = int(input())

for x in range(T):
    testcase = int(input())
    bayeol = [0 for person in range(101)]
    imsi = []
    student = list(map(int,input().split()))

    for i in range(101):
        bayeol[i] = student.count(i)

    for y in range(101):
        if(max(bayeol)==bayeol[y]):
            imsi.append(y)

    maxvalue = max(imsi)

    print(f"#{testcase} {maxvalue}")
