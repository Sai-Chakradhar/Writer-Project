
# Writer

## Description
This project is a web application that utilizes Streamlit for the front-end interface and Google Cloud services for storage and machine learning tasks.

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
```

You can install them using the following command:

```sh
pip install -r requirements.txt
```

## Setup
1. Clone the repository:

    ```sh
    git clone https://github.com/your-repo/project-name.git
    cd project-name
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
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
