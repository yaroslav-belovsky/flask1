from flask import Flask, render_template, request
from urllib3.util.util import to_str

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('tst_index.html', result=None)

@app.post('/')
def convert():
    action = request.form.get
    v = ""
    if action == "button":
        try:
            value = float(request.form.get('value'))
            form_unit = request.form.get('from_unit')
            to_unit = request.form.get('to_unit')
            result = convert_units(value, form_unit, to_unit)
        except ValueError:
            result = "помилка: введи число"
        v = render_template("tst_index.html", result=result)
    elif action == "add_fruit":
        conversion_factors = {

            'cm': {'m': 0.01, 'km': 0.00001, 'inch': 0.393701, 'foot': 0.0328084},
            'm': {'cm': 100, 'km': 0.001, 'inch': 39.3701, 'foot': 3.28084},
            'km': {'cm': 100000, 'm': 1000, 'inch': 39370.1, 'foot': 3280.84},
            'inch': {'cm': 2.54, 'm': 0.0254, 'km': 0.0000254, 'foot': 0.0833333},
            'foot': {'cm': 30.48, 'm': 0.3048, 'km': 0.0003048, 'inch': 12},

            'kg': {'g': 1000, 'lb': 2.20462, 'oz': 35.274},
            'g': {'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
            'lb': {'kg': 0.453592, 'g': 453.592, 'oz': 16},
            'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625}}
        v = f"{conversion_factors}"
    return v



def convert_units(value, from_unit, to_unit):

    conversion_factors = {

    'cm': {'m': 0.01, 'km': 0.00001, 'inch': 0.393701, 'foot': 0.0328084},
    'm': {'cm': 100, 'km': 0.001, 'inch': 39.3701, 'foot': 3.28084},
    'km': {'cm': 100000, 'm': 1000, 'inch': 39370.1, 'foot': 3280.84},
    'inch': {'cm': 2.54, 'm': 0.0254, 'km': 0.0000254, 'foot': 0.0833333},
    'foot': {'cm': 30.48, 'm': 0.3048, 'km': 0.0003048, 'inch': 12},

    'kg': {'g': 1000, 'lb': 2.20462, 'oz': 35.274},
    'g': {'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
    'lb': {'kg': 0.453592, 'g': 453.592, 'oz': 16},
    'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625}
    }
    if from_unit == to_unit:

        return value #Якщо одиниці однакові, повертаємо значення без змін

    return value * conversion_factors.get(from_unit, {}).get(to_unit, 1)

if __name__ == '__main__':
    app.run(debug=True, port=5002)