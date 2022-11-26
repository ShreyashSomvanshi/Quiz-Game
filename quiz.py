questions = ("1. How many elements are in the periodic table?: ",
             "2. Which animal lays the largest eggs?: ",
             "3. What is the most abundant gas in Earth's atmosphere?: ",
             "4. How many bones are in human body?: ",
             "5. Which planet in the solar system is the hottest?: ")

options = (("A. 116","B. 118","C. 117","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("B","D","A","A","B")

guesses = []

score = 0

qnum = 0

for question in questions:
    print("--------------------------------------------------")
    print(question)
    for option in options[qnum]:
        print("\t",option)
        
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[qnum]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[qnum]} is the correct answer")
    qnum+=1
    
print("\n")
print("--------------------------------------------------")
print("\t\t RESULTS")
print("--------------------------------------------------")

print("Answers: ",end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions)*100)
print(f'You score is {score}% !')