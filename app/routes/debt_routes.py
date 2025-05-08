from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from datetime import date
from ..models import PersonDebt
from ..forms import DebtForm
from .. import db

debt_bp = Blueprint('debt', __name__, url_prefix='/deudas')

@debt_bp.route('/')
@login_required
def index():
    deudas = PersonDebt.query.all()
    resumen = {
        'cumplido': 0,
        'moroso': 0,
        'pendiente': 0
    }
    for d in deudas:
        resumen[d.estado] += 1

    # Predicción de posibles morosos el próximo mes
    probabilidad_alta = 0
    probabilidad_media = 0
    probabilidad_baja = 0

    for d in deudas:
        if d.estado == 'pendiente' and d.due_date:
            dias_restantes = (d.due_date - date.today()).days
            porcentaje_pagado = d.abono / d.amount if d.amount else 0

            if porcentaje_pagado < 0.5 and dias_restantes <= 10:
                probabilidad_alta += 1
            elif porcentaje_pagado < 0.75 and dias_restantes <= 15:
                probabilidad_media += 1
            else:
                probabilidad_baja += 1

    prediccion = {
        'alta': probabilidad_alta,
        'media': probabilidad_media,
        'baja': probabilidad_baja
    }

    return render_template('deudas/index.html', deudas=deudas, resumen=resumen, prediccion=prediccion)

@debt_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    form = DebtForm()
    if form.validate_on_submit():
        deuda = PersonDebt(
            name=form.name.data,
            amount=form.amount.data,
            abono=form.abono.data,
            due_date=form.due_date.data
        )
        db.session.add(deuda)
        db.session.commit()
        return redirect(url_for('debt.index'))
    return render_template('deudas/create.html', form=form)

@debt_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    deuda = PersonDebt.query.get_or_404(id)
    form = DebtForm(obj=deuda)
    if form.validate_on_submit():
        deuda.name = form.name.data
        deuda.amount = form.amount.data
        deuda.abono = form.abono.data
        deuda.due_date = form.due_date.data
        db.session.commit()
        return redirect(url_for('debt.index'))
    return render_template('deudas/edit.html', form=form, deuda=deuda)

@debt_bp.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    deuda = PersonDebt.query.get_or_404(id)
    db.session.delete(deuda)
    db.session.commit()
    return redirect(url_for('debt.index'))