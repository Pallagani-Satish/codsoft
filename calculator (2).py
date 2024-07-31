def calculator():
   
   print("Select operation.")
   print("1.Addition(+)")
   print("2.Subtraction(-)")
   print("3.Multiplication(*)")
   print("4.Division(/)")
   print("5.ModuloDivision(%)")

   while True:

    #Prompts the user for input 
     users_choice=input("Enter your choice:")
   
     if users_choice in ('1','2','3','4','5'):
      
      n1 = float(input("Enter your First Number: "))
      n2 = float(input("Enter your Second Number: "))

      if users_choice=='1':

      #Performs Adittion Operation  
        print("{} + {} = ".format(n1, n2))
        print(n1 + n2)
        print("\n")

      elif users_choice=='2':

      #Performs Subtraction Operation   
         print("{} - {} = ".format(n1, n2))  
         print(n1 - n2)
         print("\n")

      elif users_choice=='3':

      #Performs Multiplication Operation   
         print("{} * {} = ".format(n1, n2))
         print(n1 * n2)   
         print("\n")

      elif users_choice=='4':

      #Performs Division Operation   
         print("{} / {} = ".format(n1, n2))
         print(n1 / n2)
         print("\n")

      elif users_choice=='5':

      #Performs ModuloDivision Operation   
         print("{} % {} = ".format(n1, n2)) 
         print(n1 % n2) 
         print("\n")  

      next_calculation=input("Do you want to continue[y/n]:")       
      if next_calculation=='n':
         break

     else:
       print("Wrong Choice")  

calculator()    