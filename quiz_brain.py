import re
from helper_functions import print_green, print_red, print_yellow


class QuizBrain:
    """
    A class representing the quiz logic

    Attributes:
        ------------------------------------------
        question_list: a quiz bank of Question objects
        total_num_questions: an int representing the total number of questions
        question_idx: index of the current question in the list
        score: int representing the user's score
        ------------------------------------------

    Methods:
        ------------------------------------------
        still_has_questions(): -> bool
            returns True if there are still questions left that the suer hasn't answered
        check_answer(user_answer:list, correct_answer_list: list) -> book
            static method that returns True if the user correctly answers all answers in the correct_answer_list
        next_question(): -> None
            displays the next question on the screen, prompts the user for an answer, updates the score at the end"
    """
    def __init__(self, question_list):
        self.question_list = question_list
        self.total_num_questions = len(question_list)
        self.question_idx = 0
        self.score = 0

    def still_has_questions(self) -> bool:
        """Checks if there still are questions the user hasn't answered"""
        return self.question_idx < self.total_num_questions

    @staticmethod
    def _check_answer(user_answer: list, correct_answers: list) -> bool:
        """Checks if the user entered the correct answer"""
        if len(user_answer) != len(correct_answers):
            return False
        for answer in user_answer:
            if answer not in correct_answers:
                return False
            return True

    def next_question(self) -> None:
        """Displays the next question on the screen, prompts the user for an answer, updates the score at the end"""
        # Get current question and update the question number index
        question = self.question_list[self.question_idx]
        self.question_idx += 1

        # Creates variables: regex to check user input, message that tells user if the question has one or more answers
        pattern = rf"^[{''.join(question.answer_options)}](?:,\s*[{''.join(question.answer_options)}])*$"
        if not question.has_multiple_answers:
            message = "There is only ONE correct answer. Please choose one of the options below. "
        else:
            message = ("There are MULTIPLE correct answers. "
                       "Please enter the answers you think are correct with commas between them (e.g. 'a, b, c'). ")

        # Display the question along and the possible answers
        print(f"Q{self.question_idx}:  {question.question_text}")
        for idx, answer in enumerate(question.answers.values()):
            print(f"{question.answer_options[idx]}) {answer}")
        print_yellow(message)

        # Prompt user to enter answer, check answer against pattern
        while True:
            user_answers = input("Enter your answer here: ").strip()
            if not re.search(pattern, user_answers):
                print("Sorry, that's not a valid answer. Please try again")
            else:
                break

        # Check if user answer is true, and update score
        user_answers = list(set([item.strip() for item in user_answers.split(",")]))
        is_answer_true = self._check_answer(user_answers, question.correct_answers_options)
        if is_answer_true:
            self.score += 1
            print_green(f"Well done! Your score is {self.score}/{self.total_num_questions}\n")
        else:
            print_red(f"Sorry. That's not correct. Your score is {self.score}/{self.total_num_questions}\n")
