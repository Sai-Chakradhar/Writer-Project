
# Writer

## Description
The Writer project consists of a fine-tuned large language model (LLM) designed to mimic the unique writing style of Professor Hammond. The user interface (UI) is developed using Streamlit and deployed on Streamlit Cloud, providing a simple yet effective platform for interacting with the model. 
## Features
- Interactive web interface using Streamlit
- Integration with Google Cloud Storage
- Machine learning capabilities via Vertex AI

## Requirements
To run this project, you need the following dependencies installed:

```plaintext
streamlit==1.10.0
google-cloud-storage
vertexai==1.43.0
google-auth
altair==4.0
```

You can install them using the following command:

```sh
pip3 install -r requirements.txt
```

## Setup
1. Clone the repository:

    ```sh
    git clone https://github.com/your-repo/writer-project.git
    cd writer-project
    ```

2. Install the dependencies:

    ```sh
    pip3 install -r requirements.txt
    ```

3. Set up Google Cloud credentials:
    - Download your service account key file from the Google Cloud Console.
    - Save the key file as `deep-beanbag-423322-p9-cc234e73d2b5.json` in the root directory of your project.
    - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to this file:

    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="path/to/deep-beanbag-423322-p9-cc234e73d2b5.json"
    ```

## Usage
To start the application, run the following command:

```sh
streamlit run main.py
```

## Project Structure
- `main.py`: The main script that runs the Streamlit application.
- `home.py`: Script containing the home page code.
- `page2.py`: Script containing additional page code.
- `requirements.txt`: A file containing all the dependencies required for the project.
- `deep-beanbag-423322-p9-cc234e73d2b5.json`: Google Cloud service account credentials.

## Contributing
Feel free to open issues or submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
