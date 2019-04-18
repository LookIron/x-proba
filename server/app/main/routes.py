# -*- coding: utf-8 -*-
from flask import render_template, url_for
from app.main import bp
import os

@bp.route('/ping', methods=['GET'])
def ping():
    return 'pong'

def calculate_frequencies():
    suma = 0
    with open(os.path.abspath('./app/main/frequencies.txt'), 'r+') as f:
        for line in f:
            suma += int(line)
    return str(suma)

@bp.route('/frequencies', methods=['GET'])
def frequencies():
    result = calculate_frequencies()
    return render_template('frequencies.html', result=result)

@bp.route('/')
def index():
    return render_template('index.html', title='Home')

