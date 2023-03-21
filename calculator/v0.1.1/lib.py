# --- MADE BY RYAN --- #

def add():
  in1 = float(input("Enter First Number: "))
  in2 = float(input("Enter Second Number: "))
  answer = in1 + in2
  print(f"{str(in1)} + {str(in2)} = {str(answer)}")

def sub():
  in1 = float(input("Enter First Number: "))
  in2 = float(input("Enter Second Number: "))
  answer = in1 - in2
  print(f"{str(in1)} - {str(in2)} = {str(answer)}")

def multi():
  in1 = float(input("Enter First Number: "))
  in2 = float(input("Enter Second Number: "))
  answer = in1 * in2
  print(f"{str(in1)} * {str(in2)} = {str(answer)}")

def div():
  in1 = float(input("Enter First Number: "))
  in2 = float(input("Enter Second Number: "))
  answer = in1 / in2
  print(f"{str(in1)} / {str(in2)} = {str(answer)}")

def area_square():
  in1 = float(input("Enter Length: "))
  answer = in1 * in1
  print(f"{str(in1)} * {str(in1)} = {str(answer)}")

def perimeter_square():
  in1 = float(input("Enter Length: "))
  answer = in1 * 4
  print(f"{str(in1)} * 4 = {str(answer)}")

def check_continue():
  yes_option = ["Yes", "Y"]
  no_option = ["No", "N"]
  user_in = input("Continue? [Y/N] ")
  if user_in.title() in yes_option or no_option:
    if user_in.title() in yes_option:
      user()
    elif user_in.title() in no_option:
      exit()
    else:
      print("Please enter Yes, No, Y or N.")
      check_continue()
  else:
    print("Please enter Yes, No, Y or N.")
    check_continue()

def user():
  try:
    maincmd = int(input('''
    Enter 1 for Operations
    Enter 2 for Area & Perimeter
    >>> '''))
  except ValueError:
    print("Value Error. Try again!")
    check_continue()
  else:
    if maincmd == 1:
      try:
        cmd = int(input('''
        Enter 1 for Addition
        Enter 2 for Subtraction
        Enter 3 for Multiplication
        Enter 4 for Division
        >>> '''))
      except ValueError:
        print("Valur Error. Try again!")
        check_continue()
      else:
        if cmd == 1:
          add()
          check_continue()
        elif cmd == 2:
          sub()
          check_continue()
        elif cmd == 3:
          multi()
          check_continue()
        elif cmd == 4:
          div()
          check_continue()
        else:
          print("This service is currently unavailable. Try another service.")
          check_continue()
    elif maincmd == 2:
      try:
        cmd = int(input('''
        Enter 1 for Area of Square
        Enter 2 for Perimeter of Square
        >>> ''')) 
      except ValueError:
        print("Value Error. Try again!")
        check_continue()
      else:
        if cmd == 1:
          area_square()
          check_continue()
        elif cmd == 2:
          perimeter_square()
          check_continue()
        else:
          print("This service is currently unavailable. Try another service.")
          check_continue()
    else:
      print("This service is currently unavailable. Try another service.")
      check_continue()
