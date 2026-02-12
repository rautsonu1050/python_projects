
#Another  way


# quiz game using list of dictionaries
questions= [
    { 
         "question" : "What is the Capital of India?",
        "Options"  :["A. Mumbai","B. Delhi","C. Kolkata","D. Chennai"],
        "answer"   : "B"
    },
    {
         "question" : "Which language is used to web-development?",
        "Options"  :["A. Python","B. Java","C. HTML","D. C++"],
        "answer"   : "C"
        
    },
    {
            "question" : "What is 5+3?",
        "Options"  :["A. 8","B. 9","C. 10","D. 11"],
        "answer"   : "A"
    }
]

score= 0  # variable to save user score
print("Wel-Come to  the Quize Game!")
print("==============================")

# loop through each question in the list of dictionaries
for q in questions:
    print("\n" +q["question"])
    for option in q["Options"]:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D) : ") .upper()
    if user_answer == q["answer"]:
        print("CORRECT!")
        score+=1
    else:
        # if the answer is incorrect, print WRONG
        print("WRONG!")
print("\n Quiz Complete!")
print("You Score: ",score,"/" , len(questions))  # print user score and total number of questions
        


