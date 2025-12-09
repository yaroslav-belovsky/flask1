from flask import Flask, session, render_template_string, request, make_response

app = Flask(__name__)
app.secret_key = "секретний_ключ"

@app.route("/")
def home():
    name = request.cookies.get("username")
    user_agent = request.headers.get("User-Agent")
    if "clicks" not in session:

        session["clicks"] = 0

    return render_template_string("""
        {{name}}
        <h1>Кількість кліків: {{ clicks }}</h1>
        <a href="/click">Натисни!</a>
    
        """, clicks=session["clicks"], name=name, user_agent=user_agent)

@app.get("/cookies/")
def cookies():
    res = make_response("Settings cookies")
    res.set_cookie("username", "Yaroslav", max_age=1000)
    return res

@app.route("/click")
def click():
    session["clicks"] += 1

    return home()

@app.get("/exemple/<int:id>")
def exemple(id):
    return f"число {id}"

@app.get("/exemple/<string:text>")
def exemple(text):
    return f"число {text}"

if __name__ == "__main__":

    app.run(debug=True)
