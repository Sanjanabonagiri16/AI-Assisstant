
!pip install -q -U google-generativeai

pip install gTTS

def speak(answer):
  tts = gTTS('answer')
  tts.save('audio.mp3')
  display(Audio('audio.mp3', autoplay=True))

speak("hello.good afternoon everyone")

def ask_question(name):
  ques = 'Hey '+ name + 'what do you want' ?
  ques=input(ques)
  return ques

ask_question("sanju")

def classify_questions(ques):
  goahead_with_web_search =False
  device_lst = [ 'alarm','reminder','message','call']
  personal_lst =['who are you ?','who created you']

  device=False
  for i in device_lst:
    if i in ques:
      device=True

  if device:
    print("This question is related to Device things,which is not support in our google assistant")

  personal_question=False
  for  i in personal_lst:
    if i in ques.lower():
      personal_question=True

  if personal_question:
    print("Hey am a personal assistant created by your name")

  if device:
    goahead_with_web_search =False
  elif personal_question:
    goahead_with_web_search =False
  else:
    goahead_with_web_search =True

  return goahead_with_web_search

classify_questions("who are you ?")

# start searching with google gemini

from google.colab import userdata

GOOGLEAPIKEY= userdata.get('GOOGLEAPIKEY')

import pathlib
import textwrap
from gtts import gTTS

import google.generativeai as genai

#use to securely store your API key
from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown
from IPython.display import Audio, display

def to_markdown(text):
  text =text.replace('.','*')
  return Markdown(textwrap.indent(text,'>',predicate=lambda _: True))

genai.configure(api_key=GOOGLEAPIKEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

response.text

to_markdown(response.text)

def ask_gemini(ques):
  modifed_prompt ='Hey give me answer to this question'+ ques + 'in maximum of 40 words'
  response=model.generate_content(ques)
  to_markdown(response.text)
  return response.text

have_any_other_ques ='y'
name = ''

while have_any_other_ques == 'y':

  if name == '':
    name == input("Hey what is your name?-")

  q = ask_question(name)

  go_ahead = classify_questions(q)
  answer =''

  if go_ahead == True:
    answer = ask_gemini(q)
    speak(answer)
    print(answer)

  have_any_other_ques= input("Do you have any other questions??")

