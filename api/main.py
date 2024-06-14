from flask import Flask

app = Flask(__name__)

@app.route("/")
def met():
    return {"msg":"flask application"}

app.run(host="0.0.0.0", port=4000)