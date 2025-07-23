from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Kebi from Flask in Docker on EKS! lets celebarate the successful completion for project🥳😊"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
