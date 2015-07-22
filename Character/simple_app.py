from flask import Flask
from flask import render_template
#from flask import request

#use the current name space
#in this case __name__
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def  index(name="Iceland"):
	#get argument from the browser url
	#name = request.args.get("name", name)
	context = {"name": name}
	return render_template("index.html", **context)


@app.route("/add/<int:num1>/<int:num2>")
@app.route("/add/<float:num1>/<float:num2>")
def add(num1, num2):
	#return str(num1 + num2)
	context = {"num1": num1, "num2": num2}
	return render_template("add.html",**context)


app.run(debug=True, port=8000, host="0.0.0.0")