import sys

def getInput() -> int:
################################################################################
# Validate Input
# Sum and convert to int
################################################################################
  
  print("Getting and Validating Input")

  args = sys.argv[1]
  print("Argument Type: ", type(args))
  print("Argument: ", args)

  if args.isspace():
    return -1

  if args.isdigit() == False:
    return -1
  
  if len(args) != 8:
    return -1
  
  n_list = []
  for char in args:
    n_list.append(int(char))

  print("\nDate as list:", n_list)

  return sum(n_list)

def digitOfLife(digits: int) -> int:
################################################################################
# Digit of Life Recursive
################################################################################
  
  print("Calculating Digit of Life")
  
  digits = str(digits)
  print(digits)

  if len(digits) == 1:
    return int(digits)
  
  l_sum = [int(x) for x in digits]

  print("List Digits:", l_sum)
  
  return digitOfLife(sum(l_sum))

 
  


