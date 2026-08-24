
try:
    from flask import Flask
except ImportError:
    print('Flask is not installed. Please install it using pip.')
    exit(1)

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
