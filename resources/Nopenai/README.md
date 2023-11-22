Building LLM Apps...without OpenAI
Want to build LLM Apps...but without OpenAI dependencies? Well have I got the code for you my friend. In this project I walk through how to build a langchain x streamlit app using GPT4All. We start off with a simple app and then build up to a langchain PythonREPL agent.

See it live and in action 📺

Startup 🚀
Create a virtual environment python -m venv nonopenai
Activate it:
Windows:.\nonopenai\Scripts\activate
Mac: source nonopenai/bin/activate
Install the GPT4All Installer using GUI based installers
Windows: https://gpt4all.io/installers/gpt4all-installer-win64.exe
Mac: https://gpt4all.io/installers/gpt4all-installer-darwin.dmg
Ubuntu: https://gpt4all.io/installers/gpt4all-installer-linux.run
Download the required LLM models and take note of the PATH they're installed to
Clone this repo git clone https://github.com/nicknochnack/Nopenai
Go into the directory cd NonOpenAI
Install the required dependencies pip install -r requirements.txt
Update the path of the models in line 9 of app.py and line 5 of app-chain.py
Start the python agent app by running streamlit run app.py or the chain app by running streamlit run app-chain.py
Go back to my YouTube channel and like and subscribe 😉...no seriously...please! lol
The comparison app can be started by running streamlit run app-comparison.py before you do that though, update the base ggml download path in line 16, e.g. BASE_PATH = 'C:/Users/User/AppData/Local/nomic.ai/GPT4All/' and openAI api key on line 18
Other References 🔗
-GPT4AllReference : mainly used to determine how to install the GPT4All library and references. Doco was changing frequently, at the time of coding this was the most up to date example of getting it running.

Who, When, Why?
👨🏾‍💻 Author: Nick Renotte
📅 Version: 1.x
📜 License: This project is licensed under the MIT License