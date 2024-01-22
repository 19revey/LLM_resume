FROM python:3.11-slim

<<<<<<< HEAD
EXPOSE 8501
=======
>>>>>>> 200ac25a6d0dc4da1df6bfce19cccf1d03d4f8f3

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
<<<<<<< HEAD
=======
    poppler-utils \
>>>>>>> 200ac25a6d0dc4da1df6bfce19cccf1d03d4f8f3
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

<<<<<<< HEAD
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
=======
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
>>>>>>> 200ac25a6d0dc4da1df6bfce19cccf1d03d4f8f3
