
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.environ.get("NAME", "World")
    return f"Hello, {name}!"

if __name__ == "__main__":
    # The default port is 5000, which matches the Dockerfile
    app.run(host='0.0.0.0', port=5000)
