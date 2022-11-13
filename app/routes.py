from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/anime')
def anime():
    return render_template('anime.html')


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/drink')
def drink():
    return render_template('drink.html')


@app.route('/food')
def food():
    return render_template('food.html')