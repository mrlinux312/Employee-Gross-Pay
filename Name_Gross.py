print("Name and Gross Pay Program")
print()

gross_tot = 0
emp_tot = 0

start = input("Would you like to start the program? yes/no?: ").lower()


if start == "yes":
  while True:
    lastname = input("Enter last name of employee: ")
    hrs = float(input("Enter hours worked: "))
    payrate = float(input("Enter rate of pay for employee: "))
  
       
    if hrs > 40:
          gross = (payrate * 40) + ((hrs - 40) * (payrate * 1.5))
    if hrs <= 40:
          gross = hrs * payrate
       
    print(f"Employee last name:{lastname} \nGross Pay: {gross}") 
   
    gross_tot += gross
    emp_tot += 1
  
  
  
    another_emp = input("Would you like to enter another employee? yes/no?").lower()
    if another_emp == "no":
     break
avg = gross_tot / emp_tot
print(f"Gross Pay Sum: {gross_tot:.2f} \nEmployee Count: {emp_tot} \nAverage Pay: {avg:.2f}")