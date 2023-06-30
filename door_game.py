import random
from matplotlib import pyplot as plt

def print_separator():
    separator = "\u2500" * 30  # Using Unicode character "─" (U+2500) to create the line
    print(f"{separator}\n")

def display_strategy_scores(change_strategy_winning_rate, keep_strategy_winning_rate):
  plt.plot(change_strategy_winning_rate, color='green', label='Changing')
  plt.plot(keep_strategy_winning_rate, color='blue', label='Keeping')
  plt.xlabel('Rounds')
  plt.ylabel('Winning proportion')
  plt.legend()
  plt.show()

def play_door_game():
  doors = ['A', 'B', 'C']

  try:
      n_games = int(input("Type the number of rounds you want to play [int]: "))
  except ValueError:
      print("Please enter a valid integer.")

  change_strategy_winning_rate, keep_strategy_winning_rate = [], []
  n_games_change_strategy, n_games_keep_strategy = 0, 0
  winnings_change_strategy, winnings_keep_strategy = 0, 0


  for i in range(n_games):

    print(f"Execution {i+1}")
    print_separator()

    car_door = random.choice(doors)


    try:
      first_chosen_door = input("Enter the door you choose [A, B or C]: ")
    except ValueError:
      print("Please enter a valid door.")

    possible_doors_to_open = [d for d in doors if d != car_door and d != first_chosen_door]
    opened_door = random.choice(possible_doors_to_open)


    try:
      change_door_answer = input(f'The presenter has opened door {opened_door}. Do you want to change your choice? [Y or N] ')
    except ValueError:
      print("Please enter a valid answer.")

    if(change_door_answer == 'N'):

      n_games_keep_strategy += 1
      if(car_door == first_chosen_door):
        winnings_keep_strategy =+ 1
      keep_strategy_winning_rate.append(winnings_keep_strategy/n_games_keep_strategy)

    else:

      n_games_change_strategy += 1
      if(car_door != first_chosen_door):
        winnings_change_strategy =+ 1
      change_strategy_winning_rate.append(winnings_change_strategy/n_games_change_strategy)

  display_strategy_scores(change_strategy_winning_rate, keep_strategy_winning_rate)

  print(change_strategy_winning_rate)
  print(keep_strategy_winning_rate)

def main():
    play_door_game()

if __name__ == "__main__":
    main()

