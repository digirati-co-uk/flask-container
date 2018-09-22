from flask import Flask, request, jsonify
import settings

app = Flask(__name__)


def main():
    app.run(threaded=True, debug=settings.DEBUG, port=5000, host='0.0.0.0')


@app.route('/ping', methods=['GET'])
def ping():

    return "pong"


@app.route('/', methods=['GET'])
def default():
    response = {
        "message": settings.EXAMPLE_VARIABLE
    }

    return jsonify(response)


if __name__ == "__main__":
    main()
