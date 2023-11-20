#importing libraries
import os
import random
from colorama import *
from colorama import Fore, Back, Style



def quiz():
    Fore.RESET
    #auto reset doesn't work :(
    score = 1
    #intro
    os.system('cls')
    print('''Welcome to the quiz! You will be asked 10 questions and will be given 4 possible answers for each question.\nYou will be given 10 points for each correct answer and will lose 10 points for each incorrect answer. \nIf your score reaches 0 or below, you will fail the quiz and the program will exit. \nYou will be asked to press enter to continue after each question. \nIf you get a answer close to the correct one you will be given 1-5 points''')
    print("Good luck!")
    print("")
    print("")
    print("Are you ready?")
    quiz_begin = input(Fore.LIGHTGREEN_EX + "Enter y for yes or n for no: " + Fore.RESET)
    if quiz_begin == "y" or quiz_begin == "Y":
        os.system('cls')
        name = input("What is your name? ")
        os.system('cls')
        print("Hi " + name +" Let's begin!" + Fore.RESET)
    elif quiz_begin == "n" or quiz_begin == "N":
        print(Fore.RESET + "Goodbye!")
        exit()
    elif quiz_begin == "exit" or quiz_begin == "Exit":
        print(Fore.RESET + "Goodbye!")
        exit()
    else:
        print(Fore.RED + "Invalid input. I Said use y or n!" + Fore.RESET)
        exit()

    #questions

    print(Fore.RESET + "Question 1")
    print("What is the capital France?")
    print("A. Paris,  B, London, C, Berlin, D, Madrid")
    answer = input("Enter your answer a, b, c or d: ")
    if answer == "a" or answer == "A":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer == "b" or answer == "B" or answer == "c" or answer == "C" or answer == "d" or answer == "D":
        print(Fore.RED + "Incorrect! The correct anwser was A. Paris" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')

    
    print("Question 2")
    print("What is the capital of China?")
    print("A. Hong Kong, B. Shanghai, C. Beijing, D. Shenzhen")
    answer2 = input("Enter your answer a, b, c or d: ")
    if answer2 == "c" or answer2 == "C":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer2 == "b" or answer2 == "B":
        print(Fore.YELLOW + "Not quite. The correct answer is C. Beijing. Shanghai is the largest city in China" +Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer2 == "a" or answer2 == "A" or answer2 == "d" or answer2 == "D":
        print(Fore.RED + "Incorrect! The correct answer is C. Beijing" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')


    print("Question 3")
    print("What is the largest river in China?")
    print("A. Pearl River, B. Yellow River, C. Yangtze River, D. Mekong")
    answer3 = input("Enter your answer a, b, c or d: ")
    if answer3 == "c" or answer3 == "C":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer3 == "b" or answer3 == "B":
        print(Fore.YELLOW + "Not quite. The correct answer is C. Yangtze. The Yellow River is the second largest river in China" +  Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer3 == "a" or answer3 == "A" or answer3 == "d" or answer3 == "D":
        print(Fore.RED + "Incorrect! The correct answer is C. Yangtze" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')

    print("Question 4")
    print("What is BRICS?")
    print("A. A group of countries with the largest military, B. A group of countries with the largest populations, C. A group of countries with the largest land area, D. A group of countries with the largest economies")
    answer4 = input("Enter your answer a, b, c or d: ")
    if answer4 == "d" or answer4 == "D":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer4 == "b" or answer4 == "B":
        print(Fore.YELLOW + "Not quite. The correct answer is D. A group of countries with the largest economies. BRICS stands for Brazil, Russia, India, China and South Africa" + Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer4 == "a" or answer4 == "A" or answer4 == "c" or answer4 == "C":
        print(Fore.RED + "Incorrect! The correct answer is D. A group of countries with the largest economies" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')

    print("Question 5")
    print("Which country is notrotious for its censorship, human rights violation and imprisonments of its citizens?")
    print("A. China, B. North Korea, C. Russia, D. Iran")
    answer5 = input("Enter your answer a, b, c or d: ")
    if answer5 == "b" or answer5 == "B":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer5 == "a" or answer5 == "A":
        print(Fore.YELLOW + "Not quite. The correct answer is B. North Korea. China is also known for its censorship, human rights violation and imprisonments of its citizens but not as much as North Korea" + Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer5 == "c" or answer5 == "C" or answer5 == "d" or answer5 == "D":
        print(Fore.RED + "Incorrect! The correct answer is B. North Korea" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')
    
    wait = input("Press enter to continue")
    print(Fore.LIGHTYELLOW_EX + "There is more questions, do you wish to continue?" + Fore.RESET)
    continue_quiz = input(Fore.GREEN + "Enter y for yes or n for no: " + Fore.RESET)
    if continue_quiz == "y" or continue_quiz == "Y":
        print("Ok, let's continue!")
        wait = input("Press enter to continue")
        os.system('cls')
    elif continue_quiz == "n" or continue_quiz == "N":
        print("Ok, goodbye!")
        os.system('cls')
        print("Thank you for participating in the quiz!")
        print(Fore.LIGHTCYAN_EX + "Your final score is: {}".format(score) + Fore.RESET)
        #writes score to score file and add new line for each person
        #open score file
        score_file = open("score.txt", "a")
        #write score to score file
        score_file.write(name + " " + str(score) + "\n")
        #close file
        score_file.close()

        wait = input("Press enter to exit")
        exit()
    else:
        print(Fore.RED + "Invalid input. I Said use y or n! I'm going to automatically procceed" + Fore.RESET)
        wait = input("Press enter to continue")
        os.system('cls')


    print("Question 6")
    print("What is the largest country in the world?")
    print("A. Russia, B. China, C. USA, D. Canada")
    answer6 = input("Enter your answer a, b, c or d: ")
    if answer6 == "a" or answer6 == "A":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer6 == "b" or answer6 == "B":
        print(Fore.YELLOW + "Not quite. The correct answer is A. Russia. China is the 4th largest country in the world" + Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer6 == "c" or answer6 == "C" or answer6 == "d" or answer6 == "D":
        print(Fore.RED + "Incorrect! The correct answer is A. Russia" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')

    print("Question 7")
    print("Which country has the biggest population in the world in 2020?")
    print("A. India, B. China, C. USA, D. Russia")
    answer7 = input("Enter your answer a, b, c or d: ")
    if answer7 == "b" or answer7 == "B":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer7 == "a" or answer7 == "A":
        print(Fore.YELLOW + "Not quite. The correct answer is B. China. India wasn't most populated country in the world in 2020" + Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer7 == "c" or answer7 == "C" or answer7 == "d" or answer7 == "D":
        print(Fore.RED + "Incorrect! The correct answer is B. China" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')

    print("Question 8")
    print("Which country has the largest economy in the world in 2020?")
    print("A. China, B. USA, C. Japan, D. Germany")
    answer8 = input("Enter your answer a, b, c or d: ")
    if answer8 == "b" or answer8 == "B":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer8 == "a" or answer8 == "A":
        print(Fore.YELLOW + "Not quite. The correct answer is B. USA. China wasn't the largest economy in the world in 2020 it was the second largest" + Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer8 == "c" or answer8 == "C" or answer8 == "d" or answer8 == "D":
        print(Fore.RED + "Incorrect! The correct answer is B. USA" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)      
    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')

    print("Question 9")
    print("Which country has the largest army in the world?")
    print("A. USA  , B. India, C. Russia, D. China")
    answer9 = input("Enter your answer a, b, c or d: ")
    if answer9 == "d" or answer9 == "D":
        print(Fore.GREEN + "Correct!" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer9 == "a" or answer9 == "A":
        print(Fore.YELLOW + "Not quite. The correct answer is D. China. USA has the second largest army in the world but it has the largest military budget in the world" + Fore.RESET)
        score += random.randint(1,5)
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer9 == "c" or answer9 == "C" or answer9 == "b" or answer9 == "B":
        print(Fore.RED + "Incorrect! The correct answer is D. China" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    wait = input("Press enter to continue")
    if score <=0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
        exit()
    os.system('cls')

    print("Question 10")
    print("Which country has tried to apply to be part of the UN security council?")
    print("A. India, B. Brazil, C. Germany, D. Japan")
    answer10 = input("Enter your answer a, b, c or d: ")
    if answer10 == "a" or answer10 == "A":
        print(Fore.GREEN + "Correct! India has tried to apply for more than 5 times but has been rejected every time by each of the members" + Fore.RESET)
        score += 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer10 == "b" or answer10 == "B":
        print(Fore.YELLOW + "Not quite. The correct answer is A. India. Brazil has never tried to apply to be part of the UN security council" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    elif answer10 == "c" or answer10 == "C" or answer10 == "d" or answer10 == "D":
        print(Fore.RED + "Incorrect! The correct answer is A. India" + Fore.RESET)
        score -= 10
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
    else:
        print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
        score += 1
        print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)

    wait = input("Press enter to continue")
    if score <= 0:
        print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
    if score >= 80:
        print(Fore.GREEN + "You have passed the quiz!" + Fore.RESET)
        #give reward
        print("You have passed the quiz with a score of: {}".format(score)  + Fore.RESET)
        print("You have unlocked the secret reward! Have fun with a random score boost!")
        score += random.randint(1,20)
        print(Fore.LIGHTMAGENTA_EX + "Your score is now: {}".format(score) + Fore.RESET)


        #bonus questions, asks user if they want to have them,
        print("Would you like to answer some bonus questions? (You will fail the quiz if the score goes below 0, more points will be given, and you will also lose more if you get one incorrect.)")
        bonus = input("Enter y for yes or n for no: ")
        if bonus == "y" or bonus == "Y":
            print("Ok, here are some bonus questions!")
            print("Question 11")
            print("What is the capital of the USA?")
            print("A. Washington DC, B. New York, C. Los Angeles, D. Chicago")
            answer11 = input("Enter your answer a, b, c or d: ")
            if answer11 == "a" or answer11 == "A":
                print(Fore.GREEN + "Correct!" + Fore.RESET)
                score += 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer11 == "b" or answer11 == "B":
                print(Fore.YELLOW + "Not quite. The correct answer is A. Washington DC. New York is the largest city in the USA" + Fore.RESET)
                score += random.randint(2,10)
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer11 == "c" or answer11 == "C" or answer11 == "d" or answer11 == "D":
                print(Fore.RED + "Incorrect! The correct answer is A. Washington DC" + Fore.RESET)
                score -= 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            else:
                print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
                score += 1
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            wait = input("Press enter to continue")
            if score <= 0:
                print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
                exit()
            os.system('cls')


            print("Question 12")
            print("What is the capital of Australia?")
            print("A. Sydney, B. Melbourne, C. Brisbane, D. Canberra")
            answer12 = input("Enter your answer a, b, c or d: ")
            if answer12 == "d" or answer12 == "D":
                print(Fore.GREEN + "Correct!" + Fore.RESET)
                score += 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer12 == "b" or answer12 == "B":
                print(Fore.YELLOW + "Not quite. The correct answer is C. Canberra. Melbourne is the second largest city in Australia" + Fore.RESET)
                score += random.randint(2,10)
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer12 == "a" or answer12 == "A" or answer12 == "c" or answer12 == "C":
                print(Fore.RED + "Incorrect! The correct answer is C. Canberra" + Fore.RESET)
                score -= 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            else:
                print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
                score += 1
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            wait = input("Press enter to continue")
            if score <= 0:
                print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
                exit()
            os.system('cls')


            print("Question 13")
            print("What is the capital of Brazil?")
            print("A. Sao Paulo, B. Rio de Janeiro, C. Brasilia, D. Salvador")
            answer13 = input("Enter your answer a, b, c or d: ")
            if answer13 == "c" or answer13 == "C":
                print(Fore.GREEN + "Correct!" + Fore.RESET)
                score += 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer13 == "b" or answer13 == "B":
                print(Fore.YELLOW + "Not quite. The correct answer is C. Brasilia. Rio de Janeiro is the second largest city in Brazil" + Fore.RESET)
                score += random.randint(2,10)
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer13 == "a" or answer13 == "A" or answer13 == "d" or answer13 == "D":
                print(Fore.RED + "Incorrect! The correct answer is C. Brasilia" + Fore.RESET)
                score -= 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            else:
                print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
                score += 1
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            wait = input("Press enter to continue")
            if score <= 0:
                print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
                exit()
            os.system('cls')


            print("Question 14")
            print("What is the capital of South Africa?")
            print("A. Johannesburg, B. Pretoria, C. Cape Town, D. Bloemfontein")
            answer14 = input("Enter your answer a, b, c or d: ")
            if answer14 == "b" or answer14 == "B":
                print(Fore.GREEN + "Correct!" + Fore.RESET)
                score += 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer14 == "a" or answer14 == "A":
                print(Fore.YELLOW + "Not quite. The correct answer is B. Pretoria. Johannesburg is the largest city in South Africa" + Fore.RESET)
                score += random.randint(2,10)
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer14 == "c" or answer14 == "C" or answer14 == "d" or answer14 == "D":
                print(Fore.RED + "Incorrect! The correct answer is B. Pretoria" + Fore.RESET)
                score -= 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            else:
                print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
                score += 1
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            wait = input("Press enter to continue")
            if score <= 0:
                print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
                exit()
            os.system('cls')


            print("Question 15")
            print("What is the capital of Japan?")
            print("A. Tokyo, B. Kyoto, C. Osaka, D. Hiroshima")
            answer15 = input("Enter your answer a, b, c or d: ")
            if answer15 == "a" or answer15 == "A":
                print(Fore.GREEN + "Correct, but there is a saying that Japan doesn't really have a capital city." + Fore.RESET)
                score += 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer15 == "b" or answer15 == "B":
                print(Fore.YELLOW + "Not quite. The correct answer is A. Tokyo. Kyoto is the second largest city in Japan, but it was the capital of Japan before Tokyo" + Fore.RESET)
                score += random.randint(2,15)
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            elif answer15 == "c" or answer15 == "C" or answer15 == "d" or answer15 == "D":
                print(Fore.RED + "Incorrect! The correct answer is A. Tokyo" + Fore.RESET)
                score -= 20
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            else:
                print(Fore.RED + "Invalid input. I Said use a, b, c or d! only 1 point can be given" + Fore.RESET)
                score += 1
                print(Fore.LIGHTCYAN_EX + "Your score is: {}".format(score) + Fore.RESET)
            wait = input("Press enter to continue")
            if score <= 0:
                print(Fore.RED + "You have failed the quiz!" + Fore.RESET)
                exit()




        elif bonus == "n" or bonus == "N":
            print("Ok, no bonus questions for you then!")

        else:
            print(Fore.RED + "Invalid input. I Said use y or n! Sorry no bonus questions for you." + Fore.RESET)
            
            

    wait = input("Press enter to continue")




    #thank you for participating and display final score
    os.system('cls')
    print("Thank you for participating in the quiz!")
    print("Your final score is: {}".format(score))
    #write score to file and add new line for each person.
    #open file
    score_file = open("score.txt", "a")
    #write score to file
    score_file.write(name + " " + str(score) + "\n")
    #close file
    score_file.close()

    wait = input("Press enter to exit")



quiz()