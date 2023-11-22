from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain
import colorama
import time

# load and set our open source llm path
PATH = 'C:/Users/User/AppData/Local/nomic.ai/GPT4All/ggml-gpt4all-l13b-snoozy.bin'

def gpt4all_query(message_history, model, max_retries=15, sleep_time=2, DEBUG=True):
    retries = 0
    if DEBUG:
        print(colorama.Fore.MAGENTA + colorama.Style.DIM + "Message History: " + str(message_history) + colorama.Style.RESET_ALL)
    while retries < max_retries:
        try:
            llm = GPT4All(model=PATH, verbose=True)

            prompt = PromptTemplate(input_variables=['question'], template="""
                Question: {question}
                
                Answer: Let's think step by step.
                """)

            llm_chain = LLMChain(prompt=prompt, llm=llm)
            reply_content = llm_chain.run(prompt, context=)

            # completion = openai.ChatCompletion.create(
            #     model=model,
            #     messages=message_history
            # )
            # reply_content = completion.choices[0].message.content
            if reply_content:
                return reply_content
        except Exception as e:
            print(colorama.Fore.YELLOW + colorama.Style.DIM + "Error during gpt_query() " + str(e) + colorama.Style.RESET_ALL)
            retries += 1
            time.sleep(sleep_time)
    raise Exception("Maximum retries exceeded. Check your code for errors.")
