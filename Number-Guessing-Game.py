import random

def number_guessing_game():
    random_number = random.randint(1,10)
    
    while True:
        try:
            guss = int(input("Guss The Number Between 1 to 10: "))
            if guss <= 10 :
                if guss == random_number :
                    print(" Correct ")
                    break
                print(" Wrong NT try again ")
        except ValueError:
            print(" Invalid input I SAid NUMBERRR")
            
        


if __name__ == "__main__":
    number_guessing_game()