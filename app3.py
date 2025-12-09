from flask import Flask, render_template, request

app = Flask(__name__)
example = ""
@app.get('/')
def klkulatorGet():
    return render_template('kalkulator.html', namber="")

@app.post('/')
def klkulatorPost():
    global example
    action = request.form.get('action')
    print("hsdagjs",action)
    if action in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "/", "+", "-"):
        example += action
    elif action == "=":
        example = eval(example)
        print(example)
        print(action)
    return render_template('kalkulator.html', namber=example)

if __name__ == '__main__':
    app.run(debug=True, port=5002)