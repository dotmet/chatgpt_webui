# ChatGPT_WebUI
Build a WebUI of ChatGPT with multiple authentication methods using Gradio and revChatGPT

(Based on [revChatGPT](https://github.com/acheong08/ChatGPT) and [Gradio](https://gradio.app/))

#### If you have a Valid OpenAI account, u can use ChatGPT on [HuggingFace](https://huggingface.co/) through this project without VPN tools.
#### This project will not SAVE/DISPLAY/SHARE the ACCOUNT INFO of any user!!


## Demos
#### To bypass the Area and Network restriction, you can duplicate the huggingface space demo and login to your own account. Then you can use ChatGPT in any place.
  - HuggingFace [Demo](https://huggingface.co/spaces/dotmet/chatgpt_webui) 
  - GoogleColab [Demo](https://colab.research.google.com/drive/1NhSKhSPFNsEzCIjcNgnbDQgewtp6Leub#scrollTo=q9qPXpL_ydSW)

## Login methods
  1. Email/Password
  2. Access token
  3. Session token

## How to login
  - Before webui launch
  
  Replace the corresponding variable based on your token type in ```app.py``` (see more details in ```app.py```).
  - After webui launch
  
  Login through UI Login button when WebUI is running by choosing a method based on your token type.

## How to launch webui

Clone this repository:

```bash
  git clone https://github.com/dotmet/chatgpt_webui.git
```

Install depencies:

```bash
  cd chatgpt_webui
  pip install -r requirements.txt
```
Launch webui:
```
  python app.py
```

## Chat in WebUI (example)

![ui](https://github.com/dotmet/chatgpt_webui/blob/main/UI.JPG)
