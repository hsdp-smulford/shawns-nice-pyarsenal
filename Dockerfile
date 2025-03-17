FROM python:3.13-alpine

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    curl \
    bash \
    git \
    make

RUN pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.create false

COPY pyproject.toml ./

RUN poetry install --no-root

COPY . .

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

RUN echo 'echo "Welcome to Shawns Nice PyArsenal 🐍"' >> /root/.bashrc \
    && echo 'echo "Python $(python --version)" | sed "s/Python //"' >> /root/.bashrc

CMD ["/bin/bash"]
