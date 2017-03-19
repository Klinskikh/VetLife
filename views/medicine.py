# -*- coding: utf-8 -*-
from .. import app, db
from ..forms import MedicineForm
from ..models import Medicine
from flask import render_template, flash, redirect, request, url_for


@app.route('/medicine<id>', methods=['GET', 'POST'])
def medicine_edit(id):
    medicine = Medicine.get(id)
    form = MedicineForm(request.form, medicine)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(medicine)
                medicine.put()
                flash(u"Сохранено")
                return redirect(url_for("medicine{0}".format(id)))
    return render_template('medicine/edit.html',
                           title=u'Лекарства',
                           form=form)


@app.route('/medicine', methods=['GET', 'POST'])
def medicine_list():
    medicines = Medicine.query.all()
    forms = []
    for medicine in medicines:
        forms.append(MedicineForm(instance=medicine))
    return render_template('medicine/list.html',
                           title=u'Лекарства',
                           forms=forms)

@app.route('/medicineadd', methods=['GET', 'POST'])
def medicine_add():
    medicine = Medicine()
    form = MedicineForm(request.form, instance=medicine)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(medicine)
                db.session.add(medicine)
                db.session.commit()
                flash(u"Сохранено")
                return redirect(url_for("medicine"))
    return render_template('medicine/edit.html',
                           title=u'Лекарства',
                           form=form)
