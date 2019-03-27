from flask import Flask, make_response, request
import json

app = Flask(__name__)


def make_json_response(the_json, status_code):
    """
    Make json_response -- so we can pass back JSON from this backend to the front end
    """
    response = make_response(the_json, status_code)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')
    return response


@app.route('/', methods=['GET'])
def index():
    return 'INDEX'


@app.route('/status', methods=['GET'])
def get_status():
    try:
        with open('status.json', 'r') as rf:
            read_json = json.load(rf)
            return make_json_response(json.dumps(read_json), 200)
    except FileNotFoundError:
        return make_json_response(json.dumps({"error": "No JSON on server"}), 400)


@app.route('/status', methods=['POST'])
def post_status():
    if request.json is not None:
        with open('status.json', 'w') as wf:
            json.dump(request.json, wf)
        return make_json_response(json.dumps(request.json), 201)
    return make_json_response(json.dumps({"error": "json not included with request"}), 400)


if __name__ == '__main__':
    app.run(port=8080)