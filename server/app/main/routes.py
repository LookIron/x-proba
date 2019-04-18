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

def calculate_frequencies_2():
    suma = 0 
    cadena = ""
    with open(os.path.abspath('./app/main/frequencies.txt'), 'r+') as f:
        while True:            
            for line in f:
                suma += int(line)
                line = int(line)
                cadena += str(suma) +","
                if (str(line) in cadena):
                    return line
    return str(suma)

@bp.route('/frequencies', methods=['GET'])
def frequencies():
    result = calculate_frequencies()
    return render_template('frequencies.html', result=result)

@bp.route('/frequencies-2', methods=['GET'])
def frequencies2():
    result = calculate_frequencies_2()
    return render_template('frequencies2.html', result=result)

@bp.route('/')
def index():
    return render_template('index.html', title='Home')

