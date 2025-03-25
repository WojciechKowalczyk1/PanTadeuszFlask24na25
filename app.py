from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name):
    return "Hello World!"
if __name__ == "__main__":
    app.run()