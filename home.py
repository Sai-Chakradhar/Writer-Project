import streamlit as st
import os
import json
from google.cloud import storage
from google.api_core.exceptions import GoogleAPIError
import socket
# Function to check if the environment is online by checking network connectivity
from google.cloud import storage
from google.api_core.exceptions import GoogleAPIError

# Function to check if the environment is online based on the presence of specific environment variables
def is_online():
    # Check for environment variables commonly set in cloud environments
    import os
    is_local = os.getenv("LOCAL_ENV", "false").lower() == "true"
    print(is_local)
    if is_local:
        return True
    else:
        False
# Create a JSON file with service account credentials from st.secrets

def create_service_account_json():
    service_account_info = {
        "type": "service_account",
        "project_id": st.secrets["app"]["project_id"],
        "private_key_id": st.secrets["secrets"]["private_key_id"],
        "private_key": st.secrets["secrets"]["private_key"],
        "client_email": st.secrets["app"]["client_email"],
        "client_id": st.secrets["app"]["client_id"],
        "auth_uri": st.secrets["app"]["auth_uri"],
        "token_uri": st.secrets["app"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["app"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["app"]["client_x509_cert_url"],
        "universe_domain": st.secrets["app"]["universe_domain"]
    }
    
    with open('service_account.json', 'w') as json_file:
        json.dump(service_account_info, json_file)
    st.write(service_account_info)
    return 'service_account.json'

# Check if the environment is online or offline
if is_online():
    print(True)
    service_account_key_file = create_service_account_json()
else:
    # Set the path to your service account key file if running locally
    service_account_key_file = 'deep-beanbag-423322-p9-cc234e73d2b5.json'


# Set the environment variable to point to your service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_file

# Initialize a Google Cloud Storage client
client = storage.Client()


#buckets = list(client.list_buckets())

generation_config = {
    "max_output_tokens": 2048,
    "temperature": 1,
    "top_p": 1,
}
def multiturn_generate_content(text):
    import vertexai
    from vertexai.generative_models import GenerativeModel
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
    
    st.subheader("Input a prompt and see it generate text in Kris Hammond's writing style")

    col1, col2 = st.columns(2)

    # Accept user input in the first column
    with col1:
        user_input = st.text_area("Enter your text here:", key="home_input")

    # Display the user input in the second column
    with col2:
        st.write("Generated text")
        if user_input:
            y = multiturn_generate_content(user_input)
            y = y.to_dict()
            content = y['candidates'][0]['content']['parts'][0]['text']
            st.write(content.encode().decode('unicode_escape'))

if __name__ == "__main__":
    app()