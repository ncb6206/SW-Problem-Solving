T = int(input())
fullprice = [0 for p in range(T)]

for x in range(T):
  N = int(input())
  price = list(map(int, input().split()))

  count = 0
  somo = 0
  notmore = 0
  max = 0
  fullprice[x] = 0

  for i in range(0, N):
    for j in range(i, N):
      if (price[i] < price[j]):
        count += 1
        somo += price[i]
        max = price[j]
        notmore += 1
        break
    if (notmore == 0):
      fullprice[x] += (price[i] * count) - somo
      count = 0
      somo = 0
    notmore = 0

  print(f"#{x+1} {fullprice[x]}")
