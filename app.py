from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_information', methods=['POST'])
def get_information():
    data = request.form
    moisture = data.get('moisture')
    pH = data.get('pH')
    temperature = data.get('temperature')
    ec = data.get('ec')
    npk = data.get('npk')

    # Process data and provide recommendations
    recommendation = process_data(moisture, pH, temperature, ec, npk)
    return jsonify({'recommendation': recommendation})

def process_data(moisture, pH, temperature, ec, npk):
    # Implement logic based on soil types and crop needs
    return "Recommended Fertilizer and Crop"

if __name__ == "__main__":
    app.run(debug=True)
