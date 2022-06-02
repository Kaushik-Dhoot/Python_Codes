import time
import random

print("\t\t*****Welcome to rock Paper Scissor Game*****")
time.sleep(2)
player_win = 0
cpu_win = 0
tie = 0

def cpu_choose():
    print("CPU is choosing...")

def game():
    global player_win
    global cpu_win
    global tie
    list_cpu = ["ROCK", "PAPER", "SCISSOR"]
    cpu_choice = random.choice(list_cpu)
    player_choice = input("\nRock\nPaper\nScissor\nEnter your choice :")

    if player_choice.upper() == cpu_choice.upper():
        cpu_choose()
        time.sleep(2)
        print(f"\tYour choice is {player_choice.upper()} and CPU's choice is {cpu_choice}")
        # time.sleep(2)
        print("\tIts a tie\n")
        tie = tie + 1

    elif player_choice.upper() == "ROCK" and cpu_choice.upper() == "SCISSOR":
        cpu_choose()
        time.sleep(2)
        print(f"\tYour choice is {player_choice.upper()} and CPU's choice is {cpu_choice}")
        # time.sleep(2)
        print("\tYou Won!!!\n")
        player_win = player_win + 1

    elif player_choice.upper() == "PAPER" and cpu_choice.upper() == "ROCK":
        cpu_choose()
        time.sleep(2)
        print(f"\tYour choice is {player_choice.upper()} and CPU's choice is {cpu_choice}")
        # time.sleep(2)
        print("\tYou Won!!!\n")
        player_win = player_win + 1

    elif player_choice.upper() == "SCISSOR" and cpu_choice.upper()== "PAPER":
        cpu_choose()
        time.sleep(2)
        print(f"\tYour choice is {player_choice.upper()} and CPU's choice is {cpu_choice}")
        # time.sleep(2)
        print("\tYou Won!!!\n")
        player_win = player_win + 1

    elif player_choice.upper() not in ["ROCK","PAPER","SCISSOR"]:
        time.sleep(2)
        print(f"\t{player_choice.upper()} is an invalid choice please enter correct choice ")

    else:
        cpu_choose()
        time.sleep(2)
        print(f"\tYour choice is {player_choice.upper()} and CPU's choice is {cpu_choice}")
        # time.sleep(2)
        print("\tYou Lost!!!")
        cpu_win = cpu_win + 1

    time.sleep(2)
    str_1 = f"\tYour points : {player_win} \t Cpu points : {cpu_win} \t tie points : {tie} times"
    return str_1


i = 0
while i <= 10:

    # choice = int(input("\n1.Start\n2.End:"))

    if i < 10:
        print(game())
        i = i + 1
        print(f"\t{10 - i} turns remaining")

    elif i == 10:
        print("Calculating Total Score...")
        if player_win > cpu_win:
            time.sleep(4)
            print(f"\n\tYou won by lead of {player_win - cpu_win} points")
        elif cpu_win > player_win:
            time.sleep(4)
            print(f"\n\tCPU won by the lead of {cpu_win - player_win} points")
        else:
            time.sleep(4)
            print("\tIts a tie")

        print("\t\t***** Thanks for playing *****")
        break
