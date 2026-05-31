from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from models import Task

@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

