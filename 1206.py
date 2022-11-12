for h in range(0, 10):
  T = int(input())
  building = list(map(int, input().split()))
  yang = [0 for y in range(4)]
  sede = 0

  for i in range(2, T - 2):
    yang[0] = building[i - 2]
    yang[1] = building[i - 1]
    yang[2] = building[i + 1]
    yang[3] = building[i + 2]
    if (building[i] > max(yang)):
      sede += building[i] - max(yang)

  print(f"#{h+1} {sede}")
