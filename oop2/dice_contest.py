from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
swapper_score = 0
loaded_dice_score = 0
number_of_games = 100000
game_number = 0
print("simulation running")
print("==================")
while game_number < number_of_games:
    swapper.roll()
    loaded_dice.roll()

    swapper.cheat()
    loaded_dice.cheat()

    if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
        pass
    elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
        swapper_score += 1
    else:
        loaded_dice_score += 1
    game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
if swapper_score == loaded_dice_score:
    print("Game was drawn")
elif swapper_score > loaded_dice_score:
    print("Swapper won most games")
else:
    print("Loaded dice won most games")

