
#python quize game :

# Wrte questin and options in tuple and answers in another tuple
questions = ("1. How many element arein periodic table? " , 
            "2. Which animal lays the largest eggs?",
            "3. How many bone in human body?",
            "4. What is the full form of RAM?",
            "5. Which device is used to input data into a computer?",
            "6. Which of the following is an example of system software?" )
        


options = (("A. 116" , "B.117","C.118","D.119") , 
           ("A. Whale" , "B.Crocodile","C.Elephant","D.Ostrich"), 
           ("A. 206" , "B.207","C.208","D.209"),
           ("A. Random Access Memory" , "B.Read Access Memory","C. Readily Available Memory","D. Random Available Memory"),
           ("A. Printer" , "B. Monitor","C. Keyboard","D.Speaker"),
           ("A.  Microsoft Excel" , "B. Windows 10","C. Google Chrome","D.Adobe Reader"))
            
answers = ("C", "D","A","A","C","B")  #vsave answers in tuple
guesses=[] # save user guesses in list
score=0  # save user score in variable
questions_num = 0  # save question number in variable

print()

for question in questions:
    print("---------------------------------------------------------")
    print(question)
    # print options for each question
    for option in options [questions_num]:
     print(option)

    guess = input("Enter (A, B , C, D) : ").upper()
    guesses.append(guess)
    # check if the guess is correct and update score
    if guess == answers[questions_num]:
     
      print("CORRECT!")
      score+=1
    else:
     # if the guess is incorrect, print the correct answer
     print("INCORRECT!")
     print(f"{answers[questions_num]} is the correct answer ")
    questions_num+=1
    
print("-------------------------------")
print("           RESULT             ")
print("-------------------------------")
print("answer :" ,end=" ")
# print correct answers and user guesses
for answer in answers:
  print(answer,end=" ")
print()
print("Guesses :" ,end=" ")
for guess in guesses:
  # print user guesses
  print(guess,end=" ")
print()
# calculate and print user score
score = float(score/len(questions)*100)
# print user score with 2 decimal places
print(f"Your Score is : {score :.2f}% ")
