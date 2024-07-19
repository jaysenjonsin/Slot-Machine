MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def main():
  balance = deposit()
  lines = get_number_of_lines()

  while True:
    bet = get_bet()
    total_bet = bet + lines
    if total_bet > balance:
      print(f"you do not have enough to be that amount. Your current balance is ${balance}")
    else:
      break

  print("you are betting " +str(bet) + " on " + str(lines) + ". Total bet is equal to " + str(total_bet))


main()
