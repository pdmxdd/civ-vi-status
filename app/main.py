from flask import Flask, make_response, request, render_template
import json
import datetime

app = Flask(__name__)


def central_time(datetime_string):
    datetime_string_split = datetime_string.split("/")
    central_year = int(datetime_string_split[0])
    central_month = int(datetime_string_split[1])
    central_day = int(datetime_string_split[2])
    central_hour = int(datetime_string_split[3][0:2]) - 5
    if central_hour < 0:
        central_hour += 24
        central_day = int(datetime_string_split[2]) - 1
        if central_day == 0:
            if datetime_string_split[1] in ["01", "03", "05", "07", "08", "10", "12"]:
                central_day = 31
            elif datetime_string_split[1] in ["04", "06", "09", "11"]:
                central_day = 30
            else:
                # TODO: if leapyear(): central_day = 29 if leapyear(): else central_day = 28
                central_day = 28
            central_month = int(datetime_string_split[1]) - 1
            if central_month == 0:
                central_month = 12
                central_year = int(datetime_string_split[0]) - 1

    if central_day < 10:
        central_day = "0{}".format(central_day)
    if central_month < 10:
        central_month = "0{}".format(central_month)
    if central_hour < 10:
        central_hour = "0{}".format(central_hour)

    str_civ_time = "{}/{}/{}/{}{}".format(central_year,
                                          central_month,
                                          central_day,
                                          central_hour,
                                          datetime_string_split[3][2:])

    return str_civ_time

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
    return render_template("index.html")


@app.route('/status', methods=['GET'])
def get_status():
    try:
        with open('status.json', 'r') as rf:
            read_json = json.load(rf)
            read_json["current_time"] = central_time(datetime.datetime.utcnow().strftime("%Y/%m/%d/%H:%M:%S"))
            return make_json_response(json.dumps(read_json), 200)
    except FileNotFoundError:
        return make_json_response(json.dumps({"error": "No JSON on server"}), 400)


@app.route('/status', methods=['POST'])
def post_status():
    if request.json is not None:
        game_json = {}
        game_json["turn_time"] = central_time(datetime.datetime.utcnow().strftime("%Y/%m/%d/%H:%M:%S"))
        if "value1" in request.json.keys():
            game_json["name"] = request.json["value1"]
        if "value2" in request.json.keys():
            game_json["player"] = request.json["value2"]
        if "value3" in request.json.keys():
            game_json["turn"] = request.json["value3"]
        with open('status.json', 'w') as wf:
            json.dump(game_json, wf)
        return make_json_response(json.dumps(game_json), 201)
    return make_json_response(json.dumps({"error": "json not included with request"}), 400)


if __name__ == '__main__':
    app.run(port=8080)
