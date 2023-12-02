import random
n=random.randrange(1,100)

guess=int(input("Guess a number between 1 and 100 :"))
tries=0
while(n!=guess):
    
    tries=tries+1
    if(guess>n):
        print("Lower !!")
        guess=int(input("Enter the number again :"))
        
    
    elif(guess<n):
        print("higher !!")
        guess=int(input("Enter the number again :"))
          
    else:
        break

if(guess==n):
    print("Congratulation, You guessed the number in",tries," tries !!")
        

