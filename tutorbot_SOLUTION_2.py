import streamlit as st
import json

# Import LTS Proxy from another file
from proxy import lts_proxy

# Create Proxy
proxy = lts_proxy.Proxy()

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
    # Add a role to ChatGPT
    proxy.system_role = "You're a teacher for 15 year olds. Result in JSON format."
    # Add the initial question
    proxy.question = "Generate multiple questions and answers about:"
    # Add the data
    proxy.user_data = topic
    # Send the request and get questions and answers
    questions_answers = proxy.get_questions_and_answers()

    # Preview questions and answers
    tab_1.write(questions_answers)
    
    # Download questions and answers json file
    tab_1.download_button(label='Download', 
                          data=json.dumps(questions_answers), 
                          file_name='download.json', 
                          mime='text/json')

# --- Tab 2
# Add title
tab_2.title('Chatbot tutor')

# Add JSON file uploder 
file = tab_2.file_uploader('Upload a json file', type=["json"])

# Continue only if there is a file
if file:
    # Convert json file to a python dictionary
    file_json = json.loads(file.read())
    tab_2.write('Data Loaded: ' + file_json["content"])
    tab_2.header('Question to answer')

    # Create 2 columns
    col_1, col_2 = tab_2.columns(2)
    # Add streamlit elements to the first column
    with col_1:
        # Streamlit refreshes after every interaction, meaning all 
        # state is deleted. We therefore save each given question in cache.
        # Here we check if the key 'question' is in the dictionary
        # If not, we assign a value (random question) to our key (question)
        if 'question' not in st.session_state:
            st.session_state.question = proxy.get_random_question(file_json)
        
    # Add streamlit elements to the second column
    with col_2:
        # Button which allows to choose the next question randomly
        if col_2.button('Next Question'):
            st.session_state.question = proxy.get_random_question(file_json)
            # Write the chosen question in our tab
            col_1.write(st.session_state.question)

    # Save the answer
    answer = tab_2.text_area("Please enter your answer: ", value=None)
    # Add button to send answer
    if tab_2.button(label="Submit"):
        # Set the role as tutor
        proxy.system_role = "You act as a tutor for 15 year olds."
	    # Add the whole file as user data (content, questions & answers)
        proxy.user_data = file_json
	    # The current answer and question are stored in the assistant instance
        proxy.answer = answer
        proxy.question = st.session_state.question

        # Get an evaluation from ChatGPT
        evaluation = proxy.get_evaluation()
        tab_2.subheader('Question')
        tab_2.write(st.session_state.question)
        tab_2.subheader('Answer')
        tab_2.write(answer)
        tab_2.subheader('Evaluation')
        tab_2.write(evaluation)

        # If the answer scores >7 out of 10, let's celebrate a little ;)
        if (("10 out of 10" in evaluation)
        or ("9 out of 10" in evaluation)
        or ("8 out of 10" in evaluation)):
            st.balloons()
