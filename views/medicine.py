# -*- coding: utf-8 -*-
from .. import app, db
from ..forms import MedicineForm
from ..models import Medicine, Dosage
from flask import render_template, flash, redirect, request, url_for


@app.route('/medicine<id>', methods=['GET', 'POST'])
def medicine_edit(id):
    medicine = Medicine.query.get(id)
    form = MedicineForm(obj=medicine)
    if request.method == 'POST':
        form = MedicineForm(request.form, obj=medicine)
        if form.validate_on_submit():
            if form.validate():
                form.populate_obj(medicine)
                db.session.add(medicine)
                db.session.commit()
                flash(u"Сохранено")
    ctx = dict(form=form, title=medicine.title)
    return render_template('medicine/edit.html', **ctx)


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
                return redirect(url_for('medicine_list'))
    return render_template('medicine/edit.html',
                           title=u'Лекарства',
                           form=form)

@app.route('/medicine', methods=['GET', 'POST'])
@app.route('/medicine/<int:page>', methods=['GET', 'POST'])
def medicine_list(page=1):
    medicines = Medicine.query.order_by('title').paginate(page, 10, False)
    ctx = dict(medicines=medicines, title=u'Препараты')
    return render_template('medicine/list.html', **ctx)



