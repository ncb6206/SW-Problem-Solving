for i in range(10):
  T = int(input())
  array = list(map(int, input().split()))

  maxvalue = max(array)

  for j in range(T):
    if (maxvalue != max(array)):
      maxvalue = max(array)

    array[array.index(max(array))] -= 1
    array[array.index(min(array))] += 1

  value = max(array) - min(array)

  print(f"#{i+1} {value}")
