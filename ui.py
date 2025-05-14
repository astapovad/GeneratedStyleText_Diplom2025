import streamlit as st
import requests

st.title("Генератор текстів")

topic = st.text_input("Введіть тему")
style = st.selectbox("Оберіть стиль", ["науковий", "пояснювальний", "діловий", "неформальний"])
language = "українська"

if st.button("Згенерувати"):
    if topic:
        response = requests.post(
            "https://<твоє-ім’я-сервісу>.onrender.com/generate",
            json={"topic": topic, "style": style, "language": language}
        )
        if response.status_code == 200:
            st.write(response.json()["result"])
        else:
            st.error("Помилка генерації")
    else:
        st.warning("Введіть тему")