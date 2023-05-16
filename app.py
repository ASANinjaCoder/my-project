import openai
import streamlit as st

openai.api_key = "your_api_key"


def BasicGeneration(userprompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messsages=[
        {"role": "user", "content": userprompt}]
    )
    return completion.choices[0].message.content

st.title("Professional Prompt Generator")
st.subheader("Turn short prompts into highly detailed and straight to the point")

prompt = "Your_prompt_here"


response = BasicGeneration(prompt)


