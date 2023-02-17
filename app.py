import os
import gradio as gr
from revChatGPT.V1 import Chatbot

#You can setup login information here, or login in from UI
email = None
password = None
access_token = None
session_token = None

# Detect if this script is running on the google colab
def is_google_colab():
    try:
        import google.colab
        return True
    except:
        return False

def configure_chatbot(method, info):
    
    if method=="Email/Password":
        email, password = info.split()
    elif method=="Access token":
        access_token = info
    elif method=="Session token":
        session_token = info

    config = {}
    if email and password:
        config.update({"email": email,
                      "password": password})
    elif access_token:
        config.update({"access_token": access_token})
    elif session_token:
        config.update({"session_token": session_token})

    global chatbot
    chatbot = Chatbot(config=config)

login_method = ['Email/Password',
                'Access token',
                'Session token',
                ]

def ask_bot(prompt):
    message = ""
    for data in chatbot.ask(prompt):
        message = data["message"]
    return message

def chatgpt_clone(inputs, history):
    history = history or []
    # s = list(sum(history, ()))
    # s.append(inputs)
    # inp = ' '.join(s)
    # print(inp)
    output = ask_bot(inputs)
    history.append((inputs, output))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("""<h1><center>ChatGPT BOT build by revChatGPT & Gradio</center></h1>
    """)

    if not ((email and password) or access_token or session_token):
        gr.Markdown("""<h2>Login to OpenAI<h2>""")
        with gr.Row():
            with gr.Group():
                method = gr.Dropdown(label="Login Method", choices=login_method)
                info = gr.Textbox(placeholder="email password/access_token/session_token", label="Login Information")
                with gr.Row():
                    login = gr.Button("Login")
                    login.click(configure_chatbot, inputs=[method, info])

    gr.Markdown("""<h2>Start Chatting ...<h2>""")
    chatbot1 = gr.Chatbot()
    message = gr.Textbox(placeholder="Chat here")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot1, state])

    demo.launch(debug = True, share=is_google_colab())
