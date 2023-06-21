from flask import Flask,request,jsonify
from flask_cors import CORS

from main import main

app = Flask(__name__)
CORS(app)


@app.route("/api", methods=["GET"])
def main():
    url = request.args.get("url")
    dic,status_code=main(url)
    return jsonify(dic),status_code
    
if __name__ == "__main__":
    app.run()