import random

def shoot():#main body of the program
    points = 0
    difficulty = input("Select your difficulty level: 1, 2, 3 ")#this is only for temp measures until GUI is implemented
    thresh = 0  #this is the points threshold for winning
    if difficulty == "1":
        thresh = 500
    elif difficulty == "2":
        thresh = 750
    elif difficulty == "3":
        thresh = 1000
    else:
        print("Invalid input")
   
    def stage(): #core rolling concept
        dice = random.randrange(1,6)
        dice1 = random.randrange(1,6)
        dice2 = random.randrange(1,6)
        dice3 = random.randrange(1,6)
        dice4 = random.randrange(1,6)
        dice5 = random.randrange(1,6)

        array = [dice, dice1, dice2, dice3, dice4, dice5]

        print(dice,dice1,dice2,dice3,dice4,dice5)
        
        def check_pairs():
            nonlocal points
            numbers = [2, 3, 4, 6]  # List of specific numbers to check for pairs
            for x in numbers:
                if array.count(x) == 2:
                    points += 200
                if array.count(x) == 3:
                    points += 300
                if array.count(x) == 4:
                    points += 400
                if array.count(x) == 5:
                    points += 1000
                if array.count(x) == 6:
                    points += 1200

        check_pairs()

        def check_points():#assigning points to the dice rolls
            nonlocal points
            if array.count(1) == 1:
                print("100 points!")#this is only for temp measures until GUI is implemented   
                points += 100       #this gives "1s" a special value
            if array.count(1) == 2:
                print("200 points!")   
                points += 200
            if array.count(1) == 3:
                print("300 points!")   
                points += 300
            if array.count(1) == 4:
                print("400 points!")   
                points += 400
            if array.count(1) == 5:
                print("500 points!")   
                points += 500
            if array.count(1) == 6:
                print("600 points!")   
                points += 600


            if array.count(5) == 1: #this is to give "5s" a special value
                print("50 points!")
                points += 50
            if array.count(5) == 2:
                print("100 points!")
                points += 100
            if array.count(5) == 3:
                print("150 points!")
                points += 150
            if array.count(5) == 4:
                print("200 points!")
                points += 200
            if array.count(5) == 5:
                print("250 points!")
                points += 250
            if array.count(5) == 6:
                print("300 points!")
                points += 300
            


            
            
        check_points()


    if points > thresh:
        print("You win")
    else:
        print("You lose")
    stage()  
    print("your total is", points, "points")
  
    

shoot()


