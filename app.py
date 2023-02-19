import gradio as gr
from revChatGPT.V1 import Chatbot

#You can setup login information here, or login in from UI

# If you want to use Email/Password to login, put your account information here
email = ""
password = ""

# If you have an access token, put your access token here
access_token = ""

# If you have a session token, put your session token here
session_token = ""


def is_google_colab():
    try:
        import google.colab
        return True
    except:
        return False
    
chatbot = None
    
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

    chatbot = Chatbot(config=config)

login_method = ['Email/Password',
                'Access token',
                'Session token',
                ]

def ask_bot(prompt):
    message = ""
    if chatbot:
        for data in chatbot.ask(prompt):
            message = data["message"]
    else:
        message = "The chatbot is not set up properly! Try to login again."
    return parse_text(message)

def parse_text(text):
    lines = text.split("\n")
    for i,line in enumerate(lines):
        if "```" in line:
            items = line.split('`')
            if items[-1]:
                lines[i] = f'<pre><code class="{items[-1]}">'
            else:
                lines[i] = f'</code></pre>'
        else:
            if i>0:
                lines[i] = '<br/>'+line.replace(" ", "&nbsp;")
    return "".join(lines)

def chatgpt_clone(inputs, history):
    history = history or []
    output = ask_bot(inputs)
    history.append((inputs, output))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("""<h1><center>ChatGPT BOT build by revChatGPT & Gradio</center></h1>
    """)

    if not ((email and password) or access_token or session_token):
        gr.Markdown("""<h2>Login to OpenAI</h2>""")
        with gr.Row():
            with gr.Group():
                method = gr.Dropdown(label="Login Method", choices=login_method)
                info = gr.Textbox(placeholder="email password/access_token/session_token", label="Login Information (choose login method first)")
                with gr.Row():
                    login = gr.Button("Login")
                    login.click(configure_chatbot, inputs=[method, info])
    else:
        if email and password:
            method = "Email/Password"
            info = email + " " + password
        elif access_token:
            method = "Access token"
            info = access_token
        elif session_token:
            method = "Session token"
            info = session_token
        configure_chatbot(method, info)

    gr.Markdown("""<h2>Start Chatting ...</h2>""")
    chatbot1 = gr.Chatbot()
    message = gr.Textbox(placeholder="Chat here")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot1, state])

    demo.launch(debug = True, share=is_google_colab())
