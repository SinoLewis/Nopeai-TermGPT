import openai
import colorama
import logging
from dotenv import load_dotenv
import time

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

def openai_query(message_history, model="gpt-4", max_retries=15, sleep_time=2):
    retries = 0
    logger = logging.getLogger()

    logger.info("Message History: %s", message_history)
        
    while retries < max_retries:
        try:
            completion = openai.ChatCompletion.create(
                model=model,
                messages=message_history
            )
            reply_content = completion.choices[0].message.content
            if reply_content:
                return reply_content
        except Exception as e:
            logger.warning("Error during gpt_query(): %s", e)
            retries += 1
            time.sleep(sleep_time)

    raise Exception("Maximum retries exceeded. Check your code for errors.")
