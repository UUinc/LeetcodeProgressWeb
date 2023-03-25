from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "home page"

if __name__ == '__main__':
    app.run(debug=True, port=8000)