ma = ['H','He','Li','Be','B','C','N','O','F','Ne']
mass = {'H':1,'He':4,'Li':7,'Be':9,'B':11,'C':12,'N':14,'O':16,'F':19,'Ne':20}
start = 0
while start != 1:
 el = input("xA + yB + zC + ..., where x, y, and z are positive integers (called stoichiometric coefficients) and A, B, and C are distinct symbols of elements.\n " )
 el = el.split("+")
 #print(elements)
 am = 0
 length = len(el)
 f = ''
 for i in range(length):
  divide = list(el[i])
  adivide = ''.join(divide[-2:])
  if divide[-1] in ma:
   sc = int(el[i].replace(divide[-1], ''))
   am = am + sc* mass[divide[-1]]
   if sc == 1:
    f =f + divide[-1]
   else:
    f = f + divide[-1] + str(sc)
   start = 1
  elif adivide in ma:
   sc = int(el[i].replace(adivide,''))
   am = am + sc * mass[adivide]
   if sc == 1:
    f = f + adivide
   else:
    f = f + adivide + str(sc)
   strat = 1
  else:
   print("Input error, please re-enter")
print(f)
print(am)