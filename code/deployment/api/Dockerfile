FROM python:3.9.20-slim-bullseye
WORKDIR /app
COPY . .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install fastapi[all]
RUN pip install opencv-python

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
