N = int(input())
array = [0 for l in range(N)]

for i in range(0, N):
  count = 0
  check = str(i + 1)

  for j in range(len(check)):
    if (check[j] == '3' or check[j] == '6' or check[j] == '9'):
      count += 1

  if (count == 0):
    array[i] = i + 1
  else:
    array[i] = "-" * count

print(f"{array}".strip('[]').replace(',', '').replace('\'', ''))
