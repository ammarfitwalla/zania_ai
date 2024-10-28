import os
import logging
import argparse
from src.connect_to_openai import OpenAIConnector
from src.connect_to_slack import SlackConnector
from src.pdf_text_extraction import PDFTextExtractor
from settings import SLACK_CHANNEL, OPENAI_API_KEY, OPENAI_MODEL, SLACK_BOT_TOKEN


def parse_arguments():
    """
    Parses command-line arguments for PDF path and questions.

    Returns:
        argparse.Namespace: Parsed arguments with pdf_path and questions.
    """
    parser = argparse.ArgumentParser(description="Process a PDF and answer questions, then post to Slack.")
    parser.add_argument("-p", "--pdf_path", type=str, required=True, help="Path to the PDF file.")
    parser.add_argument(
        "-q", "--questions",
        type=str,
        required=True,
        help="Questions to answer based on the PDF content, separated by semicolons (;)."
    )
    return parser.parse_args()


def main() -> None:
    """
    Main function to handle inputs, process the PDF, answer questions, format answers as JSON,
    and post the results to Slack.

    Returns:
        None
    """
    try:
        logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        openai_connector = OpenAIConnector(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
        slack_connector = SlackConnector(bot_token=SLACK_BOT_TOKEN, channel_name=SLACK_CHANNEL)
        pdf_processor = PDFTextExtractor()

        args = parse_arguments()

        pdf_path = os.path.normpath(args.pdf_path)
        if not os.path.isfile(pdf_path):
            print(f"Error: The file at '{pdf_path}' does not exist. Please enter a valid file path.")
            return

        questions = [q.strip() for q in args.questions.split(";") if q.strip()]
        if not questions:
            print("Error: Questions cannot be blank. Please provide at least one question.")
            return

        document_text = pdf_processor.extract_text_from_pdf(pdf_path=pdf_path)
        if not document_text:
            logging.warning("No text extracted from PDF. Check file content.")
            print("No text could be extracted from the PDF. Please check the file and try again.")
            return

        answers = openai_connector.answer_questions(document_text=document_text, questions=questions)
        answers_json = openai_connector.format_answers_as_json(answers=answers)
        # Log JSON output
        print(answers_json)
        logging.info("Formatted JSON Output:\n%s", answers_json)

        # Attempt to post to Slack
        slack_connector.post_results_to_slack(answers_json=answers_json, channel=SLACK_CHANNEL)
        logging.info("Process completed!")

    except Exception as e:
        logging.error(f"An error occurred in the main workflow. {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()
