# Access point for translating braille to text and vice verse.
import printer
import alphaToBraille
import brailleToAlpha
from sys import argv
from flask import Flask, jsonify, request


def user_braille(data):
    res = brailleToAlpha.translate(data)
    print(res)
    return res


def user_text(data):
    res = alphaToBraille.translate(data)
    print(res)
    return res


def open_braille(filename):
    file = open(filename)
    content = file.read()
    print(brailleToAlpha.translate(content))


def open_text(filename):
    file = open(filename)
    content = file.read()
    print(alphaToBraille.translate(content))


app = Flask(__name__)


@app.route("/brailleFromText", methods=["POST"])
def getBrailleFromText():
    try:
        data = request.get_json()
        if 'text' in data:
            text = data['text']
            result = user_text(text)  # Call your translation function here
            print(result)
            return jsonify({"result": result})
        else:
            return jsonify({"error": "Missing 'text' field in the JSON data"}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')
