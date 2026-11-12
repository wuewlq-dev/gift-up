from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.get("/api/status")
def status():
    # Демонстрационные данные. Реальные FlexStar-платежи и вывод не подключены.
    return jsonify({
        "demo": True,
        "balance": 3000,
        "currency": "FlexStar",
        "minimum_withdrawal": 200
    })

if __name__ == "__main__":
    print("GIFT UP v4 запущен: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
