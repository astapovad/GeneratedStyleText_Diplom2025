# Генерація текстів із використанням GPT-3.5 Turbo

Цей проєкт реалізує веб-сервіс для генерації текстів на основі заданої теми, стилю та мови. Для реалізації використано FastAPI для серверної частини та Streamlit для інтерфейсу користувача. Текст генерується через модель GPT-3.5 Turbo за допомогою API OpenAI.

## Основні технології

- Python 3.10+
- FastAPI
- Streamlit
- OpenAI API (GPT-3.5 Turbo)
- Uvicorn
- Render (для хмарного розгортання)

## Запуск проєкту локально

### 1. Клонувати репозиторій
```bash
git clone https://github.com/your-username/text-generation-service.git
cd text-generation-service

### 2. Створити .env файл
OPENAI_API_KEY=sk-...тут_твій_ключ...

### 3. Встановити залежності 
pip install -r requirements.txt

### 4. Запустити бекенд (FastAPI)
uvicorn main:app --reload

### 5. Запустити Streamlit UI
streamlit run ui.py


## Автор: Астапова Дар'я Вячеславівна, студентка ДУІКТ, м. КИЇВ, кафедра "Комп'ютерні науки" освітня програма "Штучний інтелект", група ШІД-42, 2025 р.