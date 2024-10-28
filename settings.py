import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI and Slack API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Slack Channel
SLACK_CHANNEL = "#ai-agent-project"  # Update as necessary

# OpenAI Model
OPENAI_MODEL = "gpt-4o-mini"

# Logging Configuration
LOGGING_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "app.log"
