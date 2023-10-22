from typing import List, Any


class Question:
    """
    A class modeling a Question

    Attributes:
        ------------------------------------------
        question_text: str containing the question
        answers: dict representing the possible answers
        answer_options: list containing the keys of the answers dict (lowercase alphabet letters)
        correct_answers: dict representing the correct answers
        correct_answers_options: list containing the keys of the correct_answers dict (lowercase alphabet letters)
        has_multiple_answers: bool (True if Question has multiple correct answers, False otherwise)
        -------------------------------------------
    """
    def __init__(self, question: str, answer_options_data: dict, answer_options_letters: list,
                 correct_options_data: dict, correct_option_letters: list, has_multiple_answers: bool):
        self.question_text = question
        self.answers = answer_options_data
        self.answer_options = answer_options_letters
        self.correct_answers = correct_options_data
        self.correct_answers_options = correct_option_letters
        self.has_multiple_answers = has_multiple_answers


class QuestionBank:
    """
    A composite class that creates and contains a list of Question objects

    Attributes:
        ------------------------------------------
        questions_bank: list of Question objects
        ------------------------------------------

    Methods:
        ------------------------------------------
        create_question_bank(question: list) -> list:
            takes in a list of dictionaries and returns a list of Question objects
        ------------------------------------------
    """
    def __init__(self):
        self.questions_bank = []

    def create_question_bank(self, questions: list[dict]) -> list[Question]:
        """Takes in a list of dictionaries and creates a list of Question objects"""
        for question_data in questions:
            # Get all relevant data from the questions list of dicts
            question = question_data["question"]
            answers_options_data = {k: v for (k, v) in question_data["answers"].items() if v}
            answers_options_letters = [key.split("_")[1] for key in answers_options_data.keys()]
            correct_answers_data = {k: v for (k, v) in question_data["correct_answers"].items() if v == "true"}
            correct_answers_letters = [key.split("_")[1] for key in correct_answers_data.keys()]
            has_multiple_answers = len(correct_answers_data) > 1
            # create a new Question object and append it to the question bank
            new_question = Question(question, answers_options_data, answers_options_letters,
                                    correct_answers_data, correct_answers_letters, has_multiple_answers)
            self.questions_bank.append(new_question)
        return self.questions_bank
