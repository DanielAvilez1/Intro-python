# imports


# globals




# funtions
def print_menu():
    print("-------------------------")
    print("  Pycal 3000    ")
    print("-------------------------")

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    
    print("[x] Leave")


# plain instructions
option = ""
while option != "x":
    print_menu()
    option = input("Please select an option: ")
    if option == "x":
        break # break means end of loop
    num1 = float(input("Please provide num1: "))
    num2 = float(input("please provide num2: "))

    if option == "1":
        result = num1 + num2

    elif option == "2":
        result = num1 - num2

    elif option == "3":
        result = num1 * num2

    elif option == "4":
        if num2 == 0:
            print("Try again")
            result = "Error wack"
        else:
            result = num1 / num2


    print ("the result is : " + str(result)) 
    input("press Enter to continue...")
    print ("")  
    print ("")  
    print ("")  

print("Thank you come again!")
