from flask import Flask

app = Flask(__name__)


def add_numbers(a, b):
    return int(a) + int(b)


@app.route("/")
def home():
    result = add_numbers(9, "99")
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)