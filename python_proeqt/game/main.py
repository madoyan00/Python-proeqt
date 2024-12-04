import random
try:
    k = int(input("enter range from 0 to 1000 "))
except ValueError:
   raise "enter only  number..."
num = random.randint(0, k)
count = 0

if  0 < k <= 128:
    x = 7
    print("you have 7 chances to try")

elif 100 < k <= 512:
    x = 9
    print("you have 9 chances to try")

elif 500 < k <= 1000:
    x = 10
    print("you have 10 chances to try")
    
else:
    x = 0
    print("your  number is not in  this range")
    

while count != x:
    try:
        number = int(input("enter number "))
    except ValueError:
      raise "enter only  number..."
    
   
    if number == num:
        print(f"you win!!! random number is {num}")
        
    elif number > num:
        print("your number is big")
       
    elif number < num:
        print("your number is small")
        
    else:
        print("error")
    
    count += 1
print("Game  over!!!")
