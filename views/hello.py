from flask import Blueprint, render_template, request, url_for

from ..app import es


hello = Blueprint('hello',__name__)
test = Blueprint('test',__name__)


@hello.route('/')
def index_page():

	if request.method == "POST":
		text1 = request.form["tag_input"]
		text2 = request.form["value_input"]
		return redirect(url_for("hello2.test", tag_input=text1, value_input=text2))
	else:
		return render_template("index_page.html")
