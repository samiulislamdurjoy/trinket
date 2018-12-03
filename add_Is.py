def box(n):
  if len(n) >= 2 and n[:2] == "Is": 
   return n
  return "Is" + n
print(box("manhole"))
print(box("Isgood"))
