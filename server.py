from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


@app.route("/info", methods={"GET"})
def information():
    x = "This website will calculate blood cholesterol levels.\n"
    x += "It is written by Denver Bradley."
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    """
        incoming_json = {"name": <name_str>,
                         "hdl_value": <hdl_value_int>}
    """
    from blood_calc import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print("The recieved value was {}".format(hdl_value))
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add_numbers", methods=["POST"])
def addition_func():
    """
        data = {"a": 1, "b": 2}
    """
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    return jsonify(answer)


@app.route("/add/<a>/<b>", methods=["GET"])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == "__main__":
    app.run()
