from fastapi import FastAPI, Body
import psycopg2
app = FastAPI()

conn = psycopg2.connect(database='psycology_centre', user='postgres', password='pass1', host='26.177.241.120', port="5432")
cursor = conn.cursor()

@app.get("/")
async def root(body = Body()):
    return body["message"]
@app.get("/psychologists/{id}")
async def psychologists(id):
    str = 'select show_psycholog_data(' + id + ')'
    cursor.execute(str)
    records = cursor.fetchone()
    return records

@app.get("/psychologists/time/{name}/{time}")
async def show_consultations(name, time):
    str = 'select show_time_consultations(\'' + name + '\',\'' + time + '\')'
    cursor.execute(str)
    records = cursor.fetchone()
    return records

@app.get("/psychologists/account/{username}/{password}")
async def check_user(username, password):
    str = 'select check_user(\'' + username + '\',\'' + password + '\')'
    cursor.execute(str)
    records = cursor.fetchone()
    return records

@app.delete("/psychologists/del_appointment/{psycholog}/{patient}/{date}")
async def del_appointment(psycholog, patient, date):
    str = 'select delete_consultation(\'' + psycholog + '\' ,\''+ patient + '\' ,\''+ date + '\')'
    cursor.execute(str)
    records = cursor.fetchone()
    return records

@app.post("/psychologists/appointment/{psycholog}/{patient}/{date}")
async def appointment(psycholog, patient, date):
    str = 'select add_consultation(\'' + psycholog + '\', \'' + patient + '\', \'' + date + '\')'
    cursor.execute(str)
    records = cursor.fetchone()
    return records

@app.get("/psychologists/psycholog_name/{name}")
async def psycholog_name(name):
    str = 'select find_psycholog_by_name(\'' + name + '\')'
    cursor.execute(str)
    a = 2
    records = cursor.fetchone()
    return records

@app.get("/psychologists/psycholog_find/{min}/{max}/{theme}")
async def psycholog_find(min, max, theme):
    str = 'select find_psycholog_data(' + min + ',' + max + ',\'' + theme + '\')'
    cursor.execute(str)
    records = cursor.fetchone()
    return records
