
---

# AI PDF Q&A Bot

This project implements an AI-driven bot that extracts information from a PDF document and answers user-provided questions. The bot uses OpenAI's language model for question-answering and integrates with Slack to post answers directly to a designated Slack channel.

## Project Structure

```
zania_ai/
├── data/
│   └── handbook.pdf            # Sample PDF file for testing
├── demo/                       # Demo video directory
│   └── zania_ai_task_demo.mp4  # Demo video (.mp4)
├── env/                        # Virtual environment directory
├── src/                        # Source code directory
│   ├── __init__.py             # Init file for source package
│   ├── connect_to_openai.py    # Interacts with OpenAI API for Q&A
│   ├── connect_to_slack.py     # Interacts with Slack API for posting messages
│   ├── pdf_text_extraction.py  # Handles PDF text extraction
│   └── settings.py             # Configuration settings for API keys, models, logging, etc.
├── tests/
│   └── __init__.py             # Init file for tests package
├── .env                        # Environment file to store API keys
├── app.log                     # Log file for application events
├── main.py                     # Main script to run the bot via command-line
├── README.md                   # Project documentation (this file)
└── requirements.txt            # List of required Python packages
```

## Features

- **PDF Text Extraction**: Extracts content from a PDF document for processing.
- **Question-Answering**: Uses OpenAI's language model to answer user-provided questions based on PDF content.
- **Slack Integration**: Posts structured JSON responses with answers directly to a specified Slack channel.
- **Error Handling**: Provides fallback responses like "Data Not Available" for low-confidence answers or unrecognized questions.
- **Configurable Settings**: Uses `settings.py` for easy configuration of API keys, logging, and other settings.

## Configuration

The `settings.py` file handles the configuration of API keys, models, logging, and other settings. It loads environment variables from a `.env` file located in the root directory and defines the following settings:

- **API Keys**:
  - `OPENAI_API_KEY`: OpenAI API key, loaded from the `.env` file.
  - `SLACK_BOT_TOKEN`: Slack bot token, loaded from the `.env` file.

- **Slack Channel**:
  - `SLACK_CHANNEL`: Specifies the default Slack channel where the bot posts answers. You can update the channel name in `settings.py`.

- **OpenAI Model**:
  - `OPENAI_MODEL`: Specifies the OpenAI model to use for question-answering. The current default is `"gpt-4o-mini"`.

- **Logging**:
  - `LOGGING_LEVEL`: Configures the logging level (options: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
  - `LOG_FILE`: Specifies the log file name (`app.log` by default).

### Example `.env` File

Create a `.env` file in the project root with the following entries:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
SLACK_BOT_TOKEN=your_slack_bot_token_here
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key
- A Slack Bot Token with necessary permissions (`chat:write`, `files:read`, etc.)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the project root directory as shown in the previous section.

5. **Add the Bot to Your Slack Channel**:
   - Invite the bot to the channel where it will post answers by typing `/invite @YourBotName` in Slack.

### Usage

1. **Run the Script**:
   Execute the main script with command-line arguments for the PDF file path and questions:

   ```bash
   python main.py -p "data/handbook.pdf" -q "What is the name of the company?; Who is the CEO of the company?"
   ```

2. **Arguments**:
   - `-p, --pdf_path`: Path to the PDF file (e.g., `data/handbook.pdf`).
   - `-q, --questions`: Questions separated by semicolons (`;`).

3. **Output**:
   - The bot will generate answers, display them in JSON format on the console, and post the output in the specified Slack channel.

### Sample Output

```json
{
  "What is the name of the company?": "Zania, Inc.",
  "Who is the CEO of the company?": "Shruti Gupta"
}
```
## Demo Video

To see the AI PDF Q&A Bot in action, watch the demo video:


[Download the demo video](demo/zania_ai_task_demo.mp4)

## Additional Notes

- **Low Confidence Answers**: If the model cannot find a clear answer, it will respond with "Data Not Available."
- **Environment File**: Ensure that `.env` is in `.gitignore` to prevent accidental exposure of API keys.

## Ways to Improve Solution Accuracy

1. **Keyword-Based Filtering**: Pre-filter document sections based on keywords in the question, improving answer relevance.
2. **Two-Pass Verification**: Use a second pass to verify or refine initial answers, reducing ambiguity.
3. **Confidence Scoring**: Implement confidence checks based on keyword matching or response content to return reliable answers.
4. **Summarization of Sections**: Summarize document sections to keep answers concise and relevant.
5. **Custom QA Model**: Fine-tune an open-source QA model for domain-specific document types to improve answer precision.

## Future Improvements for Modularity, Scalability, and Production Quality

1. **Modular Code Structure**: Separate components like PDF parsing, Q&A, and Slack posting into individual modules for easier maintenance.
2. **Asynchronous API Calls**: Use asynchronous programming to handle multiple requests concurrently, enhancing scalability.
3. **Containerization with Docker**: Use Docker for a consistent setup across environments, simplifying deployment.
---