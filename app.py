from flask import Flask,request,jsonify
from flask_cors import CORS

from main import main

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def main():
    status_code=200
    return jsonify({"res":"hello!!"}),status_code

@app.route("/api", methods=["GET"])
def main():
    url = request.args.get("url")
    dic,status_code=main(url,save_pickle=True,save_firestore=False)
    return jsonify(dic),status_code
    
if __name__ == "__main__":
    app.run()