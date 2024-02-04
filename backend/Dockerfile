FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBEFFERED 1

RUN pip install --upgrade pip

FROM continuumio/miniconda3

RUN conda update -n base -c defaults conda

RUN conda install -c conda-forge opencv

RUN apt-get update && apt-get install -y libgl1-mesa-glx

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]