# -*- coding: utf-8 -*-
from .. import app, db
from ..forms import DosageForm
from ..models import Dosage, Medicine
from flask import render_template, flash, redirect, request, url_for


def _process_request(id=None, medicine_id=None):
    medicine = Medicine.query.get(medicine_id)
    if id:
        dosage = Dosage.query.get(id)
    else:
        dosage = Dosage(medicine=medicine)
    form = DosageForm(obj=dosage)
    if request.method == 'POST':
        form = DosageForm(request.form, obj=dosage)
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(dosage)
                db.session.add(dosage)
                db.session.commit()
                flash(u"Сохранено")
                redirect(url_for('medicine_edit', id=dosage.medicine_id))
        else:
            flash(u"Неверные данные")
    ctx = dict(title=u'Дозировка', form=form, medicine=medicine)
    return render_template('dosage/edit.html', **ctx)


@app.route('/dosage_edit<id><medicine_id>', methods=['GET', 'POST'])
def dosage_edit(id, medicine_id):
    return _process_request(id, medicine_id)


@app.route('/dosage_add<medicine_id>', methods=['GET', 'POST'])
def dosage_add(medicine_id):
    return _process_request(medicine_id=medicine_id)




