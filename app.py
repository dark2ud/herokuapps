from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

locations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def add_location():
    data = request.get_json()
    locations.append(data)
    return jsonify({"message": "Location added"}), 200

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations), 200

if __name__ == '__main__':
    app.run(debug=True)
