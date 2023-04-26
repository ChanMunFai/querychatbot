import os
import gradio as gr
import pickle
from typing import Optional, Tuple
from threading import Lock
from query_data import load_chain

with open("vectorstore.pkl", "rb") as f:
    vectorstore = pickle.load(f)

def set_openai_api_key(api_key: str):
    """Set the api key and return chain.
    If no api_key, then None is returned.
    """
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        chain = load_chain(vectorstore)
        os.environ["OPENAI_API_KEY"] = ""
        return chain

OPENAI_LINK = "[OpenAI](https://openai.com)"
OPENAI_API_LINK = "[OpenAI API Key](https://platform.openai.com/account/api-keys)"
LANGCHAIN_LINK = "[LangChain](https://python.langchain.com/en/latest/index.html) 🦜️🔗"

init_message = f""" This is a chatbot that is trained to query over publicly available resources  on the [National Climate Change Secretariat](https://nccs.gov.sg) website. 
This demonstration app is based on **{OPENAI_LINK}** with **{LANGCHAIN_LINK}**. 
    1. Insert your **{OPENAI_API_LINK}** and hit `ENTER`
    2. Insert your **Question** and click `Send`
"""

disclaimer_message = f""" #### Disclaimer
This app is completely unaffilated to [NCCS Singapore](https://nccs.gov.sg) or the Government of Singapore  
This is purely an educational tool to demonstrate a chatbot that can query over publicly available material.  
"""

class ChatWrapper:

    def __init__(self):
        self.lock = Lock()
    def __call__(
        self, api_key: str, inp: str, history: Optional[Tuple[str, str]], chain
    ):
        """Execute the chat functionality."""
        self.lock.acquire()
        try:
            history = history or []
            # If chain is None, that is because no API key was provided.
            if chain is None:
                history.append((inp, "Please paste your OpenAI key to use"))
                return history, history
            # Set OpenAI key
            import openai
            openai.api_key = api_key
            # Run chain and append input.
            output = chain({"question": inp, "chat_history": history})["answer"]
            history.append((inp, output))

            print(history)
        except Exception as e:
            raise e
        finally:
            self.lock.release()
        return history, history

chat = ChatWrapper()

block = gr.Blocks(
    theme = "Base", 
    css=""".bigbox {min-height:250px;}"""
    )

with block:
    gr.Markdown("# Unofficial NCCS Chatbot")
    gr.Markdown(init_message)
    gr.Markdown(disclaimer_message)

    with gr.Row(): 
        openai_api_key_textbox = gr.Textbox(
            placeholder="Paste your OpenAI API key (sk-...)",
            show_label=False,
            lines=1,
            type="password",
        )
    with gr.Column(scale=10):
        chatbot = gr.Chatbot(elem_classes="bigbox")

    with gr.Row():
        message = gr.Textbox(
            label="What's your question?",
            placeholder="What is climate change?",
            lines=1,
        )
        submit = gr.Button(value="Send", variant="secondary").style(full_width=False)

    gr.Examples(
        examples=[
            "What is climate change?",
            "When was the National Climate Change Secretariat formed?",
            "How is hydrogen used to combat climate change?",
        ],
        inputs=message,
    )

    gr.HTML("<center>Unofficial NCCS Chatbot. This app is unaffilated to the <a href='https://www.nccs.gov.sg/'>National Climate Change Secretariat Singapore</a>.<center>")
    gr.HTML("<center>All intellectual property rights belong to the Government of Singapore. Please refer to their <a href='https://www.nccs.gov.sg/terms-of-use/'>terms of use</a> for more information.</center>")

    state = gr.State()
    agent_state = gr.State()

    submit.click(chat, inputs=[openai_api_key_textbox, message, state, agent_state], outputs=[chatbot, state])
    message.submit(chat, inputs=[openai_api_key_textbox, message, state, agent_state], outputs=[chatbot, state])

    openai_api_key_textbox.change(
        set_openai_api_key,
        inputs=[openai_api_key_textbox],
        outputs=[agent_state],
    )

block.launch(debug=True)