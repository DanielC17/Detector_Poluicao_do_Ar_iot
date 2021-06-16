from application import app
'''from application.model.dao.medidaDao import '''
from flask import render_template, request, url_for, redirect
'''from application.model.entity.medida import '''


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
