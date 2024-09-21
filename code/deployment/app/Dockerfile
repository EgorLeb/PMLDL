FROM python:3.9.20-slim-bullseye
WORKDIR /app
COPY . .

RUN pip install streamlit

CMD ["streamlit", "run", "main.py"]
