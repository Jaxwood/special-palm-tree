def floors(str):
  floor = 0
  for i in str:
    if i == '(':
      floor += 1
    else:
      floor -= 1
  return floor
