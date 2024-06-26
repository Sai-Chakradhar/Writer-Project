import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel
import os
from google.cloud import storage


service_account_key_file = 'deep-beanbag-423322-p9-cc234e73d2b5.json'

# Set the environment variable to point to your service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_file

# Initialize a Google Cloud Storage client
client = storage.Client()


def multiturn_generate_content1(text):
    vertexai.init(project="363949151355", location="us-central1")
    model = GenerativeModel(
    "projects/363949151355/locations/us-central1/endpoints/5997868914866913280",
    )
    chat = model.start_chat()
    generation_config = {
        "max_output_tokens": 2048,
        "temperature": 1,
        "top_p": 1,
    }
    x = chat.send_message(
        [text + " Write in the style of the person who you were finetuned on and don't talk about you. Write 300-500 words"],
        generation_config=generation_config,
    )
    return x

def app():
    # Title of the webpage
    st.title("Writer Project")
    st.subheader("Input a piece of text and see it rewrite in Kris Hammond's writing style.")

    # Create two columns
    col1, col2 = st.columns(2)

    # Accept user input in the first column
    with col1:
        user_input = st.text_area("Enter your text here:", key="page2_input")

    # Display the user input in the second column
    with col2:
        st.write("Generated text")
        if user_input:
            y = multiturn_generate_content1(user_input)
            y = y.to_dict()
            content = y['candidates'][0]['content']['parts'][0]['text']
            st.write(content.encode().decode('unicode_escape'))