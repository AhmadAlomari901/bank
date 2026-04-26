while True:

  print("********************Welcome to the local bank*********************")

  name = input("Username: ").strip()

  password = int(input("Password: "))

  #******************************Card number and info*****************************************
  c = card_number = "4545859674128452"
  formatted_card = f"{c[0:4]} {c[4:8]} {c[8:12]} {c[12:16]}"
  expiry_date = "12/28"
  code = 555
  #*******************************************************************************************
  current_balance = 0

   #if statment to check the username and password: 
  if name == "Ahmad" and password == 9090:
    print(f"Welcome to your account Mr.{name}")
  else :
    print("Username or password is incorrect: ")
    exit()

   #display services 
  print("\n**************************services*****************************\n")

  while True:
   print(   
    "> Add money to your account..............................PRESS( 1 )\n"
    "\n> Withdraw money.........................................PRESS( 2 )\n"
    "\n> Display my informaation................................PRESS( 3 )\n"
    "\n> Show my card info......................................PRESS( 4 )\n"
    "\n> Log out off your account...............................PRESS( 0 )\n" 
   )
   service_number = int(input(""))


   if service_number == 1:
      amount = float(input("Enter the amount: "))
      current_balance = current_balance + amount 
      print(f"Your balance now is: {current_balance:,.2f}")
   elif service_number == 2:
      take_money = float(input("Enter amount of money to withdraw: "))
      current_balance = current_balance - take_money
      print(f"Your balance now is: {current_balance:,.2f}")
   elif service_number == 0:
      print("Logged out successfully, see you later :) ")
      break
   elif service_number == 3:
      print(f"user's name is:  {name} ")
      print(f"Your password is: {password} ")
      print(f"Your current balance: {current_balance:,.2f}\n\n")
   elif service_number == 4:
       print(f"""
         _________________________________
        |  LOCAL BANK                     |
        |                                 |
        |  {formatted_card}            |
        |                                 |
        |  EXP: {expiry_date}      CVV: 555       |
        |  HOLDER NAME: {name.upper()}             |
        |_________________________________|
         """)
   else :
      print("Please select service from (0 to 4) only:")






    