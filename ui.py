import streamlit as st
import requests

# Заголовок для інтерфейсу
st.title("Генератор текстів")

# Введення даних користувача
topic = st.text_input("Введіть тему")
style = st.selectbox("Оберіть стиль", ["науковий", "пояснювальний", "діловий", "неформальний"])
language = st.selectbox("Оберіть мову", ["українська", "англійська"])

# Кнопка для генерації тексту
if st.button("Згенерувати"):
    if topic:
        # Відправка запиту до FastAPI
        try:
            response = requests.post(
                "https://generatedstyletext-diplom2025.onrender.com/generate",  # Обов'язково перевірте URL
                json={"topic": topic, "style": style, "language": language}
            )

            # Перевірка відповіді від сервера
            if response.status_code == 200:
                generated_text = response.json().get("result")
                st.write(generated_text)
            else:
                st.error("Помилка генерації тексту, спробуйте ще раз.")
        except requests.exceptions.RequestException as e:
            # Обробка помилок під час запиту
            st.error(f"Сталася помилка: {e}")
    else:
        st.warning("Будь ласка, введіть тему для генерації.")
