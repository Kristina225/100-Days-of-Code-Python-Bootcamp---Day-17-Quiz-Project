import requests
import json
import os
from dotenv import load_dotenv
from question_bank import QuestionBank
from quiz_brain import QuizBrain

load_dotenv()

API_ENDPOINT = "https://quizapi.io/api/v1/questions"
HEADERS = {
    "X-Api-Key": os.getenv("API_KEY")
}

LEVELS = ["easy", "medium", "hard"]


def main():
    """Launches the Quiz application."""
    print("Welcome to the quiz! We'll learn so much together.")
    while True:
        level = input(f"Please choose your difficulty level.\n"
                      f"Enter one of the following: {', '.join(LEVELS)}\n")
        if level in LEVELS:
            break
    questions = _get_questions({"level": level})
    if not questions:  # the API call has failed
        return
    question_bank = QuestionBank().create_question_bank(questions)
    quiz_brain = QuizBrain(question_bank)
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()
    print(f"You've completed the quiz.\n"
          f"Your final score was: {quiz_brain.score}/{quiz_brain.total_num_questions}")


def _get_questions(params: dict) -> dict or None:
    """Fetch questions from API. Return data or None if an error occurs"""
    try:
        response = requests.get(API_ENDPOINT, headers=HEADERS, params=params)
        data = response.json()
    except requests.exceptions.RequestException:
        print("Sorry, we couldn't fetch the quiz questions at the moment. Please try again later.")
        return None
    except ValueError:
        print("Sorry, an error occurred with the questions processing. Please try again later.")
        return None
    else:
        with open("questions.json", "w") as file:
            json.dump(data, file, indent=4)
        return data


if __name__ == "__main__":
    main()
