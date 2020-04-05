'''The Lizard-Spock Expansion'''


def choice():
    options = ['ROCK', 'PAPER', 'SCISSOR', 'LIZARD', 'SPOCK']
    print(options)
    playersOptions = input("Choose Sheldon's and Raj's options, in sequence, separated by a space: ").split()
    for i in playersOptions:
        if i.upper() not in options:
            print("Invalid choice, try again!")
            playersOptions = input("Choose Sheldon's and Raj's options, in sequence, separated by a space: ").split()
    return playersOptions


def result(choiceList):
    if choiceList[0].upper() == "ROCK" and (choiceList[1].upper() == "SCISSOR" or choiceList[1].upper() == "LIZARD"):
        finalResult = "Bazinga!"

    elif choiceList[0].upper() == "PAPER" and (choiceList[1].upper() == "ROCK" or choiceList[1].upper() == "SPOCK"):
        finalResult = "Bazinga!"

    elif choiceList[0].upper() == "SCISSOR" and (choiceList[1].upper() == "PAPER" or choiceList[1].upper() == "LIZARD"):
        finalResult = "Bazinga!"

    elif choiceList[0].upper() == "LIZARD" and (choiceList[1].upper() == "PAPER" or choiceList[1].upper() == "SPOCK"):
        finalResult = "Bazinga!"

    elif choiceList[0].upper() == "SPOCK" and (choiceList[1].upper() == "ROCK" or choiceList[1].upper() == "SCISSOR"):
        finalResult = "Bazinga!"

    elif choiceList[0].upper() == choiceList[1].upper():
        finalResult = "Again!"

    else:
        finalResult = "Raj Cheated!"

    return finalResult

def main():
    T = int(input("How many times would you like to play Rock, Paper, Scissors, Lizard, Spock? "))
    if T >= 1 and T <= 100:
        #print(T)
        for i in range(0, T):
            i = i + 1
            list = choice()
            result(list)
            print("Caso #",i,": ", result(list))

    else:
        print("Ivalid value! Your value must be between 1 and 100. Try again: ")
        main()
        print("Meu grupo é uma batata doce")

main()
