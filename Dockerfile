FROM python
WORKDIR /code
RUN pip install fastapi[all]
RUN pip install psycopg2-binary
COPY ./main.py /code/main.py
CMD ["fastapi", "run", "main.py", "--port", "8000"]