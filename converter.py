from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    value = float(data['value'])
    unit = data['unit']

    if unit == "m_to_km":
        result = value / 1000
    elif unit == "km_to_m":
        result = value * 1000
    else:
        result = "invalid unit"

    return jsonify({'result': result})

if __name__  == '__main__':
    app.run(debug=True)

