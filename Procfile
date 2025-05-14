# Для запуску FastAPI бекенду# Для запуску FastAPI бекенду
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# Для запуску Streamlit інтерфейсу
streamlit: streamlit run ui.py --server.port 10000 --server.address 0.0.0.0
