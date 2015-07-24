import json
from flask import (Flask, render_template, redirect, 
		     url_for, request, make_response)
from options import DEFAULTS

app = Flask(__name__)

def get_saved_data():
	try:
		data = json.loads(request.cookies.get("character"))

	except TypeError:
		data = {}

	return data


@app.route("/")
def index():
	data = get_saved_data()
	context = {"saves": data}
	return render_template("index.html", **context)


@app.route("/save", methods=["POST"])
def save():
	#import pdb; pdb.set_trace()
	#cookies are set on the respons, things that go back to the
	#browser
	response = make_response(redirect(url_for("builder")))
	data = get_saved_data()
	data.update(dict(request.form.items()))
	response.set_cookie("character", json.dumps(data))
	return response


@app.route("/builder")
def builder():
	context = {"saves": get_saved_data(),
		      "options": DEFAULTS
		    }
	return render_template("builder.html", **context)

app.run(debug=True, host="0.0.0.0", port=8090)