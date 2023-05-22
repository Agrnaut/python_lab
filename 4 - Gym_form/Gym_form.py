from People import People

def validate_age():
    new_age = int(input("Inform your new age:"))
    if(new_age < age):
        print("Invalid age")
    elif(age < 21 and new_age >= 21):
        growth = 21 - age
        new_height = height + round((growth * 0.005), 2)
        human.grow_tall(new_height)
        human.get_older(new_age)
    elif(age < 21 and new_age < 21):
        growth = (new_age - age)
        new_height = height + round((growth * 0.005), 2)
        human.grow_tall(new_height)
        human.get_older(new_age)
    else:
        human.get_older(new_age)

def change_form():
    value = ((int(input("What information you would like to change on your form?\n [1]Age  [2]Weight  [3]Height"))))
    if (value == 1):
        validate_age()
    elif(value == 2):
        human.fatten(int(input("Inform your new weight:")))
    else:
        human.grow_tall(float(input("Inform your new Height:")))

def menu():
    option = int(input("What you would like to do?:\n [1]Show your form  [2]Change Form  [3]Finish sign up:\n[Opção]:"))
    if(option == 1):
        return 1
    elif(option == 2):
        return 2
    else:
        return 3


print("Welcome to the Gym, No class no gain"
      "\nPlease fill up the form:")

end_of_loop = False

name = input("Name:")
age = int(input("Age:"))
weight = float(input("Weight [in Kilograms]:"))
height = float(input("Height [in Meters]:"))
human = People(name, age, weight, height)

while (not end_of_loop):

    question = menu()
    if(question == 1):
        print(f"Name: {human.show_person[0]}\n"
              f"Age: {human.show_person[1]}\n"
              f"Weight: {human.show_person[2]}KG\n"
               f"Height: {human.show_person[3]}M")

    elif(question == 2):
        change_form()

    else:
        print("Thanks for selection our services:")
        break