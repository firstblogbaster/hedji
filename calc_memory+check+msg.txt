memory=0
msg_list=list()
l1="Are you sure? It is only one digit! (y / n)"
l2="Don't be silly! It's just one number! Add to the memory? (y / n)"
l3="Last chance! Do you really want to embarrass yourself? (y / n)"
msg_list.append(l1)
msg_list.append(l2)
msg_list.append(l3)

def check(v1, v2, v3):
  

  v1=float(v1)
  v2=float(v2)

  msg=''
  if is_one_digit(v1) and is_one_digit(v2):
    msg = msg + " ... lazy"
  if (v1 == 1 or v2 == 1) and v3 == '*':
    msg = msg + " ... very lazy"
  if (v1==0 or v2==0) and (v3=='*' or v3=='+' or v3=='-'):
    msg = msg + " ... very, very lazy"
  if msg !='':
    msg = "You are" + msg
    print(msg)
    
 
    
  if type(v1) == 'str' or type(v2) == 'str':
    print("Do you even know what numbers are? Stay focused!")     
  elif v3 not in "+-*/":
    print("Yes ... an interesting math operation. You've slept through all classes, haven't you?") 
  return v1, v2, v3

def is_one_digit(v):
  if v > -10 and v < 10 and v-int(v)==0:
    output = True
  else:
    output = False
  return output


while True:
  print("Enter an equation\n")
  x, oper, y = input().split()

  if x == 'M':
    x = memory
  if y == 'M':
    y=memory
    
  check(x,y,oper)
  
  
  x=float(x)
  y=float(y)
   
  if oper == '+':
    result = x + y
    print(result)
  elif oper == '-':
    result =  x - y
    print(result)
  elif oper == '*':
    result = x * y
    print(result)
  elif oper == '/' and y !=0:
    result = x / y
    print(result)
  else:
    print("Yeah... division by zero. Smart move...")
    continue
    
  print("Do you want to store the result? (y / n):" ) 
  
  answer = input()
  if answer == 'y':
    if answer=='y' and not is_one_digit(result):
      memory = result
    if is_one_digit(result):
      msg_index = 0
      while msg_index<=2:
        print(msg_list[msg_index])
        answer2=input()
        if answer2=='y':
          msg_index+=1
        elif answer2=='n':
          break
      if answer2=='y':
        memory = result

  while True:
    print("Do you want to continue calculations? (y / n):")
    answer2 = input()
    if answer2 == 'y':
      break
    elif answer2 == 'n':
      break
    else:
      continue

  if answer2 =='n':
    break