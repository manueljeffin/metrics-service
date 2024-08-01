from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_data():
  data = request.json
  print(data)
  return jsonify({"status": "success", "received": data}), 200


if __name__ == '__main__':
  app.run(debug=True, port=5000)
