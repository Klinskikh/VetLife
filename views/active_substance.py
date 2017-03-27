# -*- coding: utf-8 -*-
from .. import app, db
from ..forms import ActiveSubstanceForm
from ..models import Dosage, ActiveSubstance
from flask import render_template, flash, redirect, request, url_for


def _process_request(medicine_id, id=None):
    if id:
        active_substance = ActiveSubstance.query.get(id)
        dosages = Dosage.query.filter_by(active_substance=active_substance)
    else:
        dosages = []
        active_substance = ActiveSubstance()
    form = ActiveSubstanceForm(obj=active_substance)
    if request.method == 'POST':
        form = ActiveSubstanceForm(request.form, obj=active_substance)
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(active_substance)
                db.session.add(active_substance)
                db.session.commit()
                flash(u"Сохранено")
                redirect(url_for('active_substance_edit', id=active_substance.id, medicine_id=medicine_id))
        else:
            flash(u"Неверные данные")
    ctx = dict(title=u'Активное вещество', form=form, dosages=dosages)
    return render_template('active_substance/edit.html', **ctx)


@app.route('/active_substance_edit/<id>/<medicine_id>', methods=['GET', 'POST'])
def active_substance_edit(id, medicine_id):
    return _process_request(id=id, medicine_id=medicine_id)


@app.route('/active_substance_add<medicine_id>', methods=['GET', 'POST'])
def active_substance_add(medicine_id):
    return _process_request(medicine_id)




