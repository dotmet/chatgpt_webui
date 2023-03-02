# ChatGPT_WebUI
Build a WebUI of ChatGPT with multiple authentication methods using Gradio and revChatGPT

(Based on [revChatGPT](https://github.com/acheong08/ChatGPT) and [Gradio](https://gradio.app/))
#### This project will not SAVE/DISPLAY/SHARE the ACCOUNT INFO of any user!!
#### If you have a Valid OpenAI account, u can use ChatGPT on [HuggingFace](https://huggingface.co/spaces/dotmet/chatgpt_webui) through this project without VPN tools.

## Demos
#### To bypass the Area and Network restriction, you can duplicate the huggingface space demo and login using your own account. Then you can use ChatGPT anywhere.
（如果无法登录OpenAI，使用HuggingFace部署chatgpt_webui，然后使用账号密码登录即可正常使用ChatGPT，无需使用任何VPN）

  - HuggingFace [Demo](https://huggingface.co/spaces/dotmet/chatgpt_webui) 
  - GoogleColab [Demo](https://colab.research.google.com/drive/1NhSKhSPFNsEzCIjcNgnbDQgewtp6Leub?usp=sharing)

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

## Launch options
 - ```--no_markdown``` Disable all mark down to make the UI clean. Example usage: 
 ```bash
 python app.py --no_markdown
 ```
 
 If you put the token in ```app.py``` and then launch it with the option ```--no_markdown```, you will get a very clean UI:
 ![clean_mode](https://github.com/dotmet/chatgpt_webui/blob/main/clean.JPG)
 
 - Other options coming soon.

## Chat in webpage (example)

  - Full of markdown

![ui](https://github.com/dotmet/chatgpt_webui/blob/main/example.JPG)

  - Write cpp code
 
![cpp_code](https://github.com/dotmet/chatgpt_webui/blob/main/code.JPG)
