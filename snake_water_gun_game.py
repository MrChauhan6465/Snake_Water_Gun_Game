import random

print ("======Welcome to the snake water gun game======")
rounds =1
computer_points = 0
draw_points=0
player_points=0
def game():
    global rounds
    global computer_points
    global draw_points
    global player_points
    moves = ['snake','gun','water']
    
    while rounds<=10:
        computer_choice =random.choice(moves)
        print(moves)
        user_choice =str(input(f"Enter your choice : round {rounds}:\n"))
        print("computer choice : ",computer_choice)
      
        if user_choice == computer_choice:
            print("draw")
            draw_points+=1
        elif user_choice == 'snake':
            if computer_choice == 'gun':
                print("You loose ")
                computer_points+=1
            else:
                print("You won ")
                player_points+=1
        elif user_choice =='water':
            if computer_choice =='snake':
                print("You loose")
                computer_points+=1
            else:
                print("You won")
                player_points+=1
        elif user_choice=='gun':
            if computer_choice =='water':
                print("You loose")
                computer_points+=1
            else:
                print("You won ")
                player_points+=1
        if rounds==10:
            if player_points>computer_points:
                print("=====Congratulations you  won the game")
            elif player_points==computer_points:
                print(" ====Match Draw====")
            else:
                print("=====You loose the game====")  
        rounds+=1

   
                     
game()
print("\nTotal Score at the end of  rounds")
print("\nNo. of rounds draw between cpu and player :")
print(f"{draw_points} rounds")
print("\nNo. of rounds player won:")
print(f"{player_points} rounds")
print("\nNo. of rounds cpu won :")
print(f"{computer_points} rounds")

        

