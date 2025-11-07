from flask import Flask, send_file

app = Flask(__name__)

@app.route("/get_code", methods=["GET"])
def get_code():
    try:
        # send_file serves the file content directly
        return send_file("code.txt", mimetype="text/plain")
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/",methods = ["GET"])
def get():
    return {}, 200


if __name__ == "__main__":
    # host='0.0.0.0' makes it accessible from other devices in same network
    app.run(host="0.0.0.0", port=5000)
