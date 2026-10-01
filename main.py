import config
import random
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, send_file, render_template, redirect, abort, session, url_for, make_response, jsonify
from datetime import timedelta, datetime


# Инцилизация Flask Приложение #
app = Flask(__name__)
app.config.update(SECRET_KEY=config.SECRET_KEY)
app.permanent_session_lifetime = timedelta(days=365)















@app.route('/')
@app.route('/landing')
@app.route('/lending')
def landing():
    return render_template('lending.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4432)