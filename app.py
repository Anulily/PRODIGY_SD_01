from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    temp = float(data['temperature'])
    unit = data['unit']

    if unit == "C":
        celsius = temp
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
    elif unit == "F":
        celsius = (temp - 32) * 5/9
        fahrenheit = temp
        kelvin = celsius + 273.15
    else:  # Kelvin
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        kelvin = temp

    return jsonify({
        "celsius": round(celsius, 2),
        "fahrenheit": round(fahrenheit, 2),
        "kelvin": round(kelvin, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
