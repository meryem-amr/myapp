FROM python:3.9
COPY . /swr_application
WORKDIR /swr_application
RUN pip install spacy
RUN python -m spacy download en_core_web_sm
CMD ["python", "script.py"]