sum1 = 0
sum2 = 0
sum3 = 0

A = int(input())

B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

for i in range(0, 10):
  if (B[i] % 2 == 1):
    sum1 += B[i]

for k in range(0, 10):
  if (C[k] % 2 == 1):
    sum2 += C[k]

for j in range(0, 10):
  if (D[j] % 2 == 1):
    sum3 += D[j]

print('#1 ' + str(sum1))
print('#2 ' + str(sum2))
print('#3 ' + str(sum3))
