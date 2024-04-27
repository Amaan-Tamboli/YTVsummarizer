# NLP-based Intelligent Content Summarization System

This system uses Natural Language Processing (NLP) to summarize the content of YouTube videos. It leverages the power of OpenAI and Hugging Face models to generate concise summaries in English, Hindi, and Marathi.

## Steps to Set Up and Deploy the System

1. **Download the Repository**: Click on the 'Code' button on the repository page and download the ZIP file. Extract the contents of the ZIP file to your local system.

2. **Create Your Own Repository**: You can either create a new repository and upload the extracted files there or fork the existing repository to your GitHub account.

3. **Install Dependencies**: Navigate to the project directory in your local system and run `pip install -r requirements.txt` to install the necessary dependencies.

4. **Edit the app.py File**: Open the `app.py` file in a text editor. Replace `'YOUR-OPENAI-KEY'` with your OpenAI key, and replace `'HINDI-MODEL-URL'` and `'ENG-MODEL-URL'` with the URLs of your Hugging Face models. Also, replace `'AUTH-TOKEN'` with your ChatGPT API's authorization token.

5. **Create a Streamlit Account**: Visit Streamlit and create a new account or log in to your existing account.

6. **Link Your GitHub Repository to Streamlit**: In your Streamlit dashboard, create a new app and link it to your GitHub repository where you uploaded or forked the project files.

7. **Deploy on Streamlit**: Fill in all the relevant information about the app and click 'Deploy'. Streamlit will automatically fetch the files from your GitHub repository and deploy the app. The web app will be online in a few minutes.

## Relevant Links

1. **website** : https://ytvsummarizer.streamlit.app/

2. **fine tuned model** : https://huggingface.co/amaantamboli54/whisper-small-hi

3. **dataset** : https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0
