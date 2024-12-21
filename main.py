from flask import Flask

app = Flask(__name__)

# Routing dla localhost:5000/michal
@app.route('/michal')
def michal():
    return "Witaj XYZ"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
