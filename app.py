import streamlit as st
from pytube import YouTube
import openai
import tempfile
import os
import requests

st.title("NLP-based Intelligent Content Summarization System")

openai.api_key = 'YOUR-OPENAI-KEY'
API_URL_hi = "HINDI-MODEL-URL"
API_URL_en = "ENG-MODEL-URL"
headers = {"Authorization": "Bearer AUTH-TOKEN"}
CHATGPT_MODEL = 'gpt-3.5-turbo'
YOUTUBE_VIDEO_URL = st.text_input('Input the url : ')
vid_language = st.selectbox('Audio Language', ('English', 'Hindi'))
output_language = st.selectbox('Summary Language', ('English', 'Hindi', 'Marathi'))

def download_youtube_audio(url):
    try:
        output_dir = 'OUTPUT_AUDIO'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        youtube_video = YouTube(url)
        streams = youtube_video.streams.filter(only_audio=True)
        stream = streams.first()
        output_file = os.path.join(output_dir, stream.default_filename)
        stream.download(output_path=output_dir)
        
        return output_file
    except Exception as e:
        st.write(f"Error in downloading YouTube audio: {e}")

def summarize_text(transcript):
    try:
        messages = [{"role": "user", "content": f"""Generate a concise summary of the text below.
          Text: {transcript}

          Add a title to the summary.

          Make sure your summary has useful and true information about the main points of the topic.
          Begin with a short introduction explaining the topic. If you can, use bullet points to list important details,
          and finish your summary with a concluding sentence. The output must be in {output_language}"""}]

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        )

        return response.choices[0].message["content"]
    except Exception as e:
        st.write(f"Error in summarizing text: {e}")

def query(filename, API_URL):
    try:
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    except Exception as e:
        st.write(f"Error in querying API: {e}")

def boot():
    try:
        OUTPUT_AUDIO = download_youtube_audio(YOUTUBE_VIDEO_URL)
        if OUTPUT_AUDIO is None:
            return

        if vid_language == 'English':
            transcript = query(OUTPUT_AUDIO, API_URL_en)
        else:
            transcript = query(OUTPUT_AUDIO, API_URL_hi)
        if transcript is None:
            return

        summary = summarize_text(transcript)
        if summary is None:
            return

        st.title(f'Summary for the Youtube Video:\n{summary}')
    except Exception as e:
        st.write(f"Error in boot function: {e}")
        return


if st.button('Submit'):
    boot()
