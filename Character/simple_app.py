from flask import Flask
#from flask import request

#use the current name space
#in this case __name__
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def  index(name="Iceland"):
	#get argument from the browser url
	#name = request.args.get("name", name)
	return "Hello from here {}".format(name)


@app.route("/add/<int:num1>/<int:num2>")
@app.route("/add/<float:num1>/<float:num2>")
def add(num1, num2):
	#return str(num1 + num2)
	return "{} + {} = {}".format(num1, num2,  num1 + num2)


app.run(debug=True, port=8000, host="0.0.0.0")