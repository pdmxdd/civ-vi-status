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


@app.route('/status', methods=['POST'])
def post_status():
    print('hello')
    if request.json is not None:
        print(request.json)
        return make_json_response(json.dumps(request.json), 201)
    #print(request.json) if request.json is not None else print("nope")
    #print(request)
    #print(request.data)
    #post_json = json.dumps(request.data.decode('utf-8'))
    #print(post_json)
    #return make_json_response(post_json)
    return make_json_response(json.dumps({"error": "json not included with request"}), 400)

if __name__ == '__main__':
    app.run(port=8080)