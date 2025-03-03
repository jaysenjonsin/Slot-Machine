import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}

def check_winnings(columns, lines, bet,values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
      else:
        winnings += values[symbol] * bet
        winning_lines.append(line + 1)
  
  return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count): #dont need the variable so just use _
      all_symbols.append(symbol)

  columns = [[],[],[]]
  for col in range(cols):
    column = []
    current_symbols = all_symbols[:] #slice operator, copying current_symbols so we dont have repeats when generating randoms
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
    
    columns.append(column)
  
  return columns

def print_slot_machine(columns):
  #transposing
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end = " | ") #end tells print statement what to end line on
    else:
      print (column[row], end = "")

    print() #prints new line character '\n' at end of empty print statment

def deposit():
  while True:
    amount = input("What would you like to deposit? $")
    if amount.isdigit():  # if valid number, convert to integer
      amount = int(amount)
      if amount > 0:
        break
      else:
        print('Amount must be greater than 0.')
    else:
      print('Please enter a number')

  return amount    

def get_number_of_lines():
  while True:
    lines = input("enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("enter a valid number of lines")
    else:
      print("please enter a number")

  return lines

def get_bet():
  while True:
    amount = input("what would you like to bet on each line?")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print("amount must be between " + str(MIN_BET) + "-" + str(MAX_BET)) 
  return amount

def spin(balance):
  lines = get_number_of_lines()

  while True:
    bet = get_bet()
    total_bet = bet + lines
    if total_bet > balance:
      print(f"you do not have enough to be that amount. Your current balance is ${balance}")
    else:
      break

  print("you are betting " +str(bet) + " on " + str(lines) + ". Total bet is equal to " + str(total_bet))

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
  print(f"you won ${winnings}.")
  print(f"you won on lines: ", *winning_lines) #splat operator passes all lines from winning_lines to print function
  return winnings - total_bet


def main():
  balance = deposit()
  while True:
    print(f"Current balance is ${balance}")
    answer = input("Press enter to spin(q to quit)")
    if answer == "q":
      break
    balance += spin()

  print(f"you left with ${balance}")
  
  


  

main()
