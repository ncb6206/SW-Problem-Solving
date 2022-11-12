T = int(input())

for i in range(T):
  nayeol = list(map(int, input().split()))
  hap = 0
  hap = sum(nayeol)
  middle = hap / 10

  print(f"#{i+1} {round(middle)}")
