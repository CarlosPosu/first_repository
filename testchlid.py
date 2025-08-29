from app import app
from flask import render_template
from models import Usuario, Pago

@app.route('/')
def index():
    return "¡Bienvenido a la aplicación Flask!"

@app.route('/usuarios')
def mostrar_usuarios():
    usuarios = Usuario.query.all()  # Obtener todos los usuarios
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/pagos')
def mostrar_pagos():
    pagos = Pago.query.all()  # Obtener todos los pagos
    return render_template('pagos.html', pagos=pagos)
