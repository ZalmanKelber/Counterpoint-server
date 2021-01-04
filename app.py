import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, current_dir)

from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin

from generate_from_json import GenerateFromJson

app = Flask(__name__)

CORS(app)

@app.route("/api/wake_up", methods=["GET"])
def wake_up():
    return "waking up"

@app.route("/api", methods=["POST"])
def api_route():
    json_request = request.get_json()
    print(json_request)
    counterpoint_id = GenerateFromJson().generate_from_json(json_request)
    try:
        print("counterpoint id:", counterpoint_id)
        return send_file("generated_files_store/" + counterpoint_id + ".mid", as_attachment=True)
    except FileNotFoundError:
        return "file note found"

if __name__ == "__main__":
    app.run(debug=False)