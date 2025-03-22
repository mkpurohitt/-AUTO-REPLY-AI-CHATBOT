import pyautogui
import time
import pyperclip
from openai import OpenAI
#this is main file for this project

#my openai api key for this project
API_KEY = "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"
client = OpenAI(api_key=API_KEY)

# it will click on my whatsapp web icon from browser
pyautogui.click(954, 1054)
time.sleep(1)  # Wait for the application 

# it will select text of my whatsapp chat with my friend
pyautogui.moveTo(684, 204)
pyautogui.mouseDown()
pyautogui.moveTo(1430, 885, duration=0.5)
pyautogui.mouseUp()

# will copy the selected text
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1415,856)
time.sleep(0.5) 

text = pyperclip.paste()

print("Copied Text:", text)

system_message = {
    "role": "system",
    "content": "You are a person named mehul who speaks in hindi as well as english he is from india and he is a trader and a trader of futures and options.you analyse chat history and respond  like mehul ouput should be the next chat response as mehul"
}

user_message = {
    "role": "user",
    "content": text
}

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[system_message, user_message]
)

response = completion.choices[0].message
pyperclip.copy(response)


# it will paste the response and send the message
pyautogui.click(919, 955)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')

#after all this it succesfully respond like 
# Nahi yaar, library mein hai, bas kuch study kar raha tha. Tu kya kar raha hai?


