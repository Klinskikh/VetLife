# -*- coding: utf-8 -*-
from .. import app, db
from ..forms import DosageForm
from ..models import Dosage, ActiveSubstance, Medicine
from flask import render_template, flash, redirect, request, url_for


def _process_request(id=None, active_substance_id=None, medicine_id=None):
    active_substance = ActiveSubstance.query.get(active_substance_id)
    if id:
        dosage = Dosage.query.get(id)
        form = DosageForm(obj=dosage)
    else:
        form = DosageForm()

    medicine = Medicine.query.get(medicine_id)
    if request.method == 'POST':
        dosage = Dosage(active_substance=active_substance)
        form = DosageForm(request.form, obj=dosage)
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(dosage)
                db.session.add(dosage)
                db.session.commit()
                flash(u"Сохранено")
        else:
            flash(u"Неверные данные")

    ctx = dict(title=u'Дозировка', form=form, active_substance=active_substance)
    ctx['medicine'] = medicine
    return render_template('dosage/edit.html', **ctx)


@app.route('/dosage_edit/<id>/<active_substance_id>/<medicine_id>', methods=['GET', 'POST'])
def dosage_edit(id, active_substance_id, medicine_id):
    return _process_request(id, active_substance_id, medicine_id)


@app.route('/dosage_add/<active_substance_id>/<medicine_id>', methods=['GET', 'POST'])
def dosage_add(active_substance_id, medicine_id):
    return _process_request(active_substance_id=active_substance_id, medicine_id=medicine_id)




