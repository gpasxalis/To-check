from flask import Blueprint, render_template, request, url_for
from elasticsearch import Elasticsearch




es = Elasticsearch()

hello2 = Blueprint('hello2',__name__)


@hello2.route('/search', methods = ["POST", "GET"])
def test():


	tag_input = request.form.get('tag_input')
	value_input = request.form.get('value_input')




	res = es.search(index="lib-index", size=1000, body={"query": {"nested":{"path":"datagroup", "query":{"match": {"datagroup.taggroup": tag_input}}}}})  # 1st Search


	return render_template("layout.html", tag_input=tag_input, value_input=value_input, res=res)
