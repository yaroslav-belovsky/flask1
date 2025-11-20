from flask import Flask, render_template, request
import random as r
from datetime import datetime

list1 = ["Сьогодні у вас", "Завтра на вас", "Незабаром", "Колись", "Якось", "На твій день народження"]
list2 = ["чекає", "буде", "зустріне", "настане", "почнеця", "настане", ""]
list3 = ["гарна новина", "погана звістка", "гарний день", "поганий день", "ніхто не принесе подарунку", "щось станеться..."]

app = Flask(__name__)

@app.get("/horoskop/")
def horoskop():
    return  f"{r.choice(list1)} {r.choice(list2)} <b>{r.choice(list3)}</b>"

@app.get('/')
def hello_world():

    return 'Привіт, світе!'

@app.get('/home/')
def home():
    user = request.args.get('user')
    return render_template("index.html", name=user,  data=datetime.now())

@app.get('/info/')
def info():
    return render_template("info.html")
if __name__ == '__main__':

    app.run(debug=True, port=5002)