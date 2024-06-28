ARG VIRTUAL_ENV="$HOME/packages/.venv"
ARG PYTHON_VERSION=3.12.3


# Base image is python 3.12.3
FROM python@sha256:3966b81808d864099f802080d897cef36c01550472ab3955fdd716d1c665acd6 as base
ENV \
    RYE_INSTALL_OPTION="--yes" \
    RYE_TOOLCHAIN="/usr/local/bin/python3"
SHELL ["/bin/bash", "-c", "-l"]
RUN curl -sSf https://rye.astral.sh/get |  bash && source ~/.bashrc
RUN echo 'source "$HOME/.rye/env"' >> ~/.bashrc
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

from base as build
ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 
SHELL ["/bin/bash", "-c", "-l"]
WORKDIR /code
COPY ./README.md ./README.md
COPY ./src ./src
COPY ./pyproject.toml ./pyproject.toml
RUN rye sync
RUN rye build --wheel --clean

from base as serve
workdir /code
copy --from=build /code/dist/*.whl .
run uv pip install --system ./*.whl
ARG GIT_HASH
ARG APP_VERSION=0.1.0
ENV GIT_HASH=$GIT_HASH
ENV APP_VERSION=$APP_VERSION
ENV APP_NAME=bookish-octo-invention
