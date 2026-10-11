from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is Working!"

if __name__ == "__main__":
    print("Starting...")
    app.run(debug=True)