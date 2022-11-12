T = int(input())

for i in range(T):
  array = list(map(int, input().split()))
  answer = '0'

  if (array[0] > array[1]):
    answer = ">"
  elif (array[0] < array[1]):
    answer = "<"
  else:
    answer = "="

  print(f"#{i+1} {answer}")
