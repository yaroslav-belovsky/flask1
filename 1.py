from flask import Flask, render_template, request, send_file
import random as r
from datetime import datetime

list1 = ["Сьогодні у вас", "Завтра на вас", "Незабаром", "Колись", "Якось", "На твій день народження"]
list2 = ["чекає", "буде", "зустріне", "настане", "почнеця", "настане", ""]
list3 = ["гарна новина", "погана звістка", "гарний день", "поганий день", "ніхто не принесе подарунку", "щось станеться..."]
books = ["інцеклопедія знань","Аліса в країні чудес","Аліса в задзеркаллі"]

fruits_list = [{"name": "Яблуко", "color": "red"},
{"name": "Банан", "color": "yellow"},
{"name": "Груша", "color": "green"},
{"name": "Вишня", "color": "red"},
{"name": "Ківі", "color": "green"},
{"name": "Апельсин", "color": "orange"}]

types = [
    {
      'value': 'Сніданок',
      'name': 'сніданок'
    },
{
      'value': 'Обід',
      'name': 'обід'
    },
{
      'value': 'Вечеря',
      'name': 'вечеря'
    },
{
      'value': '4',
      'name': 'хочу все одразу'
    }
]

complexities = [
    {
      'value': 'Легка',
      'name': 'легка'
    },
{
      'value': 'Середня',
      'name': 'середня'
    },
{
      'value': 'Складна',
      'name': 'складна'
    },
{
      'value': '4',
      'name': 'хочу все одразу'
    }
]

food_list = [
    {
        "назва": "Яєчня-бовтанка (скрембл)",
        "тип": "Сніданок",
        "складність": "Легка"
    },
    {
        "назва": "Вівсяна каша з ягодами",
        "тип": "Сніданок",
        "складність": "Легка"
    },
    {
        "назва": "Сирники",
        "тип": "Сніданок/Вечеря",
        "складність": "Легка"
    },
    {
        "назва": "Гречана каша з молоком",
        "тип": "Сніданок/Вечеря",
        "складність": "Легка"
    },
    {
        "назва": "Борщ український",
        "тип": "Обід/Вечеря",
        "складність": "Середня"
    },
    {
        "назва": "Вареники з картоплею/сиром",
        "тип": "Обід/Вечеря",
        "складність": "Середня"
    },
    {
        "назва": "Деруни (картопляні оладки)",
        "тип": "Сніданок/Обід/Вечеря",
        "складність": "Легка/Середня"
    },
    {
        "назва": "Салат 'Олів'є'",
        "тип": "Обід/Вечеря",
        "складність": "Легка/Середня"
    },
    {
        "назва": "Піца 'Маргарита'",
        "тип": "Обід/Вечеря",
        "складність": "Середня/Складна"
    },
    {
        "назва": "Стейк Рібай просмажування медіум",
        "тип": "Вечеря",
        "складність": "Середня/Складна"
    },
    {
        "назва": "Голубці з м'ясом і рисом",
        "тип": "Обід/Вечеря",
        "складність": "Складна"
    },
    {
        "назва": "Лазанья Болоньєзе",
        "тип": "Обід/Вечеря",
        "складність": "Складна"
    },
    {
        "назва": "Суші та роли (домашні)",
        "тип": "Обід/Вечеря",
        "складність": "Складна"
    },
    {
        "назва": "Бельгійські вафлі",
        "тип": "Сніданок/Десерт",
        "складність": "Середня"
    },
    {
        "назва": "Чизкейк класичний",
        "тип": "Десерт (Вечеря)",
        "складність": "Складна"
    }
]


app = Flask(__name__)

@app.get("/horoskop/")
def horoskop():
    return  f"{r.choice(list1)} {r.choice(list2)} <b>{r.choice(list3)}</b>"

@app.get('/')
def hello_world():

    return 'Привіт, світе!'

@app.post("/")
def get_fruits():
    action = request.form.get("action")
    name = request.form.get("name")
    color = request.form.get("color")
    if action == "add_fruit":
        fruits_list.append({"name": name, "color": color})
    if action == "delete_fruit":
        for fruit in fruits_list:
            if fruit["name"] == name:
                fruits_list.remove(fruit)

    return render_template("fruits.html", fruits=fruits_list)

@app.get('/home/')
def home():
    user = request.args.get('user')
    if user is None:
        user = "Anonim"
    age = request.args.get('age')
    if age is None:
        age = 0
    return render_template("index.html", name=user,  data=datetime.now(), age=int(age))

@app.get('/info/')
def info():
    return render_template("info.html")

@app.get("/submit/")
def get_submit():
    return render_template("submit.html")

@app.post("/submit/")
def post_submit():
    name = request.form.get("name")
    age = request.form.get("age")
    color = request.form.get("color")
    return render_template("answer.html", name=name, age=age, color=color)

@app.get("/spiderMan/")
def spiderMan():
    return render_template("spider-man.html")

@app.get("/spiderMan/image")
def spiderManImage():
    return send_file('templates/marvels-spider-man-780x439.jpg', mimetype='image/png')

@app.get("/get_books/")
def get_books():
    return render_template("books.html", books=books)

@app.get("/food_menu/")
def food():
    return render_template("food.html", types=types, complexities=complexities)

@app.post("/food_menu/")
def food_menu():
    type_name = request.form.get("type")
    complexity = request.form.get("Complexity")
    selected = []
    for food in food_list:
        if (complexity in food["складність"] or complexity == '4') and (type_name in food["тип"] or type_name == '4'):
            selected.append(food)

    return render_template(
        "food.html",
        types=types,
        complexities=complexities,
        type_name=type_name,
        complexity=complexity,
        selected=selected,
    )

if __name__ == '__main__':

    app.run(debug=True, port=5002)