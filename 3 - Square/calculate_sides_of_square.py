from Square import Square

def want_to_continue():
    value = ((int(input("Would you like to get back to main menu?\n [1] Yes\n [2] No\n"))))
    if (value == 1):
        return False
    else:
        return True



print("Welcome student")


exercise_square = Square(float(input("Insert a size for the sides for your square: ")))


end_of_loop = False
while(not end_of_loop):

    question = int(input(("You would like to "
          "\n[1] Show sides sizes "
          "\n[2] Calculate the are of your square"
          "\n[3] Change the sides of your square"
                          "\nOption: ")))

    # fim_de_loop = quer_continuar()

    for choice in range(3):
        if(question == 1):
            print(f"The size of sider of your square is {exercise_square.size}")
            end_of_loop = want_to_continue()
            break
        elif(question == 2):
            print(exercise_square.calculate())
            end_of_loop = want_to_continue()
            break
        elif(question == 3):
            exercise_square.new_size(float(input("type a new size for the sides of your square: ")))
            end_of_loop = want_to_continue()
            break
        else:
            print("Invalid option")