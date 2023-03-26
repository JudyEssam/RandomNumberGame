import random 
x = random.randint(0,10) 
y=int(input('enter you guess'))
score = 100
if ( x!=y) : 
    while ( y>x ) : 
        score = score -10 
        y=int(input('enter a smaller number'))
        if ( y == x ) : 
            print ("true the number is",y)
            print ('your score =' , score)
            break 
        elif (y>x) : 
            continue
        else : 
            break 
    while ( y<x ) : 
        score = score -10 
        y=int(input('enter a greater number'))
        if ( y == x ) : 
            print ("true the number is",y)
            print ('your score =' , score)
            break 
        elif (y<x) : 
            continue
        else : 
            break
else : 
    print ('Great you got it right from the first time')
    print ('you score is',score)


    


    
    


    


