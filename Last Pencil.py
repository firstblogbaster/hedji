import random
name0 = 'John'
name1 = 'Jack'

def bot_count_pencils():
  global y
  if y == 4:
    par1 = 3 
  elif y == 3:
    par1 = 2
  elif y == 2:
    par1 = 1
  elif y == 1:
    par1 =1 
  elif y%4 == 0:
      par1 = 3
  elif y%2 != 0:
      par1 = 2
  elif y%2 == 0:
      par1 = 1
  else:
    par1=random.randint(1, 3)
  return par1

def check_count_pencils():
  global y
  while True:    
    par1=input()
    try:
      int(par1)
    except ValueError:
      print("Possible values: '1', '2' or '3'")
    else:
      if int(par1)<=0 or int(par1)>3:
        print("Possible values: '1', '2' or '3'")
      elif int(par1)>y:
        print("Too many pencils were taken")
      else:
        return int(par1)
        break
  

while True:
  x = input("How many pencils would you like to use:")
  try:
    int(x)
  except ValueError:
    print("The number of pencils should be numeric")
  else:
    if int(x)<0:
      print("The number of pencils should be numeric")
    elif int(x)==0:
      print("The number of pencils should be positive")
    elif int(x)>0:
      break

while True:
  namex = input('Who will be the first (John, Jack):')
  if namex==name0 or namex==name1:
    break
  else:
    print("Choose between " + name0 +" and " + name1)
  
if namex == name0:
    xod=0
elif namex ==name1:
    xod=1

y=int(x)
while y != 0:
    print('|'*y)
    
    if xod==0:
      print(name0,"'s turn!")
      xod=1
      pencils=check_count_pencils()
      
    elif xod==1:
      print(name1,"'s turn:")   
      xod=0
      pencils=bot_count_pencils()
      print(pencils)
    
    y = y - pencils
    if y<=0:
        break
if xod==0:
  print(name0, " won!")
elif xod==1:
  print(name1, " won!")
        