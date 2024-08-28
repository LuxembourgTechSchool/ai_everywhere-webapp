import streamlit as st
import json

# Create list of names of tabs
tabs = ['Questions & Answers', 'Learning Assistance']

# Create tabs
tab_1, tab_2 = st.tabs(tabs)

# --- Tab 1
# Add title and header 
tab_1.title(tabs[0])
tab_1.header('Generate Practice Test Questions')

# Create a variable 'topic' and assign text_area text to it
topic = tab_1.text_area('Please input the topic you want a list of questions & answers for: ')

if tab_1.button('Generate') and len(topic) > 0:
    # Preview questions and answers
    tab_1.write('Success')

    # Create dummy questions and answers to test button
    questions_answers = [1, 2, 3]

    # Download questions and answers as json file
    tab_1.download_button(label='Download', 
                          data=json.dumps(questions_answers), 
                          file_name='download.json', 
                          mime='text/json')