import openai
import json
import logging


class OpenAIConnector:
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key
        logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def get_answer_from_llm(self, document_text: str, question: str) -> str:
        """
        Sends the document text and question to the OpenAI API and returns the answer.

        Args:
            document_text (str): Text extracted from the PDF.
            question (str): The question to be answered.

        Returns:
            str: The answer provided by the language model, or "Data Not Available" if confidence is low.
        """
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system",
                     "content": "You are an assistant that provides precise answers based on the given document text."},
                    {"role": "user", "content": f"Document text:\n{document_text}\n\nQuestion: {question}\nAnswer:"}
                ],
                max_tokens=100,
                temperature=0.2
            )
            answer = response.choices[0].message.content.strip()
            if "I'm not sure" in answer or answer == "":
                return "Data Not Available"
            return answer
        except Exception as e:
            logging.error(f"Error in get_answer_from_llm: {e}")
            return "Data Not Available"

    def answer_questions(self, document_text: str, questions: list) -> dict:
        """
        Answers a list of questions based on the document text.

        Args:
            document_text (str): Text extracted from the PDF.
            questions (list): List of questions to answer.

        Returns:
            dict: dict of question and answer pairs.
        """

        answers = {}
        for question in questions:
            try:
                answer = self.get_answer_from_llm(document_text, question)
                answers[question] = answer
            except Exception as e:
                logging.error(f"Error processing question '{question}': {e}")
                answers[question] = "Data Not Available"
        logging.info("Questions processed successfully")
        return answers

    @staticmethod
    def format_answers_as_json(answers: dict) -> str:
        """
        Formats the answers dict as a JSON string.

        Args:
            answers (dict): dict of question and answer pairs.

        Returns:
            str: JSON-formatted string of answers.
        """
        return json.dumps(answers, indent=4)
