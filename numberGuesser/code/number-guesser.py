import random

print("""
================================
     NUMBER GUESSER
================================
""")

def main():
     maxNumber = int(input("\nWhat do you want the highest number to be: "))
     randomNumber = random.randint(1, maxNumber);
     wrongCounter = 1

     userInput = input("\nGuess a number between 1 and %d: " %maxNumber)
     if userInput == "gg":
               print("The Lucky number was %d \n" %randomNumber)
               playAgain = input("Do you wanna play again? (y or n): ")
               if playAgain == "y":
                    main()
               else:
                    return

     while int(userInput) != randomNumber:

          if userInput == "gg":
               print("The Lucky number was %d \n" %randomNumber)

               playAgain = input("Do you wanna play again? (y or n): ")
               if playAgain == "y":
                    main()
               else:
                    break
                    return

          elif (randomNumber - 5) <= int(userInput) <= (randomNumber + 5):
               print("You are so close, Try Again\n")
          else:
               print("Nope, Try Again\n")

          wrongCounter = wrongCounter + 1

          if (wrongCounter % 10) == 0:
               print("\nType in `gg` if you give up and want to know the number\n")

          userInput = input("Guess a number between 1 and %d: " %maxNumber)
          if userInput == "gg":
               print("The Lucky number was %d \n" %randomNumber)
               playAgain = input("Do you wanna play again? (y or n): ")
               if playAgain == "y":
                    main()
               else:
                    break
                    return
     

     else:
          print("You guessed the right number in %d try(s)! \n" %wrongCounter)
          playAgain = input("Do you wanna play again? (y or n): ")
          if playAgain == "y":
               main()
          else:
               return

main()