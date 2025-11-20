from flask import Flask
import random as r

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

if __name__ == '__main__':

    app.run(debug=True)