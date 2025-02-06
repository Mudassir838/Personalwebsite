from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Personal Website!</h1><p>Skills: Python, Docker, Flask</p><p>Goals: Learn and grow!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


