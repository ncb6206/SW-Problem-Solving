T = int(input())

for x in range(T):
  N = int(input())
  array = [i + 1 for i in range(N * N)]
  last = [[0 for j in range(N)] for y in range(N)]
  row = 0
  column = 0
  s = 0

  while (s < N * N):
    while (column + 1 < N):
      if (last[row][column + 1] == 0):
        last[row][column] = array[s]
        s += 1
        column += 1
      else:
        break
    while (row + 1 < N):
      if (last[row + 1][column] == 0):
        last[row][column] = array[s]
        s += 1
        row += 1
      else:
        break
    while (column - 1 >= 0):
      if (last[row][column - 1] == 0):
        last[row][column] = array[s]
        s += 1
        column -= 1
      else:
        break
    while (row - 1 >= 0):
      if (last[row - 1][column] == 0):
        last[row][column] = array[s]
        s += 1
        row -= 1
      else:
        break
    if (s == N * N - 1):
      last[row][column] = array[s]
      s += 1

  print(f"#{x+1}")
  for l in range(N):
    print(f"{last[l]}".strip('[]').replace(',', ''))
