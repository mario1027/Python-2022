from apps.routes import blueprint
from flask import render_template, request,redirect

@blueprint.route("/")
def index():
    return render_template("index.html")

@blueprint.route("/page1")
def page1():
    return render_template("page1.html")