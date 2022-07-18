from kudz import app
from flask import render_template, redirect, url_for, flash, request


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/projects')
def projects():
    return render_template('projects.html')
