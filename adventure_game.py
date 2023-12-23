name = input("Type your name: ")
print("I welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right, which way do you want to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross it? Type walk to walk around and swim to swin accross: ")
    
    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")
        
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
        
    else:
        print("Not a valid option. You lose.")
    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    
    if answer == "back":
        print("You go back and loose.")
        
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger, Do you talk to them, (Yes or No)? ")
        if answer == "yes":
            print("You talk to the strangere and they give you gold. You WIN!")
            
        elif answer == "no":
            print("You ignored the stranger and offended them and You LOSE!")
            
        else: 
            print("Not a valid option. You lose.")
        
   

else:
    print("Not a valid option. You lose.")
    
print("Thank you for trying", name)