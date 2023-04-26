# Python quiz game

QUESTIONS = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

OPTIONS = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

ANSWERS = ("C", "D", "A", "A", "B")


class QuizResult:
  score = 0
  guesses = []


def main():
    
  result = ask_questions()
  print_results(result)

def ask_questions():  
  
  #guesses = []
  #score = 0
  question_num = 0

  result = QuizResult()
  
  for question in QUESTIONS:

    print("----------------------")
    print(question)
    for option in OPTIONS[question_num]:
      print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    #guesses.append(guess)
    result.guesses.append(guess)
    if guess == ANSWERS[question_num]:
      #score += 1
      result.score += 1
      print("CORRECT!")
    else:
      print("INCORRECT!")
      print(f"{ANSWERS[question_num]} is the correct answer")
    question_num += 1

  return result



def print_results(result):
  
  print("----------------------")
  print("       RESULTS        ")
  print("----------------------")
  
  print("answers: ", end="")
  for answer in ANSWERS:
      print(answer, end=" ")
  print()
  
  print("guesses: ", end="")
  for guess in result.guesses:
      print(guess, end=" ")
  print()
  
  score = int(result.score / len(QUESTIONS) * 100)
  print(f"Your score is: {score}%")


if __name__ == "__main__":
    main()
    


