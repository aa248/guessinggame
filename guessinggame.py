import random


def guessinggame():
    num = random.randint(1,10)
    print num
    numguesses = 0
    while True:
        guess = raw_input('Guess a number between and including 1 and 10: ' )
        
        try:
           
            guess = int(guess)
            
            if guess == num:
                break
            else:
                print 'Nope! Try again! '
                
                numguesses+=1
            
        except:
            print 'Sorry, the input must be an integer.'
        
        
   
    print 'Awesome, you guessed correctly! The magic number was ' + str(num) + ' and you took ' + str(numguesses) + ' tries'
    
    again = raw_input('Do you want to try a harder one? Enter Yes or No: ')
    if again == 'Yes' or again=='yes':
        num = random.randint(1,25)
        count = 0
        while True:
            guess = raw_input('Now guess a number between and including 1 and 25: ' )
            
            
            try:
                guess = int(guess)
                      
                if guess == num:
                    break
                else:
                    print 'Nope! Try again! '
                    count+=1
            except:
                print 'Sorry, the input must be an integer.'
       
        
        print 'Awesome, you guessed correctly! The magic number was ' + str(num) + ' and you took ' + str(count) + ' tries'



if __name__ == '__main__':
    guessinggame()